class Pawn(object):
    pawn_id = 0
    pawn_position = 0
    pawn_owner = 0
    pawn_resp = False

    def __init__(self, player_id, pawn_id):
        self.pawn_position = 0
        self.pawn_id = pawn_id
        self.pawn_owner = player_id
        self.pawn_resp = False

    def set_pawn_position(self, roll):
        if self.pawn_position + roll > 45:
            self.pawn_position = self.pawn_position - 45
            self.set_pawn_position(roll)
        else:
            self.pawn_position += roll

    def get_pawn_position(self):
        return self.pawn_position
