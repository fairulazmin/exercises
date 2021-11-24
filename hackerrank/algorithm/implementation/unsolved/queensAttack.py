'''
n = board size
k = obstacles
r_q, c_q = queen's position

'''


def queensAttack(n, k, r_q, c_q, obstacles):
    print(f'r_q, c_q = ({r_q}, {c_q})')
    move = [(i, c_q) for i in range(1, n+1) if i != r_q]
    move += [(r_q, j) for j in range(1, n+1) if j != c_q]
    move += [(r_q, c_q)]

    print(move)


print(queensAttack(4, 0, 4, 4, []))                         # 9
# print(queensAttack(4, 0, 3, 2, []))                         # 11
# print(queensAttack(4, 0, 2, 2, []))                         # 11
# print(queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))   # 10
# print(queensAttack(1, 0, 1, 1, []))                         # 0
