from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import asyncio
import concurrent.futures
import numpy as np

app = FastAPI(
    title="Embedding API - multilingual-e5-large",
    description="API for generating multilingual sentence embeddings using E5-large.",
    version="1.1.0"
)

model = SentenceTransformer("intfloat/multilingual-e5-large")
MAX_BATCH_SIZE = 64

class EmbedRequest(BaseModel):
    texts: list[str]

class EmbedResponse(BaseModel):
    embeddings: list[list[float]]

executor = concurrent.futures.ThreadPoolExecutor()

@app.post("/embed", response_model=EmbedResponse)
async def embed(request: EmbedRequest):
    loop = asyncio.get_event_loop()
    embeddings = await loop.run_in_executor(
        executor, lambda: model.encode(request.texts, batch_size=32, show_progress_bar=False)
    )
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    return {"embeddings": embeddings.tolist()}
