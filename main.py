# FastAPI Backend (Prediction API)
# backend/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from PIL import Image
import numpy as np
import io

app = FastAPI()

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = tf.keras.models.load_model(r"D:\Practice+Learning\Human VS Robot Classifier\backend\human_robot_classifier_model.h5")
class_names = ['Human', 'Robot']

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).resize((150, 150))
    image = np.array(image) / 255.0
    


    if image.shape[-1] == 4:  # If PNG with alpha
        image = image[..., :3]

    image = np.expand_dims(image, axis=0)
    print("Image shape after resize:", image.shape)
    prediction = model.predict(image)
    predicted_class = class_names[np.argmax(prediction)]

    return {"prediction": predicted_class, "confidence": float(np.max(prediction))}
