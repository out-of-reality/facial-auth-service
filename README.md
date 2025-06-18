# Face Recognition API

A lightweight, containerized microservice built with FastAPI that provides facial recognition capabilities through REST endpoints. This service enables face detection, encoding extraction, and face matching functionality for authentication and identification systems.

## 🚀 Features

- **Face Encoding**: Extract facial encodings from base64-encoded images
- **Face Comparison**: Compare captured face encodings against known user encodings
- **RESTful API**: Clean FastAPI endpoints with automatic documentation
- **Containerized**: Docker-ready with multi-architecture support (AMD64/ARM64)
- **Production Ready**: Built on optimized face_recognition library
- **Image Format Support**: Handles various image formats including RGBA conversion

## 📋 API Endpoints

### POST `/face_encoding`
Extract facial encoding from an image.

**Request Body:**
```json
{
  "image_b64": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ..."
}
```

**Response:**
```json
{
  "encoding": "base64-encoded-face-encoding"
}
```

### POST `/compare_faces`
Compare faces and find matches against known encodings.

**Request Body:**
```json
{
  "captured_encoding": "base64-encoded-captured-face",
  "user_encodings": ["encoding1", "encoding2", "encoding3"]
}
```

**Response:**
```json
{
  "matched_index": 1
}
```
*Returns the index of the matched face or `null` if no match found.*

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for APIs
- **face_recognition** - State-of-the-art facial recognition library
- **Docker** - Containerization with multi-platform support
- **Pillow** - Image processing capabilities
- **NumPy** - Numerical computations
- **Pydantic** - Data validation and serialization

## 🏃‍♂️ Quick Start

### Using Docker (Recommended)

1. **Pull the image:**
   ```bash
   docker pull outofreality/face_recognition:latest
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 outofreality/face_recognition:latest
   ```

3. **Access the API:**
   - API: `http://localhost:5000`
   - Interactive docs: `http://localhost:5000/docs`
   - OpenAPI schema: `http://localhost:5000/openapi.json`

### Building from Source

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd facial-auth-service
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t face-recognition-api .
   ```

3. **Run the container:**
   ```bash
   docker run -p 5000:5000 face-recognition-api
   ```

### Local Development

1. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn pillow numpy pydantic face_recognition
   ```

2. **Run the development server:**
   ```bash
   cd app
   uvicorn main:app --host 0.0.0.0 --port 5000 --reload
   ```

## 📖 Usage Examples

### Python Example

```python
import requests
import base64

# Read and encode image
with open("photo.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Extract face encoding
response = requests.post(
    "http://localhost:5000/face_encoding",
    json={"image_b64": f"data:image/jpeg;base64,{encoded_string}"}
)

if response.status_code == 200:
    encoding = response.json()["encoding"]
    print("Face encoding extracted successfully!")
else:
    print("Error:", response.json())
```

### JavaScript Example

```javascript
// Convert image to base64
const fileInput = document.getElementById('imageInput');
const file = fileInput.files[0];
const reader = new FileReader();

reader.onload = async function(e) {
    const base64Image = e.target.result;
    
    try {
        const response = await fetch('http://localhost:5000/face_encoding', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                image_b64: base64Image
            })
        });
        
        const result = await response.json();
        console.log('Face encoding:', result.encoding);
    } catch (error) {
        console.error('Error:', error);
    }
};

reader.readAsDataURL(file);
```

### cURL Example

```bash
# Extract face encoding
curl -X POST "http://localhost:5000/face_encoding" \
     -H "Content-Type: application/json" \
     -d '{
       "image_b64": "data:image/jpeg;base64,YOUR_BASE64_IMAGE_HERE"
     }'

# Compare faces
curl -X POST "http://localhost:5000/compare_faces" \
     -H "Content-Type: application/json" \
     -d '{
       "captured_encoding": "CAPTURED_ENCODING_HERE",
       "user_encodings": ["ENCODING_1", "ENCODING_2"]
     }'
```

## 🐳 Docker Details

The service is built using a multi-stage Docker build process:

- **Base Image**: `animcogn/face_recognition:cpu` (optimized for CPU inference)
- **Port**: 5000
- **Architecture Support**: AMD64, ARM64
- **Health Check**: Built-in FastAPI health endpoints

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` | Server host binding |
| `PORT` | `5000` | Server port |

## 🔧 Configuration

The service accepts various image formats and automatically handles:
- **RGBA to RGB conversion**
- **Base64 decoding** (with or without data URI prefix)
- **Image validation** (ensures 3-channel RGB images)
- **Error handling** for invalid images or missing faces

## 🎯 Use Cases

- **User Authentication Systems**
- **Access Control Applications** 
- **Identity Verification Services**
- **Security Monitoring Systems**
- **Attendance Management**
- **Customer Recognition**

## 📝 Error Handling

The API returns appropriate HTTP status codes and error messages:

- **400 Bad Request**: Invalid image format, no face detected
- **422 Unprocessable Entity**: Invalid request body
- **500 Internal Server Error**: Server processing error

Example error response:
```json
{
  "detail": "No face detected."
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [face_recognition Library](https://github.com/ageitgey/face_recognition)
- [Docker Hub Image](https://hub.docker.com/r/outofreality/face_recognition)

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

Made with ❤️ using FastAPI and face_recognition
