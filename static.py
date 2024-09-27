with open('sequence.txt') as f:
    a = [float(c) for c in f]
nado = 0
ost = 0
for i in range(len(a)):
    if -3 <= i <= 3:
        nado += 1
    else:
        ost += 1

nado_pro = int(nado / len(a) * 100) + 1 #округление
ost_pro = int(ost / len(a) * 100)

print(f'\x1b[48;5;81m{' ' * nado_pro}\x1b[0m')
print(f'\x1b[48;5;82m{' ' * ost_pro}\x1b[0m')
