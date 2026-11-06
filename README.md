# Stress Detection Web Application

This project connects the React frontend ([`home.jsx`](file:///d:/Stress/home.jsx)) with the Flask machine learning backend ([`app.py`](file:///d:/Stress/app.py)) without modifying either source file.

---

## Architecture

- **Backend ([`app.py`](file:///d:/Stress/app.py))**:
  - Flask API running on `http://localhost:5000`
  - CORS enabled to allow requests from the React frontend
  - Endpoint: `POST /predict` taking `{"text": "..."}`
  - Model directory: [`stress_model_final/`](file:///d:/Stress/stress_model_final/) containing the trained sequence classification model & tokenizer

- **Frontend ([`home.jsx`](file:///d:/Stress/home.jsx))**:
  - React component mounted via [`main.jsx`](file:///d:/Stress/main.jsx) and bundled with Vite ([`vite.config.js`](file:///d:/Stress/vite.config.js))
  - Served on `http://localhost:3000`
  - Sends text to `http://localhost:5000/predict` and displays stress predictions and confidence

---

## How to Run

### Option 1: One-Click Launcher (Windows)
Double-click [`start.bat`](file:///d:/Stress/start.bat) or run:
```cmd
.\start.bat
```
This automatically launches both backend and frontend in separate windows and opens your browser to `http://localhost:3000`.

---

### Option 2: Run Separately in Terminal

#### 1. Start the Flask Backend:
```bash
.venv\Scripts\python.exe app.py
```
Backend will be available at `http://localhost:5000`.

#### 2. Start the Frontend (in a new terminal):
```bash
npm run dev
```
Open your browser at `http://localhost:3000`.
