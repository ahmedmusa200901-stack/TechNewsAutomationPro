import streamlit as st
import os
import re


st.set_page_config(
    page_title="Tech News Automation Pro",
    page_icon="📰",
    layout="wide"
)


st.title("📰 Tech News Automation Pro")
st.subheader("Automated Technology & Cybersecurity Intelligence Platform")


st.divider()


reports_folder = "Reports"


if not os.path.exists(reports_folder):
    st.error("Reports folder not found")
    st.stop()


reports = [
    f for f in os.listdir(reports_folder)
    if f.endswith(".txt")
]


articles = []


for file in reports:

    path = os.path.join(
        reports_folder,
        file
    )


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as report:

        content = report.read()


        titles = re.findall(
            r"Title:\n(.*?)\n",
            content
        )

        sources = re.findall(
            r"Source:\n(.*?)\n",
            content
        )

        categories = re.findall(
            r"Technology Category:\n(.*?)\n",
            content
        )

        urls = re.findall(
            r"Article URL:\n(.*?)\n",
            content
        )

        images = re.findall(
            r"Image:\n(.*?)\n",
            content
        )

        summaries = re.findall(
            r"Summary:\n(.*?)\n",
            content
        )

        threats = re.findall(
            r"Threat Level:\n(.*?)\n",
            content
        )


        for i in range(len(titles)):

            articles.append(
                {
                    "title": titles[i],

                    "source":
                    sources[i]
                    if i < len(sources)
                    else "Unknown",

                    "category":
                    categories[i]
                    if i < len(categories)
                    else "Technology",

                    "url":
                    urls[i]
                    if i < len(urls)
                    else "#",

                    "image":
                    images[i]
                    if i < len(images)
                    else "",

                    "summary":
                    summaries[i]
                    if i < len(summaries)
                    else "No summary available",

                    "threat":
                    threats[i]
                    if i < len(threats)
                    else "Unknown"
                }
            )



# Sidebar search

st.sidebar.title("Search News")


search = st.sidebar.text_input(
    "Search articles"
)


if search:

    articles = [
        article for article in articles
        if search.lower()
        in article["title"].lower()
    ]



# Dashboard statistics

st.subheader("Platform Overview")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Articles Analysed",
        len(articles)
    )


with col2:

    high = len(
        [
            a for a in articles
            if a["threat"] == "HIGH"
        ]
    )

    st.metric(
        "High Risk Threats",
        high
    )


with col3:

    st.metric(
        "Reports Created",
        len(reports)
    )



st.divider()



# News cards

st.subheader("📰 Latest Technology Intelligence")


for article in reversed(articles[-10:]):


    if article["image"]:

        st.image(
            article["image"],
            width=500
        )


    st.markdown(
        f"""
## {article['title']}


**Source:** {article['source']}


**Technology Category:** {article['category']}


**Threat Level:** {article['threat']}


### Summary

{article['summary']}


🔗 [Read Full Article]({article['url']})


---
"""
    )