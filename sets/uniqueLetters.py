def find_unique_letters(word):
    letters = set()
    for c in word:
        letters.add(c)
    return letters


word = input("Enter a word: ")
unique_letters = find_unique_letters(word)
print("Unique letters in the word:", unique_letters)