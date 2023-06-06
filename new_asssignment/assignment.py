def find_highest_frequency(string):
    words = string.split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    max_frequency = max(frequency.values())
    highest_frequency_word = [word for word, freq in frequency.items() if freq == max_frequency]

    return len(highest_frequency_word[0])

# Example input
string = "write write write all the number from from from 1 to 100"
output = find_highest_frequency(string)
print(output)
