'''
Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants
to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive
the immediately following ranking number.
'''


def climbingLeaderboard(scores, alice):
    alice_rank = []
    rank = sorted(set(scores), reverse=True)

    for j in alice:
        if len(rank) == 1:
            if j >= rank[0]:
                alice_rank.append(1)
            else:
                alice_rank.append(2)
        else:
            start = 0
            end = len(rank) - 1
            while end - start != 0:
                mid = int((start + end) / 2)
                if rank[mid] == j:
                    alice_rank.append(mid + 1)
                    break
                elif end - start == 1:
                    if j < rank[end]:
                        alice_rank.append(end + 2)
                        break
                    elif j > rank[start]:
                        alice_rank.append(start + 1)
                        break
                    else:
                        alice_rank.append(end + 1)
                        break

                elif j > rank[mid]:
                    end = mid
                else:
                    start = mid

    return alice_rank


print(climbingLeaderboard([1], [1, 1]))  # 1 1
print(climbingLeaderboard([100, 92, 80, 50, 45, 40, 33, 20, 17, 10], [99, 11, 88, 19]))  # 2 10 3 9
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))  # 6 4 2 1
print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))  # 6 5 4 2 1
