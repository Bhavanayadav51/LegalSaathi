# LegalSaathi

## AI-Powered Multilingual Legal Assistant using Retrieval-Augmented Generation (RAG)

### Overview

LegalSaathi is a multilingual legal question-answering system that provides document-grounded responses to Indian legal queries using a Retrieval-Augmented Generation (RAG) architecture. The application retrieves relevant sections from legal documents stored in a Chroma vector database and uses a Groq-hosted large language model to generate accurate, context-aware answers.

Unlike conventional chatbots, LegalSaathi does not rely solely on the LLM's pretrained knowledge. Every legal response is generated from the retrieved document context, reducing hallucinations and improving reliability.

---

## Key Features

* Retrieval-Augmented Generation (RAG) for grounded legal responses
* Semantic document retrieval using Hugging Face embeddings
* Multilingual query support with automatic language detection and translation
* Intelligent routing between general conversational queries and legal document retrieval
* ChromaDB vector database for efficient similarity search
* Interactive conversational interface built with Streamlit

---

## System Architecture

```text
                        User Query
                             │
                             ▼
                 Language Detection
                             │
                             ▼
          Translate to English (if required)
                             │
                             ▼
                Intelligent Query Router
                    │                 │
                    │                 │
          GENERAL_LLM           LEGAL_RAG
                    │                 │
                    │          Semantic Retriever
                    │                 │
                    │        Chroma Vector Store
                    │                 │
                    └──────────► Retrieved Context
                                  │
                                  ▼
                           Prompt Construction
                                  │
                                  ▼
                              Groq LLM
                                  │
                                  ▼
                  Translate to User Language
                                  │
                                  ▼
                           Final Response
```

---

## Document Ingestion Pipeline

Before users interact with the system, legal PDF documents are converted into a searchable knowledge base.

```text
Legal PDFs
     │
     ▼
PDF Loader
     │
     ▼
Text Extraction
     │
     ▼
Document Chunking
     │
     ▼
Hugging Face Embeddings
     │
     ▼
ChromaDB Vector Store
```

Each document is divided into overlapping chunks, transformed into dense vector embeddings, and indexed for semantic retrieval.

---

## Query Processing Workflow

1. The user submits a legal question.
2. The system detects the input language.
3. Non-English queries are translated into English.
4. An LLM-based router classifies the query as either **GENERAL_LLM** or **LEGAL_RAG**.
5. Legal queries retrieve the most relevant document chunks using semantic search.
6. The retrieved context is combined with the user's question.
7. Groq LLM generates a grounded legal response.
8. The answer is translated back into the user's original language.

---

## Technology Stack

| Component            | Technology                         |
| -------------------- | ---------------------------------- |
| Programming Language | Python                             |
| LLM Framework        | LangChain                          |
| Large Language Model | Groq (Llama 3)                     |
| Vector Database      | ChromaDB                           |
| Embedding Model      | Hugging Face Sentence Transformers |
| User Interface       | Streamlit                          |
| Translation          | Deep Translator                    |
| Language Detection   | LangDetect                         |

---

## Project Structure

```text
LegalSaathi/
│
├── src/
│   ├── agents/
│   │   └── router.py
│   ├── retrieval/
│   │   ├── retriever.py
│   │   ├── qa_chain.py
│   │   └── vector_store.py
│   ├── ingestion/
│   │   ├── pdf_loader.py
│   │   └── text_splitter.py
│   ├── translation/
│   │   ├── language_detector.py
│   │   └── translator.py
│   └── utils/
│       └── config.py
│
├── data/
├── uploads/
├── chroma_db/
├── requirements.txt
└── agentic_legal_saathi.py
```

---

## Core Components

### Intelligent Query Router

The router distinguishes between conversational queries and legal research queries, ensuring that document retrieval is performed only when necessary. This improves both response quality and system efficiency.

### Semantic Retriever

The retriever performs similarity search over document embeddings stored in ChromaDB. It returns the most relevant legal document chunks rather than entire documents.

### Prompt Construction

Retrieved context is combined with structured instructions that constrain the LLM to answer only from the provided legal documents, reducing unsupported or hallucinated responses.

### Multilingual Support

Users can ask questions in multiple languages. Translation occurs before retrieval, and responses are translated back into the original language to provide a seamless multilingual experience.

---

## Example Queries

* How can I file an FIR in India?
* What is the procedure for obtaining bail?
* Explain Section 420 of the Indian Penal Code.
* What are the legal grounds for divorce?

---

## Future Enhancements

* Citation highlighting with document page references
* Voice-based multilingual legal assistant
* Case law recommendation engine
* Support for additional Indian regional languages
* Hybrid keyword and semantic retrieval for improved precision

---

## Author

**Bhavana Yadav**


