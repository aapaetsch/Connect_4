import time, os, sys
import bestMoves
class Connect4:
	def __init__(self):
		self.board = [[' ' for i in range(7)] for j in range(6)]
		self.Current_Player = 'X'
		self.Previous = 'O'
		self.__moves = [0,1,2,3,4,5,6]
		#Determine OS for proper clear screen
		self.__isPC = None
		self.__computer = bestMoves.ComputerPlayer()
		if sys.platform == 'win32': self.__isPC = True
		else: self.__isPC = False

	def __pBoard(self):
		b = ''
		for i in self.board:
			b+='|'
			for j in i:
				b+=j
				b+='|'
			b+= '\n'
		print('\n   Connect4!\n 0 1 2 3 4 5 6\n'+b)

	def __PlayerSwitch(self):
		swap = self.Current_Player
		self.Current_Player = self.Previous
		self.Previous = swap

	def turn(self):
		while True:

			if self.__isPC: os.system('cls')
			else: os.system('clear')

			#print('\n   Connect 4!')
			self.__pBoard()
			piece = self.Current_Player
			if self.Current_Player = 'X':
				
				print('Computer Player to go...')
				self.__computer.recieveBoard(self.board)

				time.sleep(1)
				move = self.__computer.returnMove()
				self.__drop(move)

			else:
				print("Human Player to go... ")

				move = input('Enter a valid move from 0-6> ')

				try: move = int(move)
				except: print('Entered value is not an integer.')

				if move in self.__moves:
					self.__drop(move)
				else:
					print('Invalid move entered.')
					time.sleep(2)

	def __drop(self, move):
		currentPos = []
		for i in range(6):
			if self.board[i][move] == ' ':
				self.board[i][move] = self.Current_Player
				currentPos = [i,move]
			#self.__pBoard()
			if i != 5 and self.board[i+1][move] == ' ':
				self.board[i][move] = ' '
			#	time.sleep(0.5)
		if self.board[0][move] != ' ':
			self.__moves.remove(move)
			#print(self.__moves)
			#time.sleep(1)
		self.__winCheck(currentPos)

		


	def __horiz(self, x,y):
		inrow = 1
		#Check Left
		for i in range(1,5):
			if ((x-i) >= 0) and self.board[y][x-i] == self.Current_Player:
				inrow+=1
				if inrow == 4: return True
			else: break
		#Check Right
		for i in range(1,5):
			if ((x+i) < 6) and self.board[y][x+i] == self.Current_Player:
				inrow+=1
				if inrow == 4: return True
			else: break
		return False




	def __vert(self, x,y):
		inrow = 1
		#checks down only
		if y <=2:
			for i in range(1,5):
				if self.board[y+i][x] == self.Current_Player:
					inrow+=1
					if inrow == 4: return True
				else: break
		return False

	def __diag(self, x,y):
		inrow = 1
		#check up left
		for i in range(1,5):
			if ((x-i) >= 0) and ((y-i) >= 0) and self.board[y-i][x-i] == self.Current_Player:
				inrow+=1
				if inrow == 4: return True
			else: break
		
		#check down right
		for i in range(1,5):
			if ((x+i)<7) and ((y+i)<6) and self.board[y+i][x+i] == self.Current_Player:
				inrow+=1
				if inrow == 4: return True
			else: break

		#separate
		inrow = 1
		#check up right
		for i in range(1,5):
			if ((x+i)<7) and ((y-i) >= 0) and self.board[y-i][x+i] == self.Current_Player:
				inrow+=1
				if inrow == 4: return True
			else: break
		
		#check down left
		for i in range(1,5):
			if ((x-i)>=0) and ((y+i)<6) and self.board[y+i][x-i] == self.Current_Player:
				inrow+=1
				if inrow == 4: return True
			else: break

		return False

	def __winCheck(self, move):
		#check for a win
		current = self.Current_Player
		y,x = move
		#check for another piece
		if self.__horiz(x,y) or self.__vert(x,y) or self.__diag(x,y):
			if self.__isPC: os.system('cls')
			else: os.system('clear')
			self.__pBoard()
			print('Player '+ current+' wins!')
			
			exit(0)
		elif len(self.__moves) == 0:
			print('No remaining move, Draw.')
			exit(0)
		self.__PlayerSwitch()

	
		# if no win detected, swap players

		

def main():
	c4 = Connect4()
	c4.turn()
	
main()