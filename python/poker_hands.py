#!/usr/bin/env python3

"""
Usage:
    poker_hands [-r randomize] [-s sample] [-p num_players]

Options:
    -r randomize    flag to generate two random hands of poker [default: n]
    -s sample       number of hands to show in terminal [default: 1000]
    -p num_players  if the randomize option is turned on, how many players to deal in [default: 2]

Description:
    Project Euler Problem 54: Download text file of poker hands and determine which player wins.
"""
from docopt import docopt
from urllib import request
import numpy as np


def get_hands(num_hands=None):
    url = "https://projecteuler.net/project/resources/p054_poker.txt"
    response = request.urlopen(url)
    data = response.read().decode("utf-8").split("\n")
    if num_hands is not None:
        return data[:num_hands]
    else:
        return data


def hand_value(cards):
    ordered_value_dict = {"2": 0, "3": 1, "4": 2,
                          "5": 3, "6": 4, "7": 5, "8": 6,
                          "9": 7, "T": 8, "J": 9, "Q": 10,
                          "K": 11, "A": 12}
    name_value_dict = {0: "Two", 1: "Three", 2: "Four",
                       3: "Five", 4: "Sixe", 5: "Seven", 6: "Eight",
                       7: "Nine", 8: "Ten", 9: "Jack", 10: "Queen",
                      11: "King", 12: "Ace"}
    suit_dict = {"H": "Hearts", "D": "Diamonds", "S": "Spades", "C": "Clubs"}
    vals = [ordered_value_dict[card[0]] for card in cards]
    vals.sort(reverse=True)
    suits = [card[-1] for card in cards]
    val_set, val_count = np.unique(vals, return_counts=True)
    max_val = max(vals)
    if val_set.size == 5 and ((max_val - min(vals)) == 4):
        straight_flag = True
    else:
        straight_flag = False
    if len(set(suits)) == 1:
        flush_flag = True
    else:
        flush_flag = False

    if straight_flag and flush_flag:
        if max_val == 12:
            hand_value = (10, "Royal Flush")
        else:
            dec_val = (9, max_val)
            high_card = name_value_dict[max_val]
            if max_val == 4:
                high_card = "Six"
            hand_value = (dec_val, "Straight Flush High Card " + high_card)
    elif val_set.size == 2:
        if np.max(val_count) == 4:
            four_kind_val = val_set[np.where(val_count == 4)[0]][0]
            four_kind_card = name_value_dict[four_kind_val]
            other_val = val_set[np.where(val_count == 1)[0]]
            dec_val = (8, four_kind_val, other_val)
            hand_value = (dec_val, "Four " + four_kind_card + "s")
        else:
            full_house_val = val_set[np.where(val_count == 3)[0]][0]
            full_card = name_value_dict[full_house_val]
            under_val = val_set[np.where(val_count == 2)[0]][0]
            under_card = name_value_dict[under_val]
            dec_val = (7, full_house_val, under_val)
            hand_value = (dec_val, "Full House, " + full_card + "s over " + under_card + "s")
    elif flush_flag and not straight_flag:
        suit = suit_dict[list(set(suits))[0]]
        dec_val = (6, *vals)
        high_card = name_value_dict[max_val]
        if max_val == 4:
            high_card = "Six"
        hand_value = (dec_val, suit + " Flush High Card " + high_card)
    elif straight_flag and not flush_flag:
        dec_val = (5, max_val)
        high_card = name_value_dict[max_val]
        if max_val == 4:
            high_card = "Six"
        hand_value = (dec_val, "Straight High Card " + high_card)
    elif val_set.size == 3:
        if np.max(val_count) == 3:
            three_kind_val = val_set[np.where(val_count == 3)[0]][0]
            three_kind_card = name_value_dict[three_kind_val]
            other_vals = list(val_set[np.where(val_count == 1)[0]])
            other_vals.sort(reverse=True)
            dec_val = (4, three_kind_val, *other_vals)
            hand_value = (dec_val, "Three " + three_kind_card + "s")
        else:
            pair_vals = val_set[np.where(val_count == 2)[0]]
            pair_card1 = name_value_dict[np.max(pair_vals)]
            pair_card2 = name_value_dict[np.min(pair_vals)]
            other_val = val_set[np.where(val_count == 1)[0]][0]
            pair_list = list(pair_vals)
            pair_list.sort(reverse=True)
            dec_val = (3, *pair_list, other_val)
            hand_value = (dec_val, "Two Pair, " + pair_card1 + "s and " + pair_card2 + "s")
    elif val_set.size == 4:
        pair_val = val_set[np.where(val_count == 2)[0]][0]
        pair_card = name_value_dict[pair_val]
        other_vals = list(val_set[np.where(val_count == 1)[0]])
        other_vals.sort(reverse=True)
        dec_val = (2, pair_val, *other_vals)
        hand_value = (dec_val, "Pair of " + pair_card + "s")
    else:
        dec_val = (1, *vals)
        high_card = name_value_dict[max_val]
        if max_val == 4:
            high_card = "Six"
        hand_value = (dec_val, "High Card " + high_card)
    return hand_value


def compare_hands(val1, val2):
    stop_flag = False
    ind = 0
    while stop_flag is False:
        if ind < max(len(val1), len(val2)):
            if val1[ind] > val2[ind]:
                stop_flag = True
                return True
            elif val1[ind] < val2[ind]:
                stop_flag = True
                return False
            else:
                ind += 1
        else:
            print("Hands are equal!")
            stop_flag = True

def main():
    args = docopt(__doc__)
    sample = int(args["-s"])
    r_flag = args["-r"].lower() != "n"

    if not r_flag:
        p1_wins = 0
        p2_wins = 0
        poker_hands = get_hands(num_hands=sample)
        for hand in poker_hands:
            p1_hand = hand.split()[:5]
            p2_hand = hand.split()[5:]
            p1_val = hand_value(p1_hand)
            p2_val = hand_value(p2_hand)
            if p1_val[0][0] == p2_val[0][0] and p1_val[0][0] == 4:
                print(p1_hand, p1_val)
                print(p2_hand, p2_val)
                print(compare_hands(p1_val[0], p2_val[0]))
            if compare_hands(p1_val[0], p2_val[0]):
                p1_wins += 1
            else:
                p2_wins += 1
        print(f"P1 wins: {p1_wins} vs. P2 wins: {p2_wins}")

if __name__ == "__main__":
    main()


