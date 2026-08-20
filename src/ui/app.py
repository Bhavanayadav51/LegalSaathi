import sys
import os

# Fix imports for Streamlit
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../.."
        )
    )
)

import streamlit as st

from src.agents.legal_agent import get_response

from src.ingestion.upload_processor import (
    ingest_uploaded_pdf
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="LegalSaathi",
    page_icon="⚖️",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("⚖️ LegalSaathi")

st.markdown(
    """
    AI-Powered Legal Assistant

    Agentic RAG + Groq + ChromaDB + Multilingual Support
    """
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("⚖️ LegalSaathi")

st.sidebar.success("System Ready")

# --------------------------------------------------
# Uploaded Documents
# --------------------------------------------------

st.sidebar.subheader(
    "Uploaded Documents"
)

if os.path.exists("uploads"):

    files = os.listdir("uploads")

    if files:

        for file in files:

            st.sidebar.write(
                f"📄 {file}"
            )

    else:

        st.sidebar.info(
            "No uploaded PDFs"
        )

# --------------------------------------------------
# Database Info
# --------------------------------------------------

st.sidebar.subheader(
    "Database"
)

if os.path.exists("uploads"):

    st.sidebar.write(
        f"Documents: {len(os.listdir('uploads'))}"
    )

# --------------------------------------------------
# PDF Upload
# --------------------------------------------------

st.sidebar.subheader(
    "📄 Upload Legal PDF"
)

uploaded_file = st.sidebar.file_uploader(
    "Choose PDF",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    # Duplicate Prevention
    if os.path.exists(file_path):

        st.sidebar.warning(
            "⚠️ This file has already been uploaded."
        )

    else:

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        with st.spinner(
            "Processing PDF..."
        ):

            try:

                chunks_added = (
                    ingest_uploaded_pdf(
                        file_path
                    )
                )

                st.sidebar.success(
                    f"✅ PDF Processed ({chunks_added} chunks added)"
                )

            except Exception as e:

                st.sidebar.error(
                    f"❌ Error: {str(e)}"
                )

# --------------------------------------------------
# Features
# --------------------------------------------------

st.sidebar.markdown(
    """
### Features

✅ Agentic Routing

✅ Legal RAG

✅ Groq LLM

✅ ChromaDB

✅ Multilingual Support

✅ Source Citations

---

Built with LangChain + LangGraph
"""
)

# --------------------------------------------------
# Clear Chat
# --------------------------------------------------

if st.sidebar.button(
    "🗑 Clear Chat"
):

    st.session_state.messages = []

    st.rerun()

# --------------------------------------------------
# Chat History Initialization
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []

# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask a legal question..."
)

# --------------------------------------------------
# Process User Query
# --------------------------------------------------

if question:

    # User Message
    with st.chat_message(
        "user"
    ):

        st.markdown(
            question
        )

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Assistant Response
    with st.spinner(
        "Analyzing legal documents..."
    ):

        try:

            result = get_response(
                question
            )

            answer = result["answer"]

            sources = result["sources"]

        except Exception as e:

            answer = (
                f"Error: {str(e)}"
            )

            sources = []

    with st.chat_message(
        "assistant"
    ):

        st.markdown(
            answer
        )

        # --------------------------------------------------
        # Sources Viewer
        # --------------------------------------------------

        if sources:

            st.markdown("---")

            st.markdown(
                "### 📚 Sources Used"
            )

            for source in sources:

                pdf_name = source.get(
                    "pdf",
                    "Unknown PDF"
                )

                page = source.get(
                    "page",
                    "Unknown"
                )

                chunk = source.get(
                    "chunk",
                    "Unknown"
                )

                text = source.get(
                    "text",
                    ""
                )

                with st.expander(
                    f"📄 {pdf_name} | Page {page} | Chunk {chunk}"
                ):

                    st.write(
                        text
                    )

    # Save only answer in chat history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )