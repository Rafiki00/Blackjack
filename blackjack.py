import random

cards = ['A', 'A', 'A', 'A', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']

def NewGame():

	global budget
	global bet

	while True:
		users_budget = int(input("What is your budget? "))
		users_bet = int(input("Your budget is {}. How much are you willing to bet? ".format(users_budget)))
		if users_bet <= users_budget:
			break
		else:
			print("Your bet is higher than your budget!")
			continue

	bet = users_bet
	budget = users_budget
	new_game = Game()


def PlayAgain():

	global budget

	while True:
		users_bet = int(input("Your budget is {}. How much are you willing to bet? ".format(budget)))
		if users_bet <= budget:
			break
		else:
			print("Your bet is higher than your budget!")
			continue

	global bet
	bet = users_bet
	new_game = Game()	


class Game:
	
	def __init__(self):
		self.users_hand = random.choices(cards, k=2)
		self.dealers_hand = random.choices(cards, k=1)
		self.count = 0
		print(self.users_hand)
		print(self.dealers_hand)
		self.evaluate()

	def evaluate(self):
		global budget
		self.users_score = 0

		for i in self.users_hand:
			if i in ['J', 'Q', 'K']:
				self.users_score += 10
			elif i == 'A':
				if self.users_score >= 11:
					self.users_score += 1
				else:
					self.users_score += 11
			else:
				self.users_score += i

		print("Your score is {}".format(self.users_score))		

		if self.users_score == 21:
			if self.count == 0:
				budget += (bet * 1.5)
				print("Blackjack! You win {}. Your budget is now {}".format(bet * 1.5, budget))
				self.reset()

		if self.users_score > 21:
			budget -= bet
			print("You go bust! You lose {}. Your budget is now {}".format(bet, budget))
			self.reset()

		self.count += 1	
		self.decide()

	def deal(self):
		self.users_hand.append(random.choice(cards))
		self.evaluate()

	def decide(self):
		hit_or_stay = input("Do you want to hit or stay? (H/S) ").upper()
		if(hit_or_stay == 'H'):
			self.deal()
		else:
			self.dealers_turn()

	def dealers_turn(self):
		self.dealers_hand.append(random.choice(cards))
		print("The dealers cards are {}".format(self.dealers_hand))
		self.evaluate_dealers()

	def evaluate_dealers(self):
		global budget
		self.dealers_score = 0
		for i in self.dealers_hand:
			if i in ['J', 'Q', 'K']:
				self.dealers_score += 10
			elif i == 'A':
				if self.dealers_score >= 11:
					self.dealers_score += 1
				else:
					self.dealers_score += 11
			else:
				self.dealers_score += i
		print("The dealer's score is {}".format(self.dealers_score))		
		if self.dealers_score == self.users_score:
			print("It's a tie! You get your bet back. Your budget is {}".format(budget))
			self.reset()
		elif self.dealers_score <= 16:
			self.dealers_turn()
		elif self.dealers_score > 16 and self.dealers_score <= 21:
			if self.dealers_score < self.users_score:
				budget += bet * 2
				print("You win {}. Your budget is now {}".format(bet * 2, budget))
				self.reset()
			else:
				budget -= bet
				print("You lose your bet ({}). Your budget is now {}".format(bet, budget))
				self.reset()
		else:
			budget += bet * 2
			print("The dealer went bust. You win {}. Your budget is now {}".format(bet * 2, budget))
			self.reset()

	def reset(self):
		end_game = input("What do you want to do now? \n Bet again (B). Quit (Q). Reset game (R)").upper()
		global budget

		if end_game == 'B':
			self.users_hand = random.choices(cards, k=2)
			self.dealers_hand = random.choices(cards, k=1)
			self.count = 0
			PlayAgain()
		elif end_game == 'Q':
			print("Thank you for playing Blackjack.")
			return
		else:
			budget = 0
			self.users_hand = random.choices(cards, k=2)
			self.dealers_hand = random.choices(cards, k=1)
			self.count = 0
			NewGame()	

NewGame()


