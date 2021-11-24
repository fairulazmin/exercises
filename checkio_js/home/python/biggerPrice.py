

def biggerPrice(limit, data):
    data.sort(key= lambda x: x['price'], reverse=True)
    return data[0:limit]

if __name__ == '__main__':
    print('Example:')
    print(biggerPrice(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

assert biggerPrice(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]) == [
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
]

assert biggerPrice(1, [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}
]) == [{"name": "whiteboard", "price": 170}]

print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
