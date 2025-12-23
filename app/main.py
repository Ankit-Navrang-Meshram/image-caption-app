from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from app.model import generate_caption

app = FastAPI(title="Image Captioning API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Image Captioning API"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint to receive an image file and return a caption.
    """
    # 1. Read the image file from the upload
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # 2. Pass it to our model function
    caption = generate_caption(image)

    # 3. Return the result as JSON
    return {"caption": caption}