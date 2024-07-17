from search_words import create_search_words
from arxiv_query import query_arxiv
from post_processing import filter_results
from embedding import get_embeddings
from tsp_solver import solve_tsp
from summarizer import summarize_papers
from integrator import integrate_summaries

def main(user_question):
    search_words = create_search_words(user_question)
    arxiv_results = [query_arxiv(word) for word in search_words]
    filtered_results = []
    for search_word, results in zip(search_words, arxiv_results):
        filtered_results.extend(filter_results(results, search_word))
    embeddings = get_embeddings(filtered_results)
    sorted_results = solve_tsp(embeddings)
    summaries = summarize_papers(sorted_results)
    final_report = integrate_summaries(summaries)
    return final_report

if __name__ == "__main__":
    user_question = "画像生成のLoRA周りの技術トレンドを網羅的に知りたいです"
    report = main(user_question)
    print(report)