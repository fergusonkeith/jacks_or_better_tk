from tkinter import *
import random
from collections import Counter
import locale
import re
locale.setlocale(locale.LC_ALL, '')

deck_of_cards = {0: [2, 'Heart Two'], 1: [3, 'Heart Three'], 2: [4, 'Heart Four'], 3: [5, 'Heart Five'],
                 4: [6,'Heart Six'], 5: [7, 'Heart Seven'], 6: [8, 'Heart Eight'], 7: [9, 'Heart Nine'],
                 8: [10, 'Heart Ten'], 9: [11, 'Heart Jack'], 10: [12, 'Heart Queen'], 11: [13, 'Heart King'],
                 12: [14, 'Heart Ace'], 13: [2, 'Spade Two'], 14: [3, 'Spade Three'], 15: [4, 'Spade Four'],
                 16: [5, 'Spade Five'], 17: [6, 'Spade Six'], 18: [7, 'Spade Seven'], 19: [8, 'Spade Eight'],
                 20: [9, 'Spade Nine'], 21: [10, 'Spade Ten'], 22: [11, 'Spade Jack'], 23: [12, 'Spade Queen'],
                 24: [13, 'Spade King'], 25: [14, 'Spade Ace'], 26: [2, 'Clover Two'], 27: [3, 'Clover Three'],
                 28: [4, 'Clover Four'], 29: [5, 'Clover Five'], 30: [6, 'Clover Six'], 31: [7, 'Clover Seven'],
                 32: [8, 'Clover Eight'], 33: [9, 'Clover Nine'], 34: [10, 'Clover Ten'], 35: [11, 'Clover Jack'],
                 36: [12, 'Clover Queen'], 37: [13, 'Clover King'], 38: [14, 'Clover Ace'], 39: [2, 'Diamond Two'],
                 40: [3, 'Diamond Three'], 41: [4, 'Diamond Four'], 42: [5, 'Diamond Five'], 43: [6, 'Diamond Six'],
                 44: [7, 'Diamond Seven'], 45: [8, 'Diamond Eight'], 46: [9, 'Diamond Nine'], 47: [10, 'Diamond Ten'],
                 48: [11, 'Diamond Jack'], 49: [12, 'Diamond Queen'], 50: [13, 'Diamond King'], 51: [14, 'Diamond Ace']}


players_second_hand = ['', '', '', '', '']
card0_click_count = 0
card1_click_count = 0
card2_click_count = 0
card3_click_count = 0
card4_click_count = 0
bank_account = float(100)
bet_amount = 0
history_royal_flush_wins = 0
history_straight_flush_wins = 0
history_four_of_a_kind_wins = 0
history_full_house_wins = 0
history_flush_wins = 0
history_straight_wins = 0
history_three_of_a_kind_wins = 0
history_two_pairs_wins = 0
history_jacks_or_better_wins = 0
history_lost = 0
games_played_total = 0
percent_winning_hands = float(0)

root = Tk()
root.title('JACKS OR BETTER')

def find_royal(players_second_hand):
    '''checking for a total card value of 60'''
    royal_card_total = 0
    for _ in players_second_hand:
        royal_card_total += _[0]
        #print(royal_card_total)
    if royal_card_total == 60:
        return True
    else:
        return False

def find_flush(players_second_hand):
    diamond_suit_found_count = 0
    heart_suit_found_count = 0
    spade_suit_found_count = 0
    clover_suit_found_count = 0

    for _ in players_second_hand:
        if bool(re.findall(r'Diamond', _[1])) == True:
            diamond_suit_found_count += 1

    for _ in players_second_hand:
        if bool(re.findall(r'Heart', _[1])) == True:
            heart_suit_found_count += 1

    for _ in players_second_hand:
        if bool(re.findall(r'Spade', _[1])) == True:
            spade_suit_found_count += 1

    for _ in players_second_hand:
        if bool(re.findall(r'Clover', _[1])) == True:
            clover_suit_found_count += 1

    if diamond_suit_found_count == 5 or heart_suit_found_count == 5 or spade_suit_found_count == 5 or \
            clover_suit_found_count == 5:
        return True
    else:
        return False


