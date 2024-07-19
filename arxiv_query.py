import arxiv

def query_arxiv(search_word):
    try:
        arxiv_client = arxiv.Client()
        response = arxiv_client.results(
            search=arxiv.Search(
                query=search_word,
                sort_by=arxiv.SortCriterion.Relevance,
                sort_order=arxiv.SortOrder.Descending,
                max_results=1,
            )
        )
        result = next(response, None)
        if result:
            intro_url = result.entry_id
            pdf_url = intro_url.replace('abs', 'pdf')
            return pdf_url
    except Exception as e:
        print("Error:", e)
        return None
    