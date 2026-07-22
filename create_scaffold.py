import os

dirs_to_create = [
    "backend/app/api",
    "backend/app/core",
    "backend/app/models",
    "backend/app/schemas",
    "backend/app/db",
    "backend/app/services",
    "database/migrations",
    "database/seeds",
    "shared",
    "docs/phase3",
    "assets/logos",
    "assets/icons",
    "assets/fonts"
]

files_to_create = {
    "assets/logos/.gitkeep": "",
    "assets/icons/.gitkeep": "",
    "assets/fonts/.gitkeep": "",
    "database/.gitkeep": "",
    "shared/.gitkeep": "",
    "docs/phase3/.gitkeep": "",
    "database/README.md": "# Database\nTarget database is Supabase PostgreSQL. Store connection strings in environment variables.",
    "backend/.env.example": "SUPABASE_URL=\nSUPABASE_KEY=\nDATABASE_URL=",
    "backend/app/__init__.py": "",
    "backend/app/api/__init__.py": "",
    "backend/app/core/__init__.py": "",
    "backend/app/models/__init__.py": "",
    "backend/app/schemas/__init__.py": "",
    "backend/app/db/__init__.py": "",
    "backend/app/services/__init__.py": "",
    "backend/requirements.txt": "fastapi==0.110.0\nuvicorn==0.29.0\nsqlalchemy==2.0.29\nalembic==1.13.1\npydantic==2.6.4\npydantic-settings==2.2.1\n",
    ".gitignore": "node_modules/\n.next/\n__pycache__/\n*.pyc\n.env\n.env.*\n!.env.example\n.DS_Store\nvenv/\nenv/\n",
    "README.md": "# Moodify\n\n## Project Structure\n\n- `frontend/`: Next.js web application\n- `backend/`: FastAPI backend service\n- `database/`: Database schema, migrations, and seeds (Supabase PostgreSQL)\n- `shared/`: Shared definitions and constants\n- `docs/`: Project documentation\n- `assets/`: Design assets\n\n## Running Locally\n\n### Frontend\n1. `cd frontend`\n2. `npm install`\n3. `npm run dev`\n\n### Backend\n1. `cd backend`\n2. `pip install -r requirements.txt`\n3. `uvicorn app.main:app --reload`\n"
}

for d in dirs_to_create:
    os.makedirs(d, exist_ok=True)

for path, content in files_to_create.items():
    with open(path, "w") as f:
        f.write(content)

print("Scaffold complete.")
