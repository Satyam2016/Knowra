import streamlit as st
import requests

st.set_page_config(page_title="Knowra", layout="wide")
st.title("📘 Knowra — Intelligent Document Search")

query = st.text_input("Ask a question about your documents")

if query:
    response = requests.post(
        "http://localhost:8000/chat",
        params={"query": query}
    ).json()

    st.subheader("Answer")
    st.write(response["sources"][0]["text"])

    st.subheader("Sources")
    for src in response["sources"]:
        with st.expander(f"📄 Page {src['page']}"):
            st.write(src["text"])