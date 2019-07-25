raw_data = input()
data = raw_data.lower()
    counts = dir()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count(data))
