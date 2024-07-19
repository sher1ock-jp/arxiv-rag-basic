from pprint import pprint 
# from search_words import create_search_words
from arxiv_query import query_arxiv
from text_extraction import download_pdf
# from post_processing import filter_results
# from embedding import get_embeddings
# from tsp_solver import solve_tsp
# from summarizer import summarize_papers
# from integrator import integrate_summaries
save_path = './pdf_storage'

def main(paper_title):
    # search_words = create_search_words(user_question)
    # print(search_words)
    # arxiv_results = [query_arxiv(word) for word in search_words]
    pdf_url = query_arxiv(paper_title)
    pprint(pdf_url)
    download_pdf(pdf_url, save_path)
    # filtered_results = []
    # for search_word, results in zip(search_words, arxiv_results):
    #     filtered_results.extend(filter_results(results, search_word))
    # print("filterd_results",filtered_results)
    # embeddings = get_embeddings(filtered_results)
    # sorted_results = solve_tsp(embeddings)
    # summaries = summarize_papers(sorted_results)
    # final_report = integrate_summaries(summaries)
    # return final_report

if __name__ == "__main__":
    paper_title = "Neuromorphic Correlates of Artificial Consciousness"
    report = main(paper_title)
    print(report)