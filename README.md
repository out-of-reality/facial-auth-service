# Face Recognition API

Face recognition microservice developed for the final project of Mechatronics Engineering. This service provides REST endpoints for facial encoding extraction and face comparison, designed to integrate with the `auth_faceid` module from the **out-of-reality** repository.

## Features

- Facial encoding extraction from base64 images
- Face comparison with known encodings
- REST API with FastAPI and automatic documentation
- Production-ready Docker container

## API Endpoints

### POST `/face_encoding`
Extracts facial encoding from an image.

```json
// Request
{
  "image_b64": "data:image/jpeg;base64,..."
}

// Response
{
  "encoding": "base64-encoded-face-encoding"
}
```

### POST `/compare_faces`
Compares a captured face with known encodings.

```json
// Request
{
  "captured_encoding": "base64-encoded-captured-face",
  "user_encodings": ["encoding1", "encoding2"]
}

// Response
{
  "matched_index": 1  // index of matching face or null
}
```

## Technologies

- **FastAPI** - Web framework for APIs
- **face_recognition** - Facial recognition library
- **Docker** - Containerization

## Installation and Usage

### With Docker

```bash
# Run the container
docker run -p 5000:5000 outofreality/face_recognition:latest
```

## Integration with out-of-reality

This microservice is designed to work with Odoo's `auth_faceid` module in the out-of-reality project, providing:

- Facial authentication for Odoo users
- Real-time identity verification
- Facial recognition-based access control system

---

**Final Project - Mechatronics Engineering**
