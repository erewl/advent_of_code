import numpy as np
from numpy.core import numeric

# https://adventofcode.com/2021/day/4

def __get_rows(file):
    def transform_str_2_row(row):
        return [{'number': int(r), 'called': False} for r in row.split(" ") if r!=""]

    f = open(file, "r")
    rows = f.read().split("\n")

    numbers = [int(r) for r in rows.pop(0).split(",")]
    no_empty_rows = [transform_str_2_row(row) for row in rows if "".join(row).replace(" ", "") != ""]

    card_count = int(len(no_empty_rows) / 5)
    bingo_cards = [no_empty_rows[i*5 : (i*5)+5] for i in range(0, card_count)]
    return numbers, bingo_cards

def __check_row(row):
    return all(n['called'] for n in row)

def __check_horizontal(card):
    r = range(0,5)
    def __check(card, i):
        if i >= 5: return []
        elif __check_row(card[:][i]): return [(i,j) for j in r]
        else: return __check(card, i+1)
    return __check(card, 0)

def __check_vertical(bingo_card):
    r = range(0,5)
    inverted_card = [ [bingo_card[j][i] for j in r] for i in r]
    def __check(card, i):
        if i >= 5: return []
        elif __check_row(card[:][i]): return [(j, i) for j in r]
        else: return __check(card, i+1)
    return __check(inverted_card, 0)

def __find_called_number(card, called_number):
    def __set_called(place):
        if place['number'] == called_number:
            place['called'] = True
        return place
    new_card = card.copy()
    new_card = [[__set_called(number) for number in row] for row in new_card ]
    return new_card

def __empty(card):
    return len(card) == 0

def __is_bingo(card):
    return (not __empty(__check_horizontal(card))) or (not __empty(__check_vertical(card)))

def part_one(input_file):
    input, bingo_cards = __get_rows(input_file)

    def loop(numbers, cards):
        current_number = numbers.pop(0)
        new_cards = cards.copy()
        new_cards = [__find_called_number(card, current_number) for card in new_cards]

        for card in new_cards:
            if __is_bingo(card):
                return (current_number, card)
        return loop(numbers, new_cards)
            
    number, bingo = loop(input, bingo_cards)
    filtered = [element['number'] for row in bingo for element in row if not element['called']]
    return sum(filtered) * number

def part_two(input_file):
    input, bingo_cards = __get_rows(input_file)

    def loop(numbers, cards):
        current_number = numbers.pop(0)
        new_cards = cards.copy()
        new_cards = [__find_called_number(card, current_number) for card in new_cards]

        for card in new_cards:
            if len(new_cards) <= 1 :
                return (current_number, card)
            if __is_bingo(card):
                new_cards.remove(card)

        return loop(numbers, new_cards)
            
    number, bingo = loop(input, bingo_cards)
    filtered = [element['number'] for row in bingo for element in row if not element['called']]
    return sum(filtered) * number