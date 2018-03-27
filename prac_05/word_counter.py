text = input("Text: ")
words = text.split()
word_to_count = {}

for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
keywords = sorted(word_to_count.keys())
max_word_length = max([len(word) for word in keywords])
for word in keywords:
    print("{:{}} : {}".format(word, max_word_length, word_to_count[word]))
