#he's going to post this solution later #difficult
def top_three(hist):
    sortedList = sorted(hist, key=hist.get)[::-1]

    print sortedList[:3]
    top_three_items = {}

    while len(top_three_items) < 3:
        highkey = ''
        highestValue = 0
        for key, value in tally.items():
            if value > highestValue:
                highkey = key
                highestValue = value
        top_three_items[highkey] = tally[highkey]
        del tally[highKey]
print top_three_items

top_three(word_histogram('to be or not to be'))
