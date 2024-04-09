def wordF(words):

    word_dist = {}
    for word in words:
        wordl = word.lower()
        if wordl in word_dist:
            word_dist[wordl] += 1
        else:
            word_dist[wordl] = 1

    return word_dist


myDist = ["Java", "dsa", "Java", "Python", "python", "C++"]

result = wordF(myDist)
for word, freq in result.items():
    print(f"{word}: {freq}")
