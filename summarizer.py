import openai
from config import API_KEY

openai.api_key = API_KEY

def summarize_papers(papers):
    summaries = []
    for paper in papers:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "The user provides the Title and Abstract of the paper. Please give a short summary of this paper."},
                {"role": "user", "content": f"Title: {paper.title}\nAbstract: {paper.summary}"}
            ],
            max_tokens=100
        )
        summaries.append(response.choices[0].message['content'].strip())
    return summaries