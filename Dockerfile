FROM animcogn/face_recognition:cpu

RUN pip install --upgrade pip && pip install \
    fastapi \
    uvicorn \
    pillow \
    numpy \
    pydantic

COPY app /app
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
