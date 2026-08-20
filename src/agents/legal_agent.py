from src.agents.router import (
    get_router,
    classify_question
)

from src.retrieval.retriever import (
    get_retriever
)

from src.retrieval.qa_chain import (
    get_llm
)

from src.translation.language_detector import (
    detect_language
)

from src.translation.translator import (
    translate_to_english,
    translate_from_english
)


router = get_router()
retriever = get_retriever()
llm = get_llm()


def get_response(question):

    # ----------------------------------------
    # Detect Language
    # ----------------------------------------

    language = detect_language(question)
    print("Detected Language:", language)

    if language != "en":
        english_question = translate_to_english(question)
    else:
        english_question = question

    # ----------------------------------------
    # Route Question
    # ----------------------------------------

    route = classify_question(
        english_question,
        router
    )

    print("Route:", route)

    sources = []

    # ----------------------------------------
    # General Questions
    # ----------------------------------------

    if route == "GENERAL_LLM":

        response = llm.invoke(
            english_question
        )

        answer = response.content

    # ----------------------------------------
    # Legal Questions (RAG)
    # ----------------------------------------

    else:

        docs = retriever.invoke(
            english_question
        )

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        # Collect source metadata
        for i, doc in enumerate(docs, start=1):

            sources.append(
                {
                    "chunk": i,
                    "source": doc.metadata.get(
                        "source",
                        "Unknown Document"
                    ),
                    "page": doc.metadata.get(
                        "page",
                        "N/A"
                    )
                }
            )

        prompt = f"""
You are LegalSaathi, an AI legal assistant specializing in Indian labour laws.

Use ONLY the information provided in the context below.

Instructions:
- Answer ONLY from the provided context.
- Do NOT use outside knowledge.
- Do NOT make assumptions.
- If the answer is not present in the context, reply exactly:
"I couldn't find enough information in the uploaded legal documents to answer this question."
- Keep the answer clear, concise, and easy to understand.

Context:
{context}

Question:
{english_question}

Answer:
"""

        response = llm.invoke(
            prompt
        )

        answer = response.content

    print("Before Translation:", answer)

    # ----------------------------------------
    # Translate Back
    # ----------------------------------------

    if language != "en":

        answer = translate_from_english(
            answer,
            language
        )

    print("Final Answer:", answer)

    return {
        "answer": answer,
        "sources": sources
    }