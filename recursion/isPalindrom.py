def isPalindrom(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        if(s[left] != s[right]):
            return False
        left += 1
        right -= 1
    return True

def isPalindromShowingOff(s: str) -> bool:
    return s == s[::-1]

def recIsPalindrom(s: str) -> list:
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return recIsPalindrom(s[1:len(s)-1])
    return False

word = "aabaa"
print(f"Is \"{word}\" a palindrom? {isPalindrom(word)}")
print(f"Is \"{word}\" a palindrom? {isPalindromShowingOff(word)}")
print(f"Is \"{word}\" a palindrom? {recIsPalindrom(word)}")