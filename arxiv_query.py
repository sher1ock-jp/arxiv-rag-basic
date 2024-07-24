import arxiv

def query_arxiv(search_word):
    try:
        arxiv_client = arxiv.Client()
        response = arxiv_client.results(
            search=arxiv.Search(
                query=search_word,
                sort_by=arxiv.SortCriterion.Relevance,
                sort_order=arxiv.SortOrder.Descending,
                max_results=1, # only get the top result(paper)
            )
        )
        result = next(response, None)
        if result:
            intro_url = result.entry_id # entory_id is the url of the paper
            pdf_url = intro_url.replace('abs', 'pdf')
            print(pdf_url)
            return pdf_url
    except Exception as e:
        print("Error:", e)
        return None
    