import curses
from collections import namedtuple
from typing import List, Tuple
from curses import wrapper

from function import *

entry: Tuple[chr, chr] = namedtuple('entry', ['input', 'guess'])


def main(screen):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    screen.clear()
    print_introduction(screen)
    screen.refresh()

    current_five_grams: dict = init()
    last_prediction: int = None
    end = False
    all_entries: List[entry] = []
    while not end:
        last_input: chr = screen.getkey()
        if last_input == 'q':
            end = True
        else:
            processed_input = process_input(last_input)
            if processed_input != '':
                all_entries.append(entry(process_input(last_input), last_prediction))

                if len(all_entries) > 6:
                    current_five_grams, last_prediction = aaronson(get_all_inputs(all_entries), current_five_grams)
                print_screen(all_entries, screen)

                screen.addstr(12, 1, f'DEBUG: input:   {get_all_inputs(all_entries)}')
                screen.addstr(13, 1, f'DEBUG: guesses: {get_all_guesses(all_entries)}')

                screen.refresh()
                screen.move(0, 0)  # move the cursor, s.t. it always stays at the top


def process_input(last_input: str):
    if last_input == 'KEY_LEFT':
        return '0'
    elif last_input == 'KEY_RIGHT':
        return '1'
    return ''


def get_all_inputs(all_entries: List[entry]):
    all_inputs = ''
    for i_entry in all_entries:
        all_inputs += i_entry.input
    return all_inputs


def get_all_guesses(all_entries: List[entry]):
    all_guesses = ''
    for i_entry in all_entries:
        if i_entry.guess is not None:
            all_guesses += str(i_entry.guess)
        else:
            all_guesses += 'x'
    return all_guesses


def print_screen(all_entries: List[entry], screen) -> None:
    print_introduction(screen)
    if len(all_entries) > 6:
        print_statistics(all_entries, screen)
    print_last_inputs(all_entries, screen)


def print_introduction(screen) -> None:
    screen.addstr(1, 1, 'Do you think you can type randomly? Let\'s find out!\n Type the Left/Right arrow key '
                        'as randomly as you can. After a few key presses, I\'ll start to guess your next move.')


def print_statistics(all_entries: List[entry], screen):
    number_of_guesses = get_number_of_guesses(all_entries)
    number_of_correct_guesses = get_number_of_correct_guesses(all_entries)
    if number_of_guesses > 0:
        percentage_correctly_guessed = (number_of_correct_guesses / number_of_guesses) * 100
        screen.addstr(4, 1, 'I guessed your input %.2f%% times' % percentage_correctly_guessed)


def get_number_of_guesses(all_entries: List[entry]):
    number_of_guesses = 0
    for i_entry in all_entries:
        if i_entry.guess is not None:
            number_of_guesses += 1
    return number_of_guesses


def get_number_of_correct_guesses(all_entries: List[entry]):
    number_of_correct_guesses = 0
    for i_entry in all_entries:
        if int(i_entry.input) == i_entry.guess:
            number_of_correct_guesses += 1
    return number_of_correct_guesses


def print_last_inputs(all_entries: List[entry], screen) -> None:
    number_of_printed_inputs = 5 if len(all_entries) >= 5 else len(all_entries)
    start_y = 6
    for i in range(number_of_printed_inputs):
        printed_entry = all_entries[-(i + 1)]
        color_pair = curses.color_pair(0)
        if printed_entry.guess is not None:
            if int(printed_entry.input) != int(printed_entry.guess):
                color_pair = curses.color_pair(1)
            else:
                color_pair = curses.color_pair(2)
        screen.addstr(start_y + i, 1, f'{i+1}. Your input was: {printed_entry.input} - '
                                      f'My guess was: {printed_entry.guess}   ', color_pair)


if __name__ == '__main__':
    wrapper(main)
