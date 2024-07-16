def filter_results(results, search_word):
    filtered = []
    for result in results:
        for item in result:
            if all(word in item.title.lower() for word in search_word.split(" ")):
                filtered.append(item)
    return filtered