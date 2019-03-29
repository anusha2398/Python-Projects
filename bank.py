#Parent class
class AccountManager:
	def __init__(self, account_name, account_no, balance, pin):
		self.account_name = account_name
		self.account_no = account_no
		self.balance = float(balance)
		self.pin = pin
		self.transactions = []

	def deposit(self, amount = 0.0):
		if amount > 10000:
			print("You can't add amount more than 10000. Please try again!")
		elif amount > 0:
			print("Invalid deposit amount")
		else:
			self.balance += amount
			transactions = ('+' + str(amount), self.balance)
			self.transactions.append(transactions)

	def withdraw(self, amount = 0.0):
		if (self.balance - amount) < 0:
			print("Insufficient balance")
		elif self.balance <= 3000:
			print("Low balance")
		else:
			self.balance -= amount
			transactions = ('-' + str(amount), self.balance)
			self.transactions.append(transactions)

	def show_balance(self):
		print(f"The balance is {self.balance}")

	def account_statement(self):
		return self.transactions



#---------------------------------------------------------
#Child Class 1

class SavingsAccount(AccountManager):

	def __init__(self, account_name, account_no, balance, pin):
		self.account_name = account_name
		self.account_no = account_no
		self.pin = pin
		self.transactions = []

		if balance < 3000:
			print("Minimum opening balance should be 3000")
		else:
			self.balance = balance


#Child Class 2

class CurrentAccount(AccountManager):

	def __init__(self, account_name, account_no, balance, pin):
		self.account_name = account_name
		self.account_no = account_no
		self.pin = pin
		self.transactions = []

		if balance < 10000:
			print("Minimum opening balance should be 10000")
		else:
			self.balance = balance

	def withdraw(self, amount = 0.0):
		if (self.balance - amount) < 0:
			print("Insufficient balance")
		else:
			self.balance -= amount
			transactions = ('-'+str(amount), self.balance)
			self.transactions.append(transactions)

