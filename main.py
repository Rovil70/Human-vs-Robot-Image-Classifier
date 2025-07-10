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

# Load model (use relative path for deployment!)
model = tf.keras.models.load_model("human_robot_classifier_model.h5")
class_names = ['Human', 'Robot']

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).resize((150, 150))
    image = np.array(image) / 255.0

    if image.shape[-1] == 4:  # PNG with alpha
        image = image[..., :3]

    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    predicted_class = class_names[np.argmax(prediction)]

    return {
        "prediction": predicted_class,
        "confidence": float(np.max(prediction))
    }
