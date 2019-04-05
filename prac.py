a = input().strip().split(' '); b = a[0]
Coutput = ''
BigWC = 0
DigitWC = 0

# print(len(b))
for i in range(len(b)):
    if b[i].isupper() == True:
        Coutput.append(b[i])
        BigWC += 1
        if b[i+1].islower == True:
            Coutput.append(b[i+1])
    for v in range(len(b)):
        