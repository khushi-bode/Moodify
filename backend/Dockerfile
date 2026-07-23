FROM python:3.10-slim

WORKDIR /app



COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the application using Uvicorn. Render injects the PORT environment variable.
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}
