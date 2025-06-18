from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import base64
import io
import numpy as np
from PIL import Image
import face_recognition

app = FastAPI()


class ImageData(BaseModel):
    image_b64: str


class CompareData(BaseModel):
    captured_encoding: str
    user_encodings: List[str]


def decode_image(image_b64: str) -> np.ndarray:
    try:
        if image_b64.startswith("data:"):
            image_b64 = image_b64.split(",")[1]

        image_data = base64.b64decode(image_b64)
        image = Image.open(io.BytesIO(image_data))

        if image.mode == "RGBA":
            background = Image.new("RGBA", image.size, (255, 255, 255, 255))
            image = Image.alpha_composite(background, image).convert("RGB")
        elif image.mode != "RGB":
            image = image.convert("RGB")

        image_np = np.array(image)

        if image_np.ndim != 3 or image_np.shape[2] != 3:
            raise HTTPException(status_code=400, detail="Image must have 3 channels (RGB)")

        return image_np

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image: {str(e)}")


@app.post("/face_encoding")
def face_encoding(data: ImageData):
    image_np = decode_image(data.image_b64)
    encodings = face_recognition.face_encodings(image_np)
    if not encodings:
        raise HTTPException(status_code=400, detail="No face detected.")
    return {
        "encoding": base64.b64encode(encodings[0].tobytes()).decode()
    }


@app.post("/compare_faces")
def compare_faces(data: CompareData):
    captured = np.frombuffer(base64.b64decode(data.captured_encoding), dtype=np.float64)
    known_encodings = [
        np.frombuffer(base64.b64decode(enc), dtype=np.float64)
        for enc in data.user_encodings
    ]
    matches = face_recognition.compare_faces(known_encodings, captured)
    matched_index = next((i for i, matched in enumerate(matches) if matched), None)
    return {"matched_index": matched_index}
