"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

text = input("Text: ")
words = text.split()
word_counts = {}
max_width = 0

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

    if len(word) > max_width:
        max_width = len(word)

sorted_words = sorted(word_counts)
for word in sorted_words:
    count = word_counts[word]
    print(f"{word:{max_width}} : {count}")