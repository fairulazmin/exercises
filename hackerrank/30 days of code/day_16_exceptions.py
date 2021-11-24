input = ['3', 'za', '28374', '12xf']

for i in input:
    try:
        print(int(i))
    except:
        print("Bad String")
