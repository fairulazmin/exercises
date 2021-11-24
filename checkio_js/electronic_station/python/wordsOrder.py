

def wordsOrder(text, words):
    text2 = text.split(' ')
    arr = [x for x in text2 if x in words]
    return len(set(arr)) == len(words) and arr == words

if __name__ == '__main__':
    print('Example:');
    print(wordsOrder('hi world im here', ['world', 'here']));

# These "asserts" are used for self-checking
assert wordsOrder('hi world im here', ['world', 'here']) == True
assert wordsOrder('hi world im here', ['here', 'world']) == False
assert wordsOrder('hi world im here', ['world']) == True
assert wordsOrder('hi world im here',
 ['world', 'here', 'hi']) == False
assert wordsOrder('hi world im here',
 ['world', 'im', 'here']) == True
assert wordsOrder('hi world im here',
 ['world', 'hi', 'here']) == False
assert wordsOrder('hi world im here', ['world', 'world']) == False
assert wordsOrder('hi world im here',
 ['country', 'world']) == False
assert wordsOrder('hi world im here', ['wo', 'rld']) == False
assert wordsOrder('', ['world', 'here']) == False
assert wordsOrder('hi world world im here',
 ['world', 'world']) == False

print("Coding complete? Click 'Check' to earn cool rewards!")
