def are_anagrams(word1, word2):
    freq1 = {}
    for c in word1:
        if c in freq1:
            freq1[c]+=1
        else:
            freq1[c] = 1
    freq2 = {}
    for c in word2:
        if c in freq2:
            freq2[c]+=1
        else:
            freq2[c] = 1
    return freq1 == freq2


word1 = "ABBA"
word2 = "BA BA"

print(are_anagrams(word1, word2))