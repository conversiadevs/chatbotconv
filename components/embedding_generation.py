from sentence_transformers import SentenceTransformer
import pandas as pd
from config import save_path

def generate_embeddings(pages_and_chunks, min_token_length, model_name, device, logger):
    logger.info("inside embedding_generation.py")
    logger.info(f"Loading embedding model: {model_name}")

    df = pd.DataFrame(pages_and_chunks)
    filtered_chunks = df[df["chunk_token_count"] > min_token_length].to_dict(orient="records")

    embedding_model = SentenceTransformer(model_name_or_path=model_name, device=device)

    logger.info("Generating embeddings...")
    for item in filtered_chunks:
        item["embedding"] = embedding_model.encode(item["sentence_chunk"])
    
    text_chunks = [item["sentence_chunk"] for item in filtered_chunks]

    text_chunk_embeddings = embedding_model.encode(
        text_chunks,
        batch_size=32,
        convert_to_tensor=True
    )
    logger.info("Embeddings generated.")
    logger.info("exited embedding_generation.py")

    pd.DataFrame(filtered_chunks).to_csv(f"{save_path}/test_embeddings.csv", index=False)