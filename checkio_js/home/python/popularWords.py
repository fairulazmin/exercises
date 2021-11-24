import re

def popularWords(text, words):
    num = [len(re.findall(re.compile(f'\\b{xxx}\\b', re.I), text)) for xxx in words]
    d = {}
    for x, y in zip (words, num):
        d[x] = y
    return d


if __name__ == '__main__':
    print('Example:')
    print(popularWords('''
When I was One
I had just begun
When I was Two
I was nearly new''', ['i', 'was', 'three', 'near']))

assert popularWords('When I was One I had just begun When I was Two I was nearly new',
                        ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
