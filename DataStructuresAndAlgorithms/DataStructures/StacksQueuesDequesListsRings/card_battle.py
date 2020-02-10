# Задача №50. Игра в пьяницу
# https://informatics.mccme.ru/mod/statements/view3.php?id=206&chapterid=50#1


class CardBattle:
    def __init__(self, first_cards, second_cards):
        self.first_cards = first_cards
        self.second_cards = second_cards
        self.number_moves = 0

    def game(self):
        while self.first_cards and self.second_cards:
            element1, element2 = self.first_cards[0], self.second_cards[0]
            if self.first_player_con_conditions():
                self.remaining_cards_during_con()
                self.adding_cards_to_deck_player(self.first_cards, element1, element2)

            else:
                self.remaining_cards_during_con()
                self.adding_cards_to_deck_player(self.second_cards, element1, element2)

            self.number_moves += 1

            if self.many_moves_happened():
                return 'botva'

        winner = self.winner_determination()
        return winner, self.number_moves

    def first_player_con_conditions(self):
        return self.standard_case_first_player() or self.unique_case_first_player()

    def standard_case_first_player(self):
        return self.first_cards[0] > self.second_cards[0] and self.first_cards[0] - self.second_cards[0] != 9

    def unique_case_first_player(self):
        return self.first_cards[0] == 0 and self.second_cards[0] == 9

    def many_moves_happened(self):
        return self.number_moves > 1e6

    def remaining_cards_during_con(self):
        self.first_cards = self.first_cards[1:]
        self.second_cards = self.second_cards[1:]

    def adding_cards_to_deck_player(self, deck, first_card, second_card):
        deck.append(first_card)
        deck.append(second_card)

    def winner_determination(self):
        if len(self.first_cards) == 0:
            return 'second'
        else:
            return 'first'


if __name__ == '__main__':
    first_player = [int(i) for i in input().split()]
    second_player = [int(i) for i in input().split()]

    card_battle = CardBattle(first_player, second_player)

    champion = card_battle.game()

    if len(champion) == 2:
        for data in champion:
            print(data, end=' ')
    else:
        print(champion)





