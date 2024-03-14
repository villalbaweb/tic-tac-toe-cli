from game_logic import GameLogic

game_logic = GameLogic()

# driver code

if __name__ == '__main__':

    is_game_running = True
    while(is_game_running):
        is_game_running = not game_logic.play_game()
    