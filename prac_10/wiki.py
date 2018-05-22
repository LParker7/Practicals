import wikipedia

search_text = input("Search: ")
while search_text != "":
    try:
        search = wikipedia.page(search_text)
        summary = wikipedia.summary(search_text)
        print(search.title)
        print(summary)
        print(search.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_text = input("Search: ")