def find_straight(players_second_hand):
    if (players_second_hand[0][0] + 1) == players_second_hand[1][0] and (players_second_hand[1][0] + 1) == \
            players_second_hand[2][0] and (players_second_hand[2][0] + 1) == players_second_hand[3][0] and \
            (players_second_hand[3][0] + 1) == players_second_hand[4][0]:
        return True
    elif (players_second_hand[0][0] + 1) == players_second_hand[1][0] and (players_second_hand[1][0] + 1) == \
            players_second_hand[2][0] and (players_second_hand[2][0] + 1) == players_second_hand[3][0] and \
            (players_second_hand[0][0] + 12) == players_second_hand[4][0]:
        return True
    else:
        return False

def find_four_of_a_kind(players_second_hand):
    card_values = []
    for _ in players_second_hand:
        card_values.append(_[0])
    results = Counter(card_values)
    #print(results)
    for key, value in results.items():
        if value == 4:
            #print('found four of a kind')
            return True
    return False

def find_three_of_a_kind(players_second_hand):
    card_values = []
    for _ in players_second_hand:
        card_values.append(_[0])
    results = Counter(card_values)
    # print(results)
    for key, value in results.items():
        if value == 3:
            # print('found three of a kind')
            return True
    return False

def find_two_pairs(players_second_hand):
    card_values = []
    pair_count = 0
    for _ in players_second_hand:
        card_values.append(_[0])
    results = Counter(card_values)
    # print(results)
    for key, value in results.items():
        if value == 2:
            pair_count += 1
    if pair_count == 2:
        return True
    else:
        return False

def find_two_of_a_kind(players_second_hand):
    card_values = []
    for _ in players_second_hand:
        card_values.append(_[0])
    results = Counter(card_values)
    #print(results)
    for key, value in results.items():
        if value == 2:
            # print('found two of a kind')
            return True
    return False

def find_two_jacks_or_better(players_second_hand):
    card_values = []
    for _ in players_second_hand:
        card_values.append(_[0])
    results = Counter(card_values)
    #print(results)
    for key, value in results.items():
        if key >= 11 and value == 2:
            #print('found jacks or better')
            return True
    return False

def find_bankrupt():
    if bank_account < 1.25:
        r3c0_new_game.config(state=DISABLED)
        r0c2_bet_amount.config(state=NORMAL)
        r3c2_winner.config(text='Game Over')

def find_winner():
    global history_royal_flush_wins
    global history_straight_flush_wins
    global history_four_of_a_kind_wins
    global history_full_house_wins
    global history_flush_wins
    global history_straight_wins
    global history_three_of_a_kind_wins
    global history_two_pairs_wins
    global history_jacks_or_better_wins
    global history_lost
    global games_played_total
    #players_second_hand = [[12, 'Diamond Queen'], [11, 'Diamond Jack'], [10, 'Diamond Ten'], [13, 'Diamond King'], [14, 'Diamond Ace']]
    #players_second_hand = [[2, 'Spade Two'], [2, 'Diamond Two'], [2, 'Clover Two'], [5, 'Heart Five'], [2, 'Heart Two']]
    #players_second_hand = [[2, 'Spade Two'], [2, 'Diamond Two'], [6, 'Clover Six'], [6, 'Heart Six'], [2, 'Heart Two']]
    #players_second_hand = [[4, 'Heart Four'], [3, 'Heart Three'], [2, 'Heart Two'], [5, 'Heart Five'], [6, 'Heart Six']]
    #players_second_hand = [[4, 'Heart Four'], [3, 'Heart Three'], [2, 'Heart Two'], [5, 'Heart Five'], [9, 'Heart Nine']]
    #players_second_hand = [[4, 'Heart Four'], [3, 'Heart Three'], [2, 'Heart Two'], [5, 'Heart Five'], [6, 'Spade Six']]
    #players_second_hand = [[2, 'Spade Two'], [2, 'Diamond Two'], [7, 'Clover Seven'], [6, 'Heart Six'], [7, 'Heart Seven']]
    #players_second_hand = [[2, 'Spade Two'], [11, 'Diamond Jack'], [7, 'Clover Seven'], [6, 'Heart Six'], [11, 'Heart Jack']]
    global bank_account
    players_second_hand.sort()
    check_found_royal = find_royal(players_second_hand)
    check_found_straight = find_straight(players_second_hand)
    check_found_flush = find_flush(players_second_hand)
    check_found_four_of_a_kind = find_four_of_a_kind(players_second_hand)
    check_found_three_of_a_kind = find_three_of_a_kind(players_second_hand)
    check_found_two_of_a_kind = find_two_of_a_kind(players_second_hand)
    check_found_two_pairs = find_two_pairs(players_second_hand)
    check_found_two_jacks_or_better = find_two_jacks_or_better(players_second_hand)

    while True:
        if check_found_royal == True and check_found_flush == True:
            r3c2_winner.config(text='Royal Flush')
            bank_account = (bet_amount * 250) + bank_account
            r0c4_bank_account.config(text=locale.currency((bank_account), grouping=True))
            r3c3_win_amount.config(text='Won ' + str(locale.currency(bet_amount * 250, grouping=True)))
            history_royal_flush_wins += 1
            r5c1_royal_win_history.config(text=history_royal_flush_wins)
            break
        elif check_found_straight == True and check_found_flush == True:
            r3c2_winner.config(text='Straight Flush')
            bank_account = (bet_amount * 50) + bank_account
            r0c4_bank_account.config(text=locale.currency((bank_account), grouping=True))
            r3c3_win_amount.config(text='Won ' + str(locale.currency(bet_amount * 50, grouping=True)))
            history_straight_flush_wins += 1
            r5c4_straight_flush_win_history.config(text=history_straight_flush_wins)
            break
        elif check_found_four_of_a_kind == True:
            r3c2_winner.config(text='Four Of A Kind')
            bank_account = (bet_amount * 25) + bank_account
            r0c4_bank_account.config(text=locale.currency((bank_account), grouping=True))
            r3c3_win_amount.config(text='Won ' + str(locale.currency(bet_amount * 25, grouping=True)))
            history_four_of_a_kind_wins += 1
            r6c1_four_of_a_kind_win_history.config(text=history_four_of_a_kind_wins)
            break
        elif check_found_three_of_a_kind == True and check_found_two_of_a_kind == True:
            r3c2_winner.config(text='Full House')
            bank_account = (bet_amount * 9) + bank_account
            r0c4_bank_account.config(text=locale.currency((bank_account), grouping=True))
            r3c3_win_amount.config(text='Won ' + str(locale.currency(bet_amount * 9, grouping=True)))
            history_full_house_wins += 1
            r6c4_full_house_win_history.config(text=history_full_house_wins)
            break
        elif check_found_flush == True:
            r3c2_winner.config(text='Flush')
            bank_account = (bet_amount * 6) + bank_account
            r0c4_bank_account.config(text=locale.currency((bank_account), grouping=True))
            r3c3_win_amount.config(text='Won ' + str(locale.currency(bet_amount * 6, grouping=True)))
            history_flush_wins += 1
            r7c1_flush_win_history.config(text=history_flush_wins)
            break
        elif check_found_straight == True:
            r3c2_winner.config(text='Straight')
            bank_account = (bet_amount * 4) + bank_account
            r0c4_bank_account.config(text=locale.currency((bank_account), grouping=True))
            r3c3_win_amount.config(text='Won ' + str(locale.currency(bet_amount * 4, grouping=True)))
            history_straight_wins += 1
            r7c4_straight_win_history.config(text=history_straight_wins)
            break
        elif check_found_three_of_a_kind == True:
            r3c2_winner.config(text='Three Of A Kind')
            bank_account = (bet_amount * 3) + bank_account
            r0c4_bank_account.config(text=locale.currency((bank_account), grouping=True))
            r3c3_win_amount.config(text='Won ' + str(locale.currency(bet_amount * 3, grouping=True)))
            history_three_of_a_kind_wins += 1
            r8c1_three_of_a_kind_win_history.config(text=history_three_of_a_kind_wins)
            break
        elif check_found_two_pairs == True:
            r3c2_winner.config(text='Two Pairs')
            bank_account = (bet_amount * 2) + bank_account
            r0c4_bank_account.config(text=locale.currency((bank_account), grouping=True))
            r3c3_win_amount.config(text='Won ' + str(locale.currency(bet_amount * 2, grouping=True)))
            history_two_pairs_wins += 1
            r8c4_two_pair_win_history.config(text=history_two_pairs_wins)
            break
        elif check_found_two_jacks_or_better == True:
            r3c2_winner.config(text='Jacks Or Better')
            bank_account = (bet_amount * 1) + bank_account
            r0c4_bank_account.config(text=locale.currency((bank_account), grouping=True))
            r3c3_win_amount.config(text='Won ' + str(locale.currency(bet_amount * 1, grouping=True)))
            history_jacks_or_better_wins += 1
            r9c1_jacks_or_better_win_history.config(text=history_jacks_or_better_wins)
            break
        else:
            r3c2_winner.config(text='Loser')
            history_lost += 1
            r9c4_lost_history.config(text=history_lost)
            break
    games_played_total += 1
    r10c1_games_played_total.config(text=games_played_total)
    r0c2_bet_amount.config(state=NORMAL)
    find_bankrupt()

def hold_card0():
    global players_second_hand
    global card0_click_count
    '''click count even = hold odd = changed mind don't hold'''
    if card0_click_count % 2 == 0:
        r1c0_card0.config(background='cyan')
        r2c0_hold.config(text='Held Card 0')
        players_second_hand[0] = players_first_hand[0]
        #print(players_second_hand)
    else:
        r1c0_card0.config(background=root.cget("background"))
        r2c0_hold.config(text='Hold Card 0')
        players_second_hand[0] = ''
        #print(players_second_hand)
    card0_click_count += 1

def hold_card1():
    global players_second_hand
    global card1_click_count
    '''click count even = hold odd = changed mind don't hold'''
    if card1_click_count % 2 == 0:
        r1c1_card1.config(background='cyan')
        r2c1_hold.config(text='Held Card 1')
        players_second_hand[1] = players_first_hand[1]
        #print(players_second_hand)
    else:
        r1c1_card1.config(background=root.cget("background"))
        r2c1_hold.config(text='Hold Card 1')
        players_second_hand[1] = ''
        #print(players_second_hand)
    card1_click_count += 1

def hold_card2():
    global players_second_hand
    global card2_click_count
    '''click count even = hold odd = changed mind don't hold'''
    if card2_click_count % 2 == 0:
        r1c2_card2.config(background='cyan')
        r2c2_hold.config(text='Held Card 2')
        players_second_hand[2] = players_first_hand[2]
        #print(players_second_hand)
    else:
        r1c2_card2.config(background=root.cget("background"))
        r2c2_hold.config(text='Hold Card 2')
        players_second_hand[2] = ''
        #print(players_second_hand)
    card2_click_count += 1

def hold_card3():
    global players_second_hand
    global card3_click_count
    '''click count even = hold odd = changed mind don't hold'''
    if card3_click_count % 2 == 0:
        r1c3_card3.config(background='cyan')
        r2c3_hold.config(text='Held Card 3')
        players_second_hand[3] = players_first_hand[3]
        #print(players_second_hand)
    else:
        r1c3_card3.config(background=root.cget("background"))
        r2c3_hold.config(text='Hold Card 3')
        players_second_hand[3] = ''
        #print(players_second_hand)
    card3_click_count += 1

def hold_card4():
    global players_second_hand
    global card4_click_count
    '''click count even = hold odd = changed mind don't hold'''
    if card4_click_count % 2 == 0:
        r1c4_card4.config(background='cyan')
        r2c4_hold.config(text='Held Card 4')
        players_second_hand[4] = players_first_hand[4]
        #print(players_second_hand)
    else:
        r1c4_card4.config(background=root.cget("background"))
        r2c4_hold.config(text='Hold Card 4')
        players_second_hand[4] = ''
        #print(players_second_hand)
    card4_click_count += 1

