#!/bin/bash

IMAGE_NAME="outofreality/face_recognition:latest"

docker buildx create --use --name mybuilder --driver docker-container || true

docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t $IMAGE_NAME \
  --push \
  .

echo "✅ Image pushed to Docker Hub: $IMAGE_NAME"
