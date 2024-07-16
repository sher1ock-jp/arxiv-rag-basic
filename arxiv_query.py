import arxiv

def query_arxiv(search_word):
    arxiv_client = arxiv.Client()
    response = arxiv_client.results(
        search=arxiv.Search(
            query=search_word,
            max_results=100,
        )
    )
    return [item for item in response]