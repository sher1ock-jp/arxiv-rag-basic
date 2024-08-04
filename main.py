# from search_words import create_search_words
from arxiv_query import query_arxiv
from paper_download import download_paper

# from embedding import get_embeddings
# from tsp_solver import solve_tsp
# from summarizer import summarize_papers
# from integrator import integrate_summaries

def main(arxiv_results):
    # search_words = create_search_words(user_question)
    # arxiv_results = [query_arxiv(word) for word in search_words]
    
    pdf_url = query_arxiv(arxiv_results)
    download_paper(pdf_url, paper_title)
    
    # embeddings = get_embeddings()
    
    # sorted_results = solve_tsp(embeddings)
    # summaries = summarize_papers(sorted_results)
    # final_report = integrate_summaries(summaries)
    # return final_report

if __name__ == "__main__":
    paper_title = "Neuromorphic Correlates of Artificial Consciousness"
    report = main(paper_title)
    print(report)