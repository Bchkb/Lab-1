import time

def print_line(offset_f, long, color, offset_b):
    up = f'{offset_f * " "}\x1b[48;5;{color}m{" " * long}\x1b[{offset_b * " "}\x1b[0m'
    down = f'{offset_b * " "}\x1b[48;5;{color}m{" " * long}\x1b[{offset_f * " "}\x1b[0m'
    return up + down


def circle():
    WHITE = 7
    YELLOW = 3
    BLUE = 4
    colors = [WHITE,  YELLOW, BLUE]

    while True:
        for color in colors:
            offset_f = 12
            offset_b = 0
            offset_f_down = 12
            line = 4
            for i in range(7):
                print(print_line(offset_f, line, color, offset_b) + print_line(offset_f_down, line, color, offset_b))
                if i < 3:
                    offset_f_down -= 4
                    offset_f -= 2
                    offset_b += 4
                if i >= 3:
                    offset_f_down += 4
                    offset_f += 2
                    offset_b -= 4

            time.sleep(1)
            print('\x1b[9A')
            print(f'\x1b[{offset_f * 3}C')


if __name__ == '__main__':
    circle()
        