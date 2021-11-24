from re import findall

def threeWords(text):
    return len(findall(r'[a-zA-Z]+\s[a-zA-Z]+\s[a-zA-Z]+', text)) != 0

if __name__ == '__main__':
    print('Example:')
    print(threeWords("Hello World hello"))

assert threeWords("Hello World hello") == True
assert threeWords("He is 123 man") == False
assert threeWords("1 2 3 4") == False
assert threeWords("bla bla bla bla") == True
assert threeWords("Hi") == False
assert threeWords("start 5 one two three 7 end") == True
print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
