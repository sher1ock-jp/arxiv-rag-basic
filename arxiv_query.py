import arxiv

def query_arxiv(search_word):
    arxiv_client = arxiv.Client()
    response = arxiv_client.results(
        search=arxiv.Search(
            query=search_word,
            sort_by=arxiv.SortCriterion.Relevance,
            sort_order=arxiv.SortOrder.Descending,
            max_results=1,
        )
    )
    urls = [item.entry_id for item in response]
    return urls