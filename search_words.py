from openai import OpenAI
import json
from config import API_KEY

client = OpenAI(
    api_key = API_KEY
)

def create_search_words(user_question: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": """ユーザーの質問に対して、論文を検索するためのArxivの検索ワードを3個パターンしてください。
                 出力はJSON形式で、search_wordsをキーとして、値はリスト形式で出してください。"""},
                {"role": "user", "content": user_question},
            ],
            temperature=0,
            max_tokens=512,
        )
        
        print("API Response:", response)
        
        
        message_content = response.choices[0].message.content
        print("Message Content:", message_content)
        
        
        search_words = json.loads(message_content)["search_words"]
        return search_words

    except Exception as e:
        print("Error:", e)
        return []