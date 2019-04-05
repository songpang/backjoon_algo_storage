import re
# s = 'HO21'
a = input().strip().split(' '); s = a[0]

i = re.findall('\D+', s)[0]; i += ' '
j = re.findall('\d+', s)[0]; j += ''
Coutput =''
WC = 0
k = 0
x = 0
for v in range(len(i)):
    if i[v].isupper() == True:
        WC += 1

if len(j) != WC:
    print('error')
else:
    while k < len(i) - 1:
        Coutput += i[k]
        if i[k+1].islower() == True:
            Coutput += i[k+1]
            k += 1
        k += 1
        if x > len(j):
            break
        else:
            if j[x] != '1':
                Coutput += j[x]
                x += 1
            else: x += 1
    print(Coutput)