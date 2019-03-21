from typing import List
from curses import wrapper


def main(screen):
    screen.clear()
    print_introduction(screen)
    screen.refresh()

    end = False
    all_inputs: List[str] = []
    while not end:
        last_input = screen.getkey()
        if last_input == 'q':
            end = True
        else:
            all_inputs.append(last_input)
            print_screen(all_inputs, screen)

            screen.refresh()
            screen.move(0, 0)  # move the cursor, s.t. it always stays at the top


def print_screen(all_inputs, screen):
    print_introduction(screen)
    print_last_inputs(all_inputs, screen)


def print_introduction(screen):
    screen.addstr(1, 1, 'Do you think you can type randomly? Let\'s find out!\n Type the Left/Right arrow key '
                        'as randomly as you can. After a few key presses, I\'ll start to guess your next move.')


def print_last_inputs(last_inputs: List[str], screen):
    number_of_printed_inputs = 5 if len(last_inputs) >= 5 else len(last_inputs)
    start_y = 6
    for i in range(number_of_printed_inputs):
        screen.addstr(start_y + i, 1, f'{i+1}. Your input was: {last_inputs[-(i+1)]}')


wrapper(main)
