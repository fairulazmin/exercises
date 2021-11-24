

def secondIndex(text, symbol):
    try:
        return text.index(symbol, text.index(symbol) + 1)
    except:
        return 'undefined'

if __name__ == '__main__':
    print('Example')
    print(secondIndex("sims", "s"))

# These "asserts" are used for self-checking and not for an auto-testing
assert secondIndex("sims", "s") == 3
assert secondIndex("find the river", "e") == 12
assert secondIndex("hi", " ") == 'undefined'
assert secondIndex("hi mayor", " ") == 'undefined'
assert secondIndex("hi mr Mayor", " ") == 5
print("You are awesome! All tests are done! Go Check it!")
