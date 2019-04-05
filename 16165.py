N, M = map(int, input().split())

all = {}

for i in range(N):
    girlgroup = input()
    Gmemcount = int(input())
    Gmember_list = []
    for i in range(Gmemcount):
        Gmember_list.append(input())
    Gmember_list.sort()
    Gmember_list = [girlgroup] + Gmember_list
    all[girlgroup] = Gmember_list

for i in range(M):
    Q = input()
    Qn = int(input())
    if Qn == 0:
        for i in range(1, len(all[Q])):
            print(all[Q][i])
    elif Qn == 1:
        for v in all.values():
            if Q in v:
                print(v[0])
                break
