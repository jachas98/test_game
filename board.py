import random

from player import Player

class Board(object):
    players = 0
    player_turn = 0
    game_started = 0
    player = []

    def __init__(self, players):
        if 5 > players > 1:
            self.players = players

    def render_players(self):
        for i in range(0, self.players):
            self.player.append(Player(i))

    def return_players(self):
        return self.player

    def check_collision(self, pawn):
        for i in range(0, self.players):
            for p in range(0, 3):
                if not pawn.pawn_id == self.player[i].player_pawns[p].pawn_id:
                    if pawn.pawn_position == self.player[i].player_pawns[p].pawn_position:
                        self.player[i].player_pawns[p].pawn_resp = True
                        self.player[i].player_pawns[p].pawn_position = 0

    def roll_cube(self):
        roll = random.randint(1, 6)
        print("Wypadło: " + roll.__str__())
        moved = False
        while not moved:
            pionek = input()
            if 4 > int(pionek) > 0:
                moved = True
                self.next_player_turn()
                self.player[self.player_turn].player_pawns[int(pionek)].set_pawn_position(roll)

    def next_player_turn(self):
        if self.player_turn > 3:
            self.player_turn = 0
        self.player_turn += 1

    def get_player_turn(self):
        return self.player_turn
