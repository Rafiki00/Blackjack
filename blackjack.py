import random

dealers_hand = []
users_budget = 100
cards = ['A', 'A', 'A', 'A', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']
bet = input("Your budget is {}. How much are you willing to bet? ".format(users_budget))


class Game:
	
	def __init__(self):
		self.users_hand = random.choices(cards, k=2)
		self.dealers_hand = random.choices(cards, k=1)
		self.users_score = 0

	def evaluate(self):
		self.users_score = 0
		count = 1
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

		if self.users_score == 21:
			if count == 1:
				print("Blackjack! You win {}".format(self.users_budget * 1.5))
				self.users_budget += (bet * 1.5)
			else:
				self.users_budget += (bet * 2)

		if self.users_score > 21:
			print("You go bust! You lose {}".format(bet))

	def deal(self):
		self.users_hand.append(random.choice(cards))

	def decide(self):
		hit_or_stay = input("Do you want to hit or stay? (H/S) ")
		if(hit_or_stay == 'H'):
			self.deal()


new_game = Game()
print(new_game.users_hand)
print(new_game.dealers_hand)
new_game.evaluate()
print(new_game.users_score)
new_game.decide()
new_game.evaluate()
print(new_game.users_hand)
print(new_game.users_score)