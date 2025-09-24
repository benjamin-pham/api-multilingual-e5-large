uvicorn embedding_api:app --host 0.0.0.0 --port 8181

docker build -t embedding-api .

docker run -d -p 8181:8181 embedding-api
