class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
            return
        return n**p


myCalculator = Calculator()
T = ['3 5', '2 4', '-1 -2', '-1 3']
for i in T:
    n, p = map(int, i.split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
