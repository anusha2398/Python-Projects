#Parent class
class ApparelManager:
	def __init__(self, unique_id, account_name, email_id, address, size, type_of_apparel):
		self.unique_id = unique_id
		self.account_name = account_name
		self.email_id = email_id
		self.address = address
		self.size = size
		self.type_of_apparel = type_of_apparel

	def purchase(self, total = 0.0):
		if total < 500:
			print("You can't purchase if total is less than 500.")
		elif amount > 0:
			
		else:
			

	def rent(self, total = 0.0):
		if (self.balance - amount) < 0:
			print("Insufficient balance")
		elif self.balance <= 3000:
			print("Low balance")
		else:
			self.balance -= amount
			transactions = ('-' + str(amount), self.balance)
			self.transactions.append(transactions)

	def sales(self):
		print(f"The balance is {self.balance}")

	



#---------------------------------------------------------
#Child Class 1

class SavingsAccount(AccountManager):

	def __init__(self, unique_id, account_no, account_no):


#Child Class 2

class CurrentAccount(AccountManager):

	def __init__(self, unique_id, account_no, account_name):


