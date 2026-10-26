import streamlit as st

from document_processor import extract_text, extract_url
from rag import KnowledgeBase
from backend import ask_gemini, generate_decision_brief


# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title="AI Personal Knowledge Assistant",
    page_icon="🧠",
    layout="wide"
)
st.set_page_config(
    page_title="AI Personal Knowledge Assistant",
    page_icon="🧠",
    layout="wide"
)

with st.sidebar:
    st.header("🧠 About")

    st.write(
        """
        **AI Personal Knowledge & Decision Assistant**

        A workspace that helps users:

        • 📄 Upload documents  
        • 🌐 Read web sources  
        • 🔎 Search their knowledge  
        • 🤖 Ask AI questions  
        • 🎯 Generate decision briefs  
        """
    )

    st.divider()

    st.subheader("⚙️ Technology")

    st.write(
        """
        • Python  
        • Streamlit  
        • Gemini AI  
        • TF-IDF / RAG  
        • PDF / DOCX processing  
        • Web extraction
        """
    )

    st.divider()

    st.subheader("🧹 Session Controls")

    if st.button("🗑️ Clear Knowledge"):

        st.session_state.knowledge_base = KnowledgeBase()

        st.session_state.sources = []

        st.success("Knowledge cleared successfully!")

        st.rerun()



st.title("🧠 AI Personal Knowledge & Decision Assistant")

st.markdown(
    """
    ### Turn scattered knowledge into clear answers and smarter decisions.

    Upload your **documents**, add **web sources**, ask questions,
    and generate an evidence-based **Decision Brief**.
    """
)

st.info(
    "💡 Your knowledge stays within this session and is used to answer "
    "questions and support decisions."
)

st.divider()


# -----------------------------
# CREATE KNOWLEDGE BASE
# -----------------------------

if "knowledge_base" not in st.session_state:

    st.session_state.knowledge_base = KnowledgeBase()

if "sources" not in st.session_state:

    st.session_state.sources = []


# -----------------------------
# UPLOAD DOCUMENTS
# -----------------------------

st.header("📚 Add Your Knowledge")

uploaded_files = st.file_uploader(
    "Upload PDF, DOCX or TXT files",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)


if uploaded_files:

    for file in uploaded_files:

        # Avoid adding the same file repeatedly
        if file.name not in st.session_state.sources:

            try:

                pages = extract_text(file)

                st.session_state.knowledge_base.add_document(
                    pages,
                    file.name
                )

                st.session_state.sources.append(
                    file.name
                )

                st.success(
                    f"✅ {file.name} added successfully"
                )

            except Exception as e:

                st.error(
                    f"Error processing {file.name}: {e}"
                )
# -----------------------------
# ADD WEBSITE
# -----------------------------

st.header("🔗 Add a Website")

url = st.text_input(
    "Enter a website URL",
    placeholder="https://example.com"
)

if st.button("🌐 Add Website"):

    if not url:
        st.warning("Please enter a website URL.")

    else:

        with st.spinner("🌐 Reading website..."):

            try:

                website_text = extract_url(url)

                website_pages = extract_url(url)

                st.session_state.knowledge_base.add_document(
                    website_pages,
                    url
                )

                st.session_state.sources.append(
                    url
                )

                st.success(
                    "✅ Website added successfully!"
                )

            except Exception as e:

                st.error(
                    f"Could not read website: {e}"
                )

# -----------------------------
# SHOW SOURCES
# -----------------------------

if st.session_state.sources:

    st.subheader("📚 Knowledge Sources")

    for source in st.session_state.sources:

        st.write(f"📄 {source}")


st.divider()


st.divider()

tab1, tab2 = st.tabs([
    "💬 Ask Your Knowledge",
    "🎯 Decision Assistant"
])

# =========================
# ASK KNOWLEDGE TAB
# =========================

with tab1:

    st.subheader("💬 Ask Your Knowledge")

    question = st.text_input(
        "Ask a question about your knowledge",
        placeholder="Example: What are the main requirements?"
    )

    if st.button("🤖 Ask AI", key="ask_ai_button"):

        if not question:
            st.warning("Please enter a question.")

        elif not st.session_state.sources:
            st.warning(
                "Please upload documents or add a website first."
            )

        else:

            with st.spinner("🔎 Searching your knowledge..."):

                results = st.session_state.knowledge_base.search(
                    question,
                    top_k=3
                )

            if not results:

                st.warning("No relevant information found.")

            else:

                context = ""

                for result in results:

                    context += (
                        f"\n--- SOURCE: {result['source']} ---\n"
                        f"{result['text']}\n"
                    )

                with st.spinner(
                    "🤖 Gemini is generating the answer..."
                ):

                    try:

                        answer = ask_gemini(
                            question,
                            context
                        )

                        st.success("✅ Answer generated!")

                        st.subheader("🤖 AI Answer")

                        st.write(answer)

                        st.subheader("📚 Evidence Sources")

                        for result in results:

                            source = result["source"]

                            page = result["page"]

                            if page:
                                st.write(
                                    f"📄 **{source}** — "
                                    f"📍 Page {page} — "
                                    f"Relevance: `{result['score']:.2f}`"
                                )
                            else:
                                st.write(
                                    f"📄 **{source}** — "
                                    f"Relevance: `{result['score']:.2f}`"
                                )

                            if source.startswith("http://") or source.startswith("https://"):
                                st.markdown(
                                     f"🔗 [Open Source]({source})"
                                )

                    except Exception as e:

                        st.error(
                            f"AI error: {e}"
                        )


# =========================
# DECISION ASSISTANT TAB
# =========================

with tab2:

    st.subheader("🎯 Decision Assistant")

    st.write(
        "Turn your knowledge into a practical decision brief."
    )

    decision = st.text_input(
        "What decision are you trying to make?",
        placeholder="Example: Which technology should I choose?"
    )

    if st.button(
        "📋 Generate Decision Brief",
        key="decision_button"
    ):

        if not decision:

            st.warning("Please enter a decision.")

        elif not st.session_state.sources:

            st.warning(
                "Please upload documents or add a website first."
            )

        else:

            with st.spinner("🔎 Analyzing your knowledge..."):

                results = (
                    st.session_state.knowledge_base.search(
                        decision,
                        top_k=5
                    )
                )

            if not results:

                st.warning("No relevant information found.")

            else:

                context = ""

                for result in results:

                    context += (
                        f"\n--- SOURCE: {result['source']} ---\n"
                        f"{result['text']}\n"
                    )

                with st.spinner(
                    "🤖 Creating your decision brief..."
                ):

                    try:

                        brief = generate_decision_brief(
                            decision,
                            context
                        )

                        st.success(
                            "✅ Decision brief generated!"
                        )

                        st.subheader(
                            "📋 Decision Brief"
                        )

                        st.write(brief)

                        st.subheader(
                            "📚 Evidence Used"
                        )

                        shown_sources = set()

                        for result in results:

                            source = result["source"]

                            if source not in shown_sources:

                                page = result["page"]

                            if page:
                                st.write(
                                    f"📄 **{source}** — 📍 Page {page}"
                                )
                            else:
                                st.write(
                                    f"📄 **{source}**"
                                )

                                if (
                                    source.startswith("http://")
                                    or source.startswith("https://")
                                ):
                                    st.markdown(
                                        f"🔗 [Open Source]({source})"
                                    )

                                shown_sources.add(source)

                    except Exception as e:

                        st.error(
                            f"Decision assistant error: {e}"
                        )