text = "aaabccccaa"
number = 1
prev_word = text[0]

counts = []
for word in text[1:]:
    if word == prev_word:
        number += 1
    else:
        counts.append([prev_word, number])
        number = 1
    prev_word = word
else:
    counts.append([prev_word, number])

planed = [sub_element for element in counts for sub_element in element]
print(*planed, sep='')
