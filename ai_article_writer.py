import os
import json
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def create_article(article):

    prompt = f"""
You are a professional technology news writer.

Rewrite the following original article into a new independent news article.

Rules:
- Do NOT copy sentences.
- Paraphrase everything.
- Create a professional news style.
- Add a clear headline.
- Add introduction, main details, and conclusion.
- Keep facts accurate.
- Return ONLY valid JSON.

Original article:

Title:
{article.get("title")}

Description:
{article.get("description")}

Content:
{article.get("content")}

Source:
{article.get("source")}

URL:
{article.get("url")}

Return this format:

{{
"title": "",
"content": "",
"summary": "",
"source": "",
"url": "",
"image": "",
"category": "Technology"
}}
"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )


    ai_text = response.choices[0].message.content

    ai_text = ai_text.replace("```json", "")
    ai_text = ai_text.replace("```", "")
    ai_text = ai_text.strip()


    try:

        article_json = json.loads(ai_text)

    except Exception:

        print("❌ AI did not return JSON")
        print(ai_text)

        return None


    return article_json