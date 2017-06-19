from pawn import Pawn


class Player(object):
    player_id = 0
    player_pawns = []

    def __init__(self, player_id):
        self.player_id = player_id
        for i in range(0, 3):
            self.player_pawns.append(Pawn(self.player_id, i))