def draw():
    global bank_account
    global pick_amount_to_bet
    players_second_hand_card_count = 0


    #print(players_second_hand)
    #print(players_first_hand)

    for _ in players_second_hand:
        if _ == '':
            while True:
                get_card = pick_a_random_card()
                if list(deck_of_cards.values())[get_card] not in players_first_hand \
                        and list(deck_of_cards.values())[get_card] not in players_second_hand:
                    players_second_hand[players_second_hand_card_count] = list(deck_of_cards.values())[get_card]
                    break
        players_second_hand_card_count += 1

    r1c0_card0.config(text=players_second_hand[0][1])
    r1c1_card1.config(text=players_second_hand[1][1])
    r1c2_card2.config(text=players_second_hand[2][1])
    r1c3_card3.config(text=players_second_hand[3][1])
    r1c4_card4.config(text=players_second_hand[4][1])
    r2c0_hold.config(state=DISABLED)
    r2c1_hold.config(state=DISABLED)
    r2c2_hold.config(state=DISABLED)
    r2c3_hold.config(state=DISABLED)
    r2c4_hold.config(state=DISABLED)
    r3c4_draw.config(state=DISABLED)
    r3c0_new_game.config(state=NORMAL)

    find_winner()

    if bank_account < 25 and bank_account >= 5:
        pick_amount_to_bet = StringVar(root)
        pick_amount_to_bet.set(locale.currency(5, grouping=True))
        r0c2_bet_amount = OptionMenu(root, pick_amount_to_bet, locale.currency(1.25, grouping=True),
                                     locale.currency(2.5, grouping=True), locale.currency(5, grouping=True))
        r0c2_bet_amount.grid(row=0, column=2, padx=20, pady=20, sticky=W + E)
        r0c2_bet_amount.config(state=NORMAL)
    elif bank_account < 5 and bank_account >= 2.5:
        pick_amount_to_bet = StringVar(root)
        pick_amount_to_bet.set(locale.currency(2.5, grouping=True))
        r0c2_bet_amount = OptionMenu(root, pick_amount_to_bet, locale.currency(1.25, grouping=True),
                                     locale.currency(2.5, grouping=True))
        r0c2_bet_amount.grid(row=0, column=2, padx=20, pady=20, sticky=W + E)
        r0c2_bet_amount.config(state=NORMAL)
    elif bank_account < 2.5 and bank_account >= 1.25:
        pick_amount_to_bet = StringVar(root)
        pick_amount_to_bet.set(locale.currency(1.25, grouping=True))
        r0c2_bet_amount = OptionMenu(root, pick_amount_to_bet, locale.currency(1.25, grouping=True))
        r0c2_bet_amount.grid(row=0, column=2, padx=20, pady=20, sticky=W + E)
        r0c2_bet_amount.config(state=NORMAL)



    #print(players_second_hand)

def pick_a_random_card():
    return random.randint(0, 51)

def new_game():
    global players_first_hand
    global card0_click_count
    global card1_click_count
    global card2_click_count
    global card3_click_count
    global card4_click_count
    global bank_account
    global players_second_hand
    global games_played_total
    global bet_amount
    global pick_amount_to_bet
    #print('players first hand after global')
    #print(players_first_hand)
    if pick_amount_to_bet.get() == '$1.25':
        bet_amount = float(1.25)
    elif pick_amount_to_bet.get() == '$2.50':
        bet_amount = float(2.5)
    elif pick_amount_to_bet.get() == '$5.00':
        bet_amount = float(5)
    elif pick_amount_to_bet.get() == '$25.00':
        bet_amount = float(25)
    #bet_amount = float(pick_amount_to_bet.get())
    #print(bet_amount)
    card0_click_count = 0
    card1_click_count = 0
    card2_click_count = 0
    card3_click_count = 0
    card4_click_count = 0
    players_second_hand = ['', '', '', '', '']
    #print('players second hand after new game')
    #print(players_second_hand)

    bank_account = bank_account - bet_amount

    cards_in_hand = 0
    players_first_hand = []

    while cards_in_hand < 5:
            get_card = pick_a_random_card()
            if list(deck_of_cards.values())[get_card] not in players_first_hand:
               players_first_hand.append(list(deck_of_cards.values())[get_card])
               cards_in_hand += 1
    #print(players_first_hand[0][0])
    #print(players_first_hand[0][1])
    r0c4_bank_account.config(text=locale.currency((bank_account), grouping=True))
    r1c0_card0.config(text=players_first_hand[0][1])
    r1c1_card1.config(text=players_first_hand[1][1])
    r1c2_card2.config(text=players_first_hand[2][1])
    r1c3_card3.config(text=players_first_hand[3][1])
    r1c0_card0.config(background=root.cget("background"))
    r1c1_card1.config(background=root.cget("background"))
    r1c2_card2.config(background=root.cget("background"))
    r1c3_card3.config(background=root.cget("background"))
    r1c4_card4.config(background=root.cget("background"))
    r2c0_hold.config(text='Hold Card 0')
    r2c1_hold.config(text='Hold Card 1')
    r2c2_hold.config(text='Hold Card 2')
    r2c3_hold.config(text='Hold Card 3')
    r2c4_hold.config(text='Hold Card 4')
    r1c4_card4.config(text=players_first_hand[4][1])
    r3c2_winner.config(text='')
    r3c3_win_amount.config(text='')
    #print(players_first_hand[0])
    r2c0_hold.config(state=NORMAL)
    r2c1_hold.config(state=NORMAL)
    r2c2_hold.config(state=NORMAL)
    r2c3_hold.config(state=NORMAL)
    r2c4_hold.config(state=NORMAL)
    r3c0_new_game.config(state=DISABLED)
    r3c4_draw.config(state=NORMAL)
    r0c2_bet_amount.config(state=DISABLED)
    #print('this is players first hand ' + str(players_first_hand))

