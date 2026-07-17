import streamlit as st
import json
import os


st.set_page_config(
    page_title="Tech News Automation Pro",
    page_icon="📰",
    layout="wide"
)


st.title("📰 Tech News Automation Pro")
st.subheader("Automated Technology & Cybersecurity Intelligence Platform")


st.divider()


DATABASE = "articles.json"


# Load AI generated articles

if not os.path.exists(DATABASE):

    st.error("articles.json not found. Run main.py first.")
    st.stop()


with open(
    DATABASE,
    "r",
    encoding="utf-8"
) as file:

    articles = json.load(file)



# Sidebar search

st.sidebar.title("Search News")


search = st.sidebar.text_input(
    "Search articles"
)


if search:

    articles = [
        article
        for article in articles
        if search.lower()
        in article.get(
            "title",
            ""
        ).lower()
    ]



# Dashboard statistics

st.subheader("Platform Overview")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "AI Articles Published",
        len(articles)
    )


with col2:

    st.metric(
        "Technology Articles",
        len(
            [
                a for a in articles
                if a.get("category")
            ]
        )
    )


with col3:

    st.metric(
        "Sources",
        len(
            set(
                a.get(
                    "source",
                    ""
                )
                for a in articles
            )
        )
    )



st.divider()



# Display articles

st.subheader(
    "📰 Latest AI Rewritten Technology News"
)



for article in reversed(articles[-10:]):


    image = article.get(
        "image",
        ""
    )


    if image:

        st.image(
            image,
            width=500
        )

    st.markdown(
        f"""
    # {article.get("title", "No title")}


    **Category:** {article.get("category", "Technology")}


    ## Article


    {article.get("content", "No content available")}


    ## Summary


    {article.get("summary", "No summary available")}


    ---
    """
    )