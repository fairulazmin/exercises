from re import findall

def firstWord(text):
    return findall(r"[a-zA-Z']+", text)[0]


if __name__ == '__main__':
    print('Example:')
    print(firstWord("Hello world"))

# These "asserts" using for self-checking and not for auto-testing
assert firstWord("Hello world") == "Hello"
assert firstWord(" a word ") == "a"
assert firstWord("don't touch it") == "don't"
assert firstWord("greetings, friends") == "greetings"
assert firstWord("... and so on ...") == "and"
assert firstWord("hi") == "hi"
print("Coding complete? Click 'Check' to earn cool rewards!")
