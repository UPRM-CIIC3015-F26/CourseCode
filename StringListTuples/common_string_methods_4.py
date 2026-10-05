text = "antes ahora y siempre colegio"

# Count vowels in a string
def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count

print(f"Number of Vowels: {count_vowels(text)}")
# Find position of first consonant position
def find_first_consonant(text):
    for index in range(len(text)):
        char = text[index]
        if char.isalpha() and char.lower() not in "aeiou":
            return index
    return -1

print(f"First consonant position: {find_first_consonant(text) }")

# Replace all occurrences of a letter by another letter
replaced_letters = text.replace("e", "X")
print("Replace all 'e' with 'X':", replaced_letters)

# Replace first occurrence of a word by another word
# (count=1 replaces only the first occurrence)
replaced_word = text.replace("ahora", "hoy", 1)
print("Replace first occurrence of 'ahora' with 'hoy':", replaced_word)

# Split and Join Example
words = text.split()
print("Split into words:", words)
joined_text = "-".join(words)
print("Joined with dashes:", joined_text)