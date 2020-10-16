def palindrome(word, index):
    if word == word[::-1]:
        message = f"{word} is a palindrome"
    else:
        message = f"{word} is not a palindrome"
    return message