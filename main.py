from start_menu import StartSimulator
from run_ball import Game

if __name__ == "__main__":
    start_simulator = StartSimulator(bg_image="bg.gif", game_class=Game)
    start_simulator.run()
