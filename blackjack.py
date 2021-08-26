import random

dealers_hand = []
users_budget = 100
cards = ['A', 'A', 'A', 'A', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']

def NewGame():
	while True:
		user_bet = int(input("Your budget is {}. How much are you willing to bet? ".format(users_budget)))
		if user_bet <= users_budget:
			break
		else:
			print("Your bet is higher than your budget!")
			continue
	global bet
	bet = user_bet
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
			if self.count == 1:
				print("Blackjack! You win {}".format(bet * 1.5))
				self.users_budget += (bet * 1.5)
				return
			else:
				self.users_budget += (bet * 2)
				return

		if self.users_score > 21:
			print("You go bust! You lose {}".format(bet))
			return

		self.count += 1	
		self.decide()

	def deal(self):
		self.users_hand.append(random.choice(cards))
		self.evaluate()

	def decide(self):
		hit_or_stay = input("Do you want to hit or stay? (H/S) ")
		if(hit_or_stay == 'H'):
			self.deal()
		else:
			self.dealers_turn()

	def dealers_turn(self):
		self.dealers_hand.append(random.choice(cards))
		print("The dealers cards are {}".format(self.dealers_hand))
		self.evaluate_dealers()

	def evaluate_dealers(self):
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
			print("It's a tie! You get your bet back.")
			return
		elif self.dealers_score <= 16:
			self.dealers_turn()
		elif self.dealers_score > 16 <= 21:
			if self.dealers_score < self.users_score:
				print("You win {}".format(bet * 2))
				return
			else:
				print("You lose your bet ({})".format(bet))
				return
		else:
			print("The dealer went bust. You win {}".format(bet * 2))
			return

	def reset(self):
		self.users_hand = random.choices(cards, k=2)
		self.dealers_hand = random.choices(cards, k=1)
		self.count = 0
		print(self.users_hand)
		print(self.dealers_hand)
		NewGame()


NewGame()


