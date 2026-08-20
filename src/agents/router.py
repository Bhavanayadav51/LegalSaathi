from langchain_groq import ChatGroq

from src.utils.config import (
    GROQ_API_KEY,
    LLM_MODEL
)


def get_router():

    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=LLM_MODEL,
        temperature=0
    )


def classify_question(question, llm):

    prompt = f"""
You are a classifier.

Classify the question into ONE category.

LEGAL_RAG:
Questions that require searching legal documents.

GENERAL_LLM:
Greetings, general knowledge, small talk,
definitions not requiring legal documents.

Respond with ONLY:

LEGAL_RAG

or

GENERAL_LLM

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip()