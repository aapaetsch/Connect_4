from json import dump, load
class ComputerPlayer:
	def __init__(self, ):
		# X is always computer player
		self.__moveDict = self.__loadMoves()
		self.__currentBoard = None

	def recieveBoard(self, board):
		self.__currentBoard = board
	

	def updateDict(self):
		key = str(self.__currentBoard)
		try:
			moves = self.__moveDict[key]
		except:
			pass


	def storeMoves(self):
		with open("bestmoves.json", 'w') as f:
			dump(self.__moveDict,f)

	def __loadMoves(self):
		try:
			with open("bestmoves.json",'r') as f:
				return load(f)
		except:
			return {}

x = ComputerPlayer()
