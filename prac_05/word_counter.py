text = input("Text: ")
words = text.split()
word_to_count = {}
keywords = []
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
        keywords.append(word)
keywords.sort()
for word in keywords:
    print("{:{}} : {}".format(word, len(max(keywords)), word_to_count[word]))
