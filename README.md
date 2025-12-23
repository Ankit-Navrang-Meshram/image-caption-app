# 🖼️ AI Image Captioning & Speech App

A full-stack AI application that generates descriptive captions for images.

Built with **FastAPI** (Backend), **Streamlit** (Frontend), and **Docker**.

## 🚀 Features
- **AI Image Captioning:** Uses the `Salesforce/blip-image-captioning-base` model to analyze images.
- **Microservices Architecture:** Backend and Frontend are decoupled.
- **Containerized:** Fully wrapped in Docker for easy deployment.

## 🛠️ Tech Stack
- **Model:** Hugging Face Transformers (BLIP)
- **Backend:** FastAPI, Uvicorn
- **Frontend:** Streamlit
- **Deployment:** Docker & Docker Compose

---

## 📦 How to Run (Recommended)
The easiest way to run this app is using Docker.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ankit-Navrang-Meshram/image-caption-app.git
   cd image-caption-app

```

2. **Run with Docker Compose:**
```bash
docker-compose up --build

```


3. **Open the App:**
* Frontend: [http://localhost:8501](https://www.google.com/search?q=http://localhost:8501)
* Backend Docs: [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)



---

## 🔧 How to Run Locally (Without Docker)

If you prefer running it manually, you need two terminal windows.

**1. Setup Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

```

**2. Start Backend (Terminal 1)**

```bash
uvicorn app.main:app --reload --port 8000

```

**3. Start Frontend (Terminal 2)**
*Note: You may need to update `API_URL` in `frontend/ui.py` to `http://127.0.0.1:8000/predict` if it's set to the Docker hostname.*

```bash
streamlit run frontend/ui.py

```

## 📂 Project Structure

```text
├── app/
│   ├── main.py          # FastAPI endpoints
│   └── model.py         # AI Model logic
├── frontend/
│   └── ui.py            # Streamlit Interface
├── Dockerfile           # Docker instructions
├── docker-compose.yml   # Orchestration
├── requirements.txt     # Dependencies
└── README.md

```
# 3. Push to GitHub
git push

```
