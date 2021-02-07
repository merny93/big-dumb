from src.board import Board

player = [["simon", True], ["Mom", True], ["Daniel", True]]
game = Board(player)

while True:
    game.play_turn()