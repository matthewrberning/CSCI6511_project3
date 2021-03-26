from game import Game
from api import Api


def main():

	game_type = str(input("\nstart a 'n'ew interactive game?\n'c'ontinue an interactive game? \n'l'isten for games?\n'o'pen a game with another team?\n'j'oin an open game?\n(default is new interactive/debug game)\n") or "n")

	if game_type == "n":

		agent = Api()
		user = Api("./api_key/mellon.json") #sorry

		board_size = int(input("board size? (default is 3)\nsize: ") or "3")
		
		target_size = int(input("how many to win? (must be less than or equal to board size -default is 3)\ntarget: ") or "3")

		game = Game(agent, user, size=board_size, target=target_size)

		print(f"Game created! $GME (1265) vs. MellonCap (1267) --> gameId: {game.gameId}")

		game.play_game()


	elif game_type == "c":

		agent = Api()
		user = Api("./api_key/mellon.json")

		gameId = input("what's the gameId?\ngameId: ")

		game = Game(agent, user, gameId=gameId)

		game.play_game()

	elif game_type == "o":

		agent = Api()
		opponent = int(input("other team's ID? (default is 1267)\nteamId: ") or "1267")

		board_size = int(input("board size? (default is 3)\nsize: ") or "3")
		
		target_size = int(input("how many to win? (must be less than or equal to board size -default is 3)\ntarget: ") or "3")

		game = Game(agent, opponent, size=board_size, target=target_size)

		print(f"Game created! $GME (1265) vs. [OUTSIDE TEAM?!?] ({opponent}) --> gameId: {game.gameId}")

		game.play_game()

	elif game_type == "j":

		agent = Api()
		opponent = int(input("other team's ID?\nteamId: "))

		gameId = int(input("what's the game ID?\ngameId: "))

		game = Game(agent, opponent, gameId=gameId)

		print(f"Game begun! $GME (1265) vs. [OUTSIDE TEAM?!?] ({opponent}) --> gameId: {game.gameId}")

		game.play_game(who_starts="them")

	else:
		print("that option doesn't exist yet :'(")
		# while true check for open games, create a new instance of game play
		# add instance to collection, list? update each sucessively? 
		# for instance in instances: instance.check_and_move/report?
		exit()






if __name__ == "__main__":
    main()