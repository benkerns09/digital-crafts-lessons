def word_histogram(sentence):
    tally = { }
    wordsList = sentence.split()
    for word in wordsList:
        if tally.get(word):
            tally[word] += 1
        else:
            tally[word] = 1
    print tally

word_histogram('to be or not to be')