import streamlit as st

from project import get_news_summary


st.set_page_config(
    page_title="Real-Time AI News Summarizer",
    page_icon="📰"
)

st.title("📰 Real-Time AI News Summarizer")

st.write(
    "Get real-time news summaries using Tavily Search and Mistral AI"
)


topic = st.text_input(
    "Enter a news topic",
    placeholder="Example: Latest AI news"
)


if st.button("Generate Summary"):

    if topic:

        with st.spinner("Fetching latest news..."):

            try:

                result = get_news_summary(topic)

                st.subheader("📌 News Summary")

                st.write(result)

            except Exception as e:

                st.error(e)

    else:

        st.warning("Please enter a topic")