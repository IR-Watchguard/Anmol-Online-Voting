import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# Card Class which gives a basic defination of the card


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return (f'{self.rank} of {self.suit}')

# Deck class responsible to create the whole deck of cards


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_one(self):
        curr_card = self.deck[-1]
        self.deck.pop()
        return curr_card


class Player():
    def __init__(self, name):
        self.name = name
        self.player_hand = []

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.player_hand.extend(cards)
        else:
            self.player_hand.append(cards)

    def remove_card(self):
        return self.player_hand.pop(0)

    def __str__(self):
        return (f'{self.name} has {len(self.player_hand)} cards.')


# def distribute_cards(player1, player2):
#     '''Distribute Cards among the players'''
#     add_whom = 1
#     while card_deck.deck:
#         rand_card_idx = random.randint(0, len(card_deck.deck)-1)
#         if add_whom == 1:
#             player1.add_cards(card_deck.deck[rand_card_idx])
#             add_whom = 2
#         else:
#             player2.add_cards(card_deck.deck[rand_card_idx])
#             add_whom = 1

#         card_deck.deck.pop(rand_card_idx)


card_deck = Deck()
card_deck.shuffle_deck()

player_one = Player('Anmol')
player_two = Player('Bhati')

for i in range(26):
    player_one.add_cards(card_deck.deal_one())
    player_two.add_cards(card_deck.deal_one())


round_count = 0
play_game = True
while play_game:
    round_count += 1
    print(f'Round {round_count}\n')
    if len(player_one.player_hand) == 0:
        print(f'{player_two.name} Wins!! {player_one.name} is out of cards.')
        break
    if len(player_two.player_hand) == 0:
        print(f'{player_one.name} Wins!! {player_two.name} is out of cards.')
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one_cards.extend(player_two_cards)
            player_one.add_cards(player_one_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two_cards.extend(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('You Are At War\n')
            if len(player_one.player_hand) < 5:
                print("Player 1 Can't Proceed!! Player 2 Wins")
                play_game = False
                break
            if len(player_two.player_hand) < 5:
                print("Player 2 Can't Proceed!! Player 1 Wins")
                play_game = False
                break

            for i in range(5):
                player_one_cards.append(player_one.remove_card())
                player_two_cards.append(player_two.remove_card())
