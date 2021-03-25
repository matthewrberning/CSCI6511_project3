from api import Api
from game import Game
import random
import time

def main():


	for i in range(10):
		agent = Api()
		user = Api("./api_key/mellon.json") #sorry

		board_size = 3+i
		
		if i > 3:
			target_size = 3+i-random.randint(1,2)
		else:
			target_size = 3

		print("target: ", target_size)
		print("size: ", board_size)

		game = Game(agent, user, size=board_size, target=target_size)

		print(f"Game created! $GME (1265) vs. MellonCap (1267) --> gameId: {game.gameId}")

		game.play_game()

		print("reminder target: ", target_size)
		print("reminder size: ", board_size)

		time.sleep(10)


if __name__ == "__main__":
    main()