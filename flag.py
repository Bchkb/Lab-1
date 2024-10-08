RED = 1
WHITE = 7

def square_print(long, color, offset):
    print(f'{offset * " "}\x1b[48;5;{color}m{long * " "}\x1b[0m')

def plus_print(color_offset, long, color, offset):
    print(f'\x1b[48;5;{color_offset}m{offset * " "}\x1b[48;5;{color}m{long * " "}\x1b[0m')

for i in range(8):
    square_print(25, RED, 0)

print('\x1b[9A')
print('\x1b[25D')

for i in range(8):
    if i == 0 or i == 1 or i == 5 or i == 6:
        plus_print(RED, 6, WHITE, 9)
    if i == 3 or i == 4:
        plus_print(RED, 18, WHITE, 3)

print('\x1b[1B')


