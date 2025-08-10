
# WaterM Backend (Restructured)

## Run
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Open http://127.0.0.1:8000/docs
