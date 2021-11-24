

def correctSentence(text):
    if text[-1] != '.':
        return f'{text[0].upper()}{text[1:]}.'
    return f'{text[0].upper()}{text[1:]}'

if __name__ == '__main__':
    print('Example:')
    print(correctSentence('greetings, friends'))

# These "asserts" are used for self-checking
assert correctSentence('greetings, friends') == 'Greetings, friends.'
assert correctSentence('Greetings, friends') == 'Greetings, friends.'
assert correctSentence('Greetings, friends.') == 'Greetings, friends.'

print("Coding complete? Click 'Check' to earn cool rewards!")
