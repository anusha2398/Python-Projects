from bank import AccountManager

accounts = []
account_no = 1001
print ("-" *50)
print("Welcome to Iron Bank")

while True:
	print("Hey! What would you like to do today \n\
		1. Create account\n\
		2. Check transactions\n\
		3. Deposit Amount\n\
		4. Withdraw Amount\n\
		5. Show balance\n\
		6. Exit\n")

	choice = int(input("Enter yur option:"))

	if choice == 1:
		acc_name = input("Enter account name:")
		balance = input("Enter the opening balance:")
		pin = int(input("Enter a PIN for your account:"))

		account[account_no] = AccountManager(acc_name, account_no, balance, pin)
		print(accounts)

		print(f"Account created successfully! Your account number is {account_no}")

		account_no += 1

	elif choice == 2: