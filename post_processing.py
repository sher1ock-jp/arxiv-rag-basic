def filter_results(results, search_word):
    filtered = []
    for item in results:
        if any(word.lower() in item.title.lower() for word in search_word.split(" ")):
                filtered.append(item)
    return filtered