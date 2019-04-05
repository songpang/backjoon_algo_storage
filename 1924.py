mon, date = map(int, input().split())
i = 1
day = 0
month = {1: 31, 2: 28, 3: 31, 
4: 30, 5: 31, 6: 30, 7: 31,
8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
DATE = {0: "SUN", 1: "MON", 2: "TUE", 3:"WED",
4: "THU", 5: "FRI", 6: "SAT"}

while i < mon:
    day += month[i]
    i += 1

day += date
day %= 7

if day in DATE:
    print(DATE[day])