'''row 0'''
r0c0_game_name = Label(root, text="Jacks Or Better")
r0c1_bet_amount = Label(root, text='Bet Amount')
r0c2_bet_amount = Label(root, text=locale.currency(bet_amount, grouping=True))
pick_amount_to_bet = StringVar(root)
pick_amount_to_bet.set(locale.currency(1.25, grouping=True))
r0c2_bet_amount = OptionMenu(root, pick_amount_to_bet, locale.currency(1.25, grouping=True), locale.currency(2.5, \
    grouping=True), locale.currency(5, grouping=True), locale.currency(25, grouping=True))

r0c3_bank_account = Label(root, text='Bank Account')
r0c4_bank_account = Label(root, text=locale.currency(bank_account, grouping=True))

'''row 1'''
r1c0_card0 = Label(root, text='Card 0')
r1c1_card1 = Label(root, text='Card 1')
r1c2_card2 = Label(root, text='Card 2')
r1c3_card3 = Label(root, text='Card 3')
r1c4_card4 = Label(root, text='Card 4')

'''row 2'''
r2c0_hold = Button(root, text='Hold Card 0', state=DISABLED, command=hold_card0)
r2c1_hold = Button(root, text='Hold Card 1', state=DISABLED, command=hold_card1)
r2c2_hold = Button(root, text='Hold Card 2', state=DISABLED, command=hold_card2)
r2c3_hold = Button(root, text='Hold Card 3', state=DISABLED, command=hold_card3)
r2c4_hold = Button(root, text='Hold Card 4', state=DISABLED, command=hold_card4)

'''row 3'''
r3c0_new_game = Button(root, text='New Game', command=new_game)
r3c2_winner = Label(root, text='')
r3c3_win_amount = Label(root, text='')
r3c4_draw = Button(root, text='Draw', state=DISABLED, command=draw)

'''row 4'''
r4c2_game_history = Label(root, text='Game History')

'''row 5'''
r5c0_royal_history = Label(root, text='Royal Flush')
r5c1_royal_win_history = Label(root, text=history_royal_flush_wins)
r5c3_straight_flush_history = Label(root, text='Straight Flush')
r5c4_straight_flush_win_history = Label(root, text=history_flush_wins)

'''row 6'''
r6c0_four_of_a_kind_history = Label(root, text='Four Of A Kind')
r6c1_four_of_a_kind_win_history = Label(root, text=history_four_of_a_kind_wins)
r6c3_full_house_history = Label(root, text='Full House')
r6c4_full_house_win_history = Label(root, text=history_full_house_wins)

'''row 7'''
r7c0_flush_history = Label(root, text='Flush')
r7c1_flush_win_history = Label(root, text=history_flush_wins)
r7c3_straight_history = Label(root, text='Straight')
r7c4_straight_win_history = Label(root, text=history_straight_wins)

'''row 8'''
r8c0_three_of_a_kind_history = Label(root, text='Three Of A Kind')
r8c1_three_of_a_kind_win_history = Label(root, text=history_three_of_a_kind_wins)
r8c3_two_pair_history = Label(root, text='Two Pairs')
r8c4_two_pair_win_history = Label(root, text=history_two_pairs_wins)

'''row 9'''
r9c0_jacks_or_better_history = Label(root, text='Jacks Or Better')
r9c1_jacks_or_better_win_history = Label(root, text=history_jacks_or_better_wins)
r9c3_lost_history = Label(root, text='Lost')
r9c4_lost_history = Label(root, text=history_lost)

'''row 10'''
r10c0_games_played = Label(root, text='Games Played')
r10c1_games_played_total = Label(root, text=games_played_total)
r10c4_end_game = Button(root, text='End Game', command=root.quit)


