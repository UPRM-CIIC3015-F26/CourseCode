# make a program that counts the frequency of each character in a word
def count_chars(words):
    frequencies = {}
    for word in words: # goes over list
        for c in word: # goes over characters
            if c in frequencies:
                frequencies[c] += 1
            else:
                frequencies[c] = 1
    return frequencies
        

def most_frequent_char(words):
    freq = count_chars(words)

    max_freq = -1
    max_letter = ''
    for f in freq:
        if freq[f] > max_freq:
            max_freq = freq[f]
            max_letter = f
    return max_letter
    
    

animals = ["dog", "cat", "bird", "frog", "dingo", "fox"]

print(count_chars(animals))
print(f"The most frequent letter is: {most_frequent_char(animals)}")
