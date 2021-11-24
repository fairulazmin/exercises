def acmTeam(topic):
    size = len(topic)
    combi = [bin(int(topic[i], 2) | int(j, 2))[2:] for i in range(size) for j in topic[i + 1:]]
    narrow = [i.count('1') for i in combi]
    return [max(narrow), narrow.count(max(narrow))]


print(acmTeam(['10101', '11110', '00010']))             # 5 1
print(acmTeam(['10101', '11100', '11010', '00101']))    # 5 2

'''
    size = len(topic)
    size_subject = len(topic[0])
    combi = [[topic[i], j] for i in range(size) for j in topic[i + 1:]]
    max_subject = 0
    max_team = 0
    for i in combi:
        count = 0
        for j in range(size_subject):
            if i[0][j] == '1' or i[1][j] == '1':
                count += 1
        if count > max_subject:
            max_subject = count
            max_team = 1
        elif count == max_subject:
            max_team += 1
    return [max_subject, max_team]
'''
