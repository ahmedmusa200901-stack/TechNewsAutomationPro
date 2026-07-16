import requests


API_KEY = "3b643d03e63f4c61b5693824a22ac1b1"


def get_news():

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=(cybersecurity OR hacking OR malware OR ransomware OR vulnerability OR data breach OR artificial intelligence OR cloud OR software)"
        f"&language=en"
        f"&sortBy=publishedAt"
        f"&pageSize=5"
        f"&domains=therecord.media,bleepingcomputer.com,darkreading.com,securityweek.com,thehackernews.com"
        f"&apiKey={API_KEY}"
    )


    response = requests.get(url)


    if response.status_code != 200:
        return "Error fetching news."


    data = response.json()


    articles = data.get(
        "articles",
        []
    )


    news_list = []


    for article in articles:


        title = article.get(
            "title",
            "No Title"
        )


        source = article.get(
            "source",
            {}
        ).get(
            "name",
            "Unknown Source"
        )


        url = article.get(
            "url",
            "No URL Available"
        )


        image = article.get(
            "urlToImage",
            ""
        )


        title_lower = title.lower()


        # Category detection

        if any(word in title_lower for word in [
            "ai",
            "artificial intelligence",
            "machine learning",
            "chatgpt",
            "openai"
        ]):

            category = "Artificial Intelligence"


        elif any(word in title_lower for word in [
            "cloud",
            "aws",
            "azure",
            "google cloud"
        ]):

            category = "Cloud Computing"


        elif any(word in title_lower for word in [
            "iphone",
            "android",
            "mobile",
            "smartphone"
        ]):

            category = "Mobile Technology"


        elif any(word in title_lower for word in [
            "software",
            "windows",
            "linux",
            "update",
            "application"
        ]):

            category = "Software"


        else:

            category = "Cybersecurity"



        # Remove unreliable sources

        if source.lower() == "internet":
            continue



        news_list.append(
            {
                "title": title,

                "source": source,

                "url": url,

                "image": image,

                "category": category
            }
        )


    return news_list