import openai
import json

def create_search_words(user_question: str):
    client = openai.Client()
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": """ユーザーの質問に対して、論文を検索するためのArxivの検索ワードを3個パターンしてください。
             出力はJSON形式で、search_wordsをキーとして、値はリスト形式で出してください。"""},
            {"role": "user", "content": user_question},
        ],
        temperature=0,
        response_format = {"type": "json_object"},
        max_tokens=512,
    )
    search_words = json.loads(response.choices[0].message.content)["search_words"]
    return search_words