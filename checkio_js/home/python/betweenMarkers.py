

def betweenMarkers(text, begin, end):
    return text[0 if begin not in text else text.index(begin) + len(begin) :
        len(text) if end not in text else text.index(end)]

if __name__ == '__main__':
    print('Example:')
    print(betweenMarkers('What is >apple<', '>', '<'), 'apple')


assert betweenMarkers('What is >apple<', '>', '<') == 'apple'
assert betweenMarkers("<head><title>My new site</title></head>",
                            "<title>", "</title>") == 'My new site'
assert betweenMarkers('No[/b] hi', '[b]', '[/b]') == 'No'
assert betweenMarkers('No [b]hi', '[b]', '[/b]') == 'hi'
assert betweenMarkers('No hi', '[b]', '[/b]') == 'No hi'
assert betweenMarkers('No <hi>', '>', '<') == ''
print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
