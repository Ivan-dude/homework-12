numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = int(input()) #3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
pari = []

for i in range(1, n):
    for j in range(i+1, n):
        if n % (i+j) == 0:
            b = i, j
            pari.append(b)
for k in pari:
    print(str(k[0]) + str(k[1]), end='')


