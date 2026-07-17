import json
import os
from datetime import datetime


DATABASE_FILE = "articles.json"


def save_article(article):

    articles = []


    # Load existing articles
    if os.path.exists(DATABASE_FILE):

        with open(
            DATABASE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            try:
                articles = json.load(file)

            except json.JSONDecodeError:
                articles = []


    # Add date
    article["date"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M"
    )


    # Prevent duplicates
    existing_urls = [
        item.get("url")
        for item in articles
    ]


    if article.get("url") not in existing_urls:

        articles.append(article)


    # Save updated articles

    with open(
        DATABASE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            articles,
            file,
            indent=4,
            ensure_ascii=False
        )


    return DATABASE_FILE