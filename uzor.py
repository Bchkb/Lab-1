import time

offset = 12
line = 4

WHITE = 7
YELLOW = 3
BLUE = 4
colors = [WHITE,  YELLOW, BLUE]

def print_line(offset, long, color):
    return f'{offset * ' '}\x1b[48;5;{color}m{' ' * long}\x1b[{offset//2 * ' '}C\x1b[0m'
print(print_line(offset, line, WHITE) + print_line(offset, line, WHITE))
print(print_line(offset - 4, line, WHITE) + print_line(offset - 4, line, WHITE))

# while True:
#     for color in colors:
        # print(f'{offset * 8}\x1b[48;5;{color}m{line * 8}\x1b[0m{offset * 12}\x1b[48;5;{color}m{line * 8}\x1b[0m')
        # print(f'{offset * 6}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m')
        # print(f'{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m')
        # print(f'{offset * 2}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 12}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 0}\x1b[48;5;{color}m{line * 4}\x1b[0m\x1b[0m{offset * 12}\x1b[48;5;{color}m{line * 4}\x1b[0m')
        # print(f'{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m')
        # print(f'{offset * 6}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m')
        # print(f'{offset * 8}\x1b[48;5;{color}m{line * 8}\x1b[0m{offset * 12}\x1b[48;5;{color}m{line * 8}\x1b[0m')
        # for i in range(7):
        #     print(print_line(offset, line, color) + print_line(offset, line, color))
        #     if i <= 3:
        #         offset -= 4
        #     if i > 3:
        #         offset += 4



        # time.sleep(1)
        # print('\x1b[8A')
        