'''root layout'''
r0c0_game_name.grid(row=0, column=0, padx=20, pady=20, sticky=W+E)
r0c1_bet_amount.grid(row=0, column=1, padx=20, pady=20, sticky=W+E)
r0c2_bet_amount.grid(row=0, column=2, padx=20, pady=20, sticky=W+E)
r0c3_bank_account.grid(row=0, column=3, padx=20, pady=20, sticky=W+E)
r0c4_bank_account.grid(row=0, column=4, padx=20, pady=20, sticky=W+E)
r1c0_card0.grid(row=1, column=0, padx=20, pady=20, sticky=W+E)
r1c1_card1.grid(row=1, column=1, padx=20, pady=20, sticky=W+E)
r1c2_card2.grid(row=1, column=2, padx=20, pady=20, sticky=W+E)
r1c3_card3.grid(row=1, column=3, padx=20, pady=20, sticky=W+E)
r1c4_card4.grid(row=1, column=4, padx=20, pady=20, sticky=W+E)
r2c0_hold.grid(row=2, column=0, padx=20, pady=20, sticky=W+E)
r2c1_hold.grid(row=2, column=1, padx=20, pady=20, sticky=W+E)
r2c2_hold.grid(row=2, column=2, padx=20, pady=20, sticky=W+E)
r2c3_hold.grid(row=2, column=3, padx=20, pady=20, sticky=W+E)
r2c4_hold.grid(row=2, column=4, padx=20, pady=20, sticky=W+E)
r3c0_new_game.grid(row=3, column=0, padx=20, pady=20, sticky=W+E)
r3c2_winner.grid(row=3, column=2, padx=20, pady=20, sticky=W+E)
r3c3_win_amount.grid(row=3, column=3, padx=20, pady=20, sticky=W+E)
r3c4_draw.grid(row=3, column=4, padx=20, pady=20, sticky=W+E)
r4c2_game_history.grid(row=4, column=2, padx=20, pady=20, sticky=W+E)
r5c0_royal_history.grid(row=5, column=0, padx=20, pady=20, sticky=W+E)
r5c1_royal_win_history.grid(row=5, column=1, padx=20, pady=20, sticky=W+E)
r5c3_straight_flush_history.grid(row=5, column=3, padx=20, pady=20, sticky=W+E)
r5c4_straight_flush_win_history.grid(row=5, column=4, padx=20, pady=20, sticky=W+E)
r6c0_four_of_a_kind_history.grid(row=6, column=0, padx=20, pady=20, sticky=W+E)
r6c1_four_of_a_kind_win_history.grid(row=6, column=1, padx=20, pady=20, sticky=W+E)
r6c3_full_house_history.grid(row=6, column=3, padx=20, pady=20, sticky=W+E)
r6c4_full_house_win_history.grid(row=6, column=4, padx=20, pady=20, sticky=W+E)
r7c0_flush_history.grid(row=7, column=0, padx=20, pady=20, sticky=W+E)
r7c1_flush_win_history.grid(row=7, column=1, padx=20, pady=20, sticky=W+E)
r7c3_straight_history.grid(row=7, column=3, padx=20, pady=20, sticky=W+E)
r7c4_straight_win_history.grid(row=7, column=4, padx=20, pady=20, sticky=W+E)
r8c0_three_of_a_kind_history.grid(row=8, column=0, padx=20, pady=20, sticky=W+E)
r8c1_three_of_a_kind_win_history.grid(row=8, column=1, padx=20, pady=20, sticky=W+E)
r8c3_two_pair_history.grid(row=8, column=3, padx=20, pady=20, sticky=W+E)
r8c4_two_pair_win_history.grid(row=8, column=4, padx=20, pady=20, sticky=W+E)
r9c0_jacks_or_better_history.grid(row=9, column=0, padx=20, pady=20, sticky=W+E)
r9c1_jacks_or_better_win_history.grid(row=9, column=1, padx=20, pady=20, sticky=W+E)
r9c3_lost_history.grid(row=9, column=3, padx=20, pady=20, sticky=W+E)
r9c4_lost_history.grid(row=9, column=4, padx=20, pady=20, sticky=W+E)
r10c0_games_played.grid(row=10, column=0, padx=20, pady=20, sticky=W+E)
r10c1_games_played_total.grid(row=10, column=1, padx=20, pady=20, sticky=W+E)
r10c4_end_game.grid(row=10, column=4, padx=20, pady=20, sticky=W+E)

root.mainloop()