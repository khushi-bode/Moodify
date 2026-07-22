import io
from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.colors import HexColor

router = APIRouter(prefix="/reports", tags=["reports"])

class ReportData(BaseModel):
    summary: str
    period: str
    emotion_breakdown: dict[str, int]
    task_completion_rate: int

@router.post("/generate-pdf")
def generate_pdf(data: ReportData):
    """
    Internal endpoint to generate a PDF report from provided data using ReportLab.
    """
    try:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)
        
        styles = getSampleStyleSheet()
        
        # Custom styles for Moodify
        title_style = ParagraphStyle(
            'MoodifyTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=HexColor('#3B82F6') # color-primary
        )
        
        heading_style = ParagraphStyle(
            'MoodifyHeading',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            spaceBefore=20,
            textColor=HexColor('#1E293B')
        )
        
        body_style = ParagraphStyle(
            'MoodifyBody',
            parent=styles['Normal'],
            fontSize=12,
            leading=18,
            spaceAfter=12,
            textColor=HexColor('#475569')
        )

        elements = []
        
        # Header
        period_title = data.period.capitalize()
        elements.append(Paragraph(f"Moodify {period_title} Report", title_style))
        
        # Summary Section
        elements.append(Paragraph("Your Narrative Summary", heading_style))
        elements.append(Paragraph(data.summary, body_style))
        
        # Data Snapshot Section
        elements.append(Spacer(1, 20))
        elements.append(Paragraph("Data Snapshot", heading_style))
        
        elements.append(Paragraph(f"<b>Task Completion Rate:</b> {data.task_completion_rate}%", body_style))
        
        # Emotion Breakdown
        elements.append(Paragraph("<b>Emotion Breakdown:</b>", body_style))
        for emotion, count in data.emotion_breakdown.items():
            elements.append(Paragraph(f"- {emotion}: {count} scans", body_style))

        # Footer / Disclaimer
        elements.append(Spacer(1, 40))
        disclaimer = "Note: The insights provided by Moodify are AI-generated and not medical advice."
        disclaimer_style = ParagraphStyle('Disclaimer', parent=styles['Italic'], fontSize=10, textColor=HexColor('#94A3B8'))
        elements.append(Paragraph(disclaimer, disclaimer_style))

        # Build PDF
        doc.build(elements)
        
        pdf_value = buffer.getvalue()
        buffer.close()
        
        return Response(content=pdf_value, media_type="application/pdf")
        
    except Exception as e:
        print(f"PDF Generation Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate PDF")
