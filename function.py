def print_line(offset):
    print(f'{" " * offset}\x1b[48;5;7m{" " * 5}\x1b[0m')

for y in range(11, 0, -1):
    print_line(y*3)

    
