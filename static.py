with open('sequence.txt') as f:
    a = [float(c) for c in f]
need = 0
last = 0
for i in range(len(a)):
    if -3 <= i <= 3:
        need += 1
    else:
        last += 1

need_procent = int(need / len(a) * 100) + 1 #округление
last_procent = int(last / len(a) * 100)

print(f'\x1b[48;5;81m{" " * need_procent}\x1b[0m')
print(f'\x1b[48;5;82m{" " * last_procent}\x1b[0m')
