import openai

def get_embeddings(papers):
    texts = [paper.title + " " + paper.summary for paper in papers]
    response = openai.Embedding.create(input=texts, model="text-embedding-ada-002")
    embeddings = [r['embedding'] for r in response['data']]
    return embeddings