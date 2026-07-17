import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_news():

    if not NEWS_API_KEY:
        print("❌ News API key missing")
        return []

    url = (
        "https://newsapi.org/v2/everything?"
       "q=(cybersecurity OR hacking OR malware OR ransomware "
"OR vulnerability OR artificial intelligence OR AI "
"OR cloud OR software OR Google "
"OR Microsoft OR Apple OR technology)"
        "&language=en"
        "&sortBy=publishedAt"
        "&pageSize=10"
        "&domains="
        "therecord.media,"
        "bleepingcomputer.com,"
        "darkreading.com,"
        "securityweek.com,"
        "&domains="
"therecord.media,"
"bleepingcomputer.com,"
"darkreading.com,"
"securityweek.com,"
"thehackernews.com,"
"bbc.com,"
"reuters.com,"
"apnews.com,"
"wired.com,"
"arstechnica.com,"
"zdnet.com,"
"cnet.com,"
"techcrunch.com,"
"theverge.com,"
"google.com,"
"blog.google.com"
        "thehackernews.com"
        f"&apiKey={NEWS_API_KEY}"
    )
    try:

        response = requests.get(url, timeout=15)

        if response.status_code != 200:
            print("❌ News API Error:")
            print(response.text)
            return []

        data = response.json()

        articles = data.get("articles", [])

        news_list = []

        for article in articles:
            title = article.get(
                "title",
                ""
            ).lower()

            allowed_words = [
                "cyber",
                "security",
                "hack",
                "malware",
                "ransomware",
                "vulnerability",
                "ai",
                "artificial intelligence",
                "cloud",
                "software",
                "data breach",
                "privacy"
            ]

            if not any(word in title for word in allowed_words):
                continue

            news_list.append(
                {
                    "title": article.get("title", ""),
                    "description": article.get("description", ""),
                    "content": article.get("content", ""),
                    "source": article.get("source", {}).get("name", ""),
                    "url": article.get("url", ""),
                    "image": article.get("urlToImage", ""),
                    "category": "Technology"
                }
            )

        print(f"✅ Found {len(news_list)} article(s)")

        return news_list

    except Exception as e:

        print("❌ Error:", e)

        return []