from board import Board

game = Board(4)
game.render_players()
print(game.player)
while True:
    print(game.get_player_turn())
    print(game.player_turn)
    game.roll_cube()
