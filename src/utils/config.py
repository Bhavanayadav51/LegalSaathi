# config.py — Central settings file
# All project settings live here.

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ─────────────────────────────────────────────────────
# API Keys
# ─────────────────────────────────────────────────────

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "❌ GROQ_API_KEY not found. Please add it to your .env file."
    )


# ─────────────────────────────────────────────────────
# Groq LLM Settings
# ─────────────────────────────────────────────────────

LLM_MODEL = "llama-3.3-70b-versatile"

LLM_TEMPERATURE = 0.1

LLM_MAX_TOKENS = 1024


# ─────────────────────────────────────────────────────
# Embedding Model
# ─────────────────────────────────────────────────────

EMBEDDING_MODEL = "all-MiniLM-L6-v2"


# ─────────────────────────────────────────────────────
# ChromaDB Settings
# ─────────────────────────────────────────────────────

CHROMA_DB_PATH = "./chroma_db"

CHROMA_COLLECTION = "legal_docs"


# ─────────────────────────────────────────────────────
# PDF Processing Settings
# ─────────────────────────────────────────────────────

PDF_FOLDER = "./data/pdfs"

# Legal documents are usually long,
# so larger chunks work better.

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K_RESULTS = 4


# ─────────────────────────────────────────────────────
# Agent Settings
# ─────────────────────────────────────────────────────

MAX_RETRY_ATTEMPTS = 3

RELEVANCE_THRESHOLD = 0.5