import openai

def summarize_papers(papers):
    summaries = []
    for paper in papers:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"Title: {paper.title}\nAbstract: {paper.summary}\nPlease summarize this paper.",
            max_tokens=100
        )
        summaries.append(response.choices[0].text.strip())
    return summaries