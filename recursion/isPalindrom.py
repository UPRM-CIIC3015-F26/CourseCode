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
    pass

word = "kayak"
print(f"Is \"{word}\" a palindrom? {isPalindrom(word)}")
print(f"Is \"{word}\" a palindrom? {isPalindromShowingOff(word)}")