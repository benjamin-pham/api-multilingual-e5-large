```bash
uvicorn embedding_api:app --host 0.0.0.0 --port 8181
```bash
docker build -t embedding-api .
```bash
docker run -p 8181:8181 embedding-api
