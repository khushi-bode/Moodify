# Moodify

Moodify is an AI-powered mood tracking and wellness companion.

## Prerequisites
- **Node.js**: v18 or newer
- **Python**: v3.10 to v3.12 (**STRICT REQUIREMENT**. Python 3.13+ is NOT supported due to TensorFlow/DeepFace incompatibility on Windows).

## Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd moodify
```

### 2. Frontend Setup
```bash
cd frontend
npm install
```

### 3. Backend Setup
```bash
cd backend
python -m venv venv
# Activate virtual environment (Windows)
.\venv\Scripts\activate
# Activate virtual environment (Mac/Linux)
source venv/bin/activate

pip install -r requirements.txt
```

## Environment Variables

You must set up environment variables for both the frontend and backend.

### Frontend (`frontend/.env.local`)
Create a `.env.local` file in the `frontend` directory based on `frontend/.env.example`:
```env
NEXT_PUBLIC_SUPABASE_URL=your-supabase-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-anon-key
```

### Backend (`backend/.env`)
Create a `.env` file in the `backend` directory based on `backend/.env.example`:
```env
SUPABASE_URL=your-supabase-url
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
GEMINI_API_KEY=your-gemini-api-key
```

## Running the Project

### Running Frontend
From the `frontend` directory:
```bash
npm run dev
```
The application will be available at `http://localhost:3000`.

### Running Backend
From the `backend` directory (with virtual environment activated):
```bash
uvicorn app.main:app --reload
```
The FastAPI backend will run on `http://localhost:8000`.

## Common Issues & Troubleshooting

### DeepFace / TensorFlow Installation Failure
**Issue**: Running `pip install -r requirements.txt` fails with a `ResolutionImpossible` error for `tensorflow`.
**Cause**: You are likely running Python 3.13 or 3.14 on Windows, which do not yet have pre-built TensorFlow binaries. DeepFace strictly requires TensorFlow.
**Solution**: Uninstall your current Python version and install **Python 3.12**. Recreate your virtual environment (`python -m venv venv`) and try installing again.

### Camera Access Denied
**Issue**: The Mood Scan feature shows a fallback upload UI.
**Cause**: The browser blocked camera access, or you are running the app on a device without a webcam.
**Solution**: Ensure you are accessing the app over `localhost` or `HTTPS`, as browsers require secure contexts to use the camera. Allow camera permissions when prompted.

### Database Connection Issues
**Issue**: Cannot fetch or save mood history.
**Cause**: Supabase URL or keys are incorrect, or Row Level Security (RLS) is blocking the request.
**Solution**: Double-check your `.env` and `.env.local` files. Ensure you are logged in (RLS requires an authenticated user for most operations).
