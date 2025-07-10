# Human-vs-Robot-Image-Classifier
# 🤖 Human vs Robot Image Classifier

A deep learning-based web application that classifies whether the uploaded image is of a **Human** or a **Robot**.  
Built with **FastAPI** backend, optional **React** frontend, and a **CNN model** trained using Keras.

---

## 📌 Project Overview

- 🔍 Classifies input images into two categories: **Human** or **Robot**
- 🧠 Trained a CNN model with ~79% validation accuracy
- 🌐 FastAPI backend with prediction API
- 🖼️ React (or Streamlit) frontend for UI
- ☁️ Deployed on **Render** (optional)

---

## 🛠️ Tech Stack

| Layer       | Tools Used                    |
|-------------|-------------------------------|
| Language    | Python                        |
| ML/DL       | TensorFlow, Keras             |
| Backend     | FastAPI                       |
| Frontend    | React.js / Streamlit (optional) |
| Deployment  | Render, GitHub, Git LFS       |
| Others      | Git, GitHub, VS Code          |

---

## 🚀 How to Run Locally

### 🔧 Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Visit: http://127.0.0.1:8000/docs to test API.

🖥️ Frontend (React)
bash
Copy
Edit
cd frontend
npm install
npm start
🧪 Predict Image (Postman or Swagger UI)
POST /predict/
Form Data: file: <upload_image>

📚 Model Training
Training done in the following notebook:

📁 notebooks/Human_vs_Robot_Model_Training.ipynb

CNN with Conv2D + MaxPool + Dense layers

Binary classification (Human vs Robot)

Trained on custom dataset

📁 Project Structure
css
Copy
Edit
Human-vs-Robot-Image-Classifier/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── human_robot_classifier_model.h5
│
├── frontend/
│   ├── public/
│   ├── src/
│   └── package.json
│
├── notebooks/
│   └── Human_vs_Robot_Model_Training.ipynb
│
└── README.md
📦 Model File (Large)
The model file .h5 or .zip is stored using Git LFS due to large size.

✍️ Author
👤 Rovil Katariya

🔗 GitHub Profile

📫 Email: r8882katariya@gmail.com
