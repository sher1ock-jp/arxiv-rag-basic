import openai
from config import API_KEY

openai.api_key = API_KEY

def integrate_summaries(summaries):
    response = openai.ChatCompletion.create(
        model="claude-3-sonnet",
        messages=[
            {"role": "system", "content": "Summarize the following papers."},
            {"role": "user", "content": "\n".join(summaries)}
        ],
        max_tokens=1000
    )
    return response.choices[0].message['content'].strip()