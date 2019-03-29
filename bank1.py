class AccountManager:

	def __init__(self, account_name, account_no, balance):
		self.account_name = account_name
		self.account_no = account_no
		self.balance = balance
		

	def deposit(self, amount):
		if amount > 10000:
			print("Cannot deposit more than 10000")
		elif amount < 0:
			print("Invalid deposit amount.")
		else:
			self.balance += amount

	def withdraw(self, amount):
		if amount > self.balance:
			print("insufficient balance")
		else:
			self.balance -= amount


	def show_balance(self):
		print(f"The balance is {self.balance}")