import voyageai
from config import VOYAGE_API_KEY

vo = voyageai.Client(api_key=VOYAGE_API_KEY)

def get_embeddings():
    
    texts = ["Sample text 1", "Sample text 2"]

    result = vo.embed(texts, model="voyage-2", input_type="document")
    print(result.embeddings[0])
    print(result.embeddings[1])

# def get_embeddings(papers):
#     texts = [paper.title + " " + paper.summary for paper in papers]
#     response = openai.Embedding.create(input=texts, model="text-embedding-ada-002")
#     embeddings = [r['embedding'] for r in response['data']]
#     return embeddings