from project import ApparelManager

accounts = []
account_no = 1001
print ("-" *50)
print("Welcome to ABC")

while True:
	print("Hey! What would you like to do today \n\
		1. Create account\n\
		2. Purchase\n\
		3. Rent\n\
		4. sales\n\
		5. Exit\n")
	

	choice = int(input("Enter your option:"))

	if choice == 1:
		acc_name = input("Enter account name:")
		unique_id = input("Enter unique id:")
		address = input("Enter address:")
		email_id = input("Enter email id:")

		account[account_no] = ApparelManager(acc_name, account_no, unique_id, address, email_id)
		print(accounts)

		print(f"Account created successfully! Your account number is {account_no}")

		account_no += 1

	elif choice == 2:
		acc_name = input("Enter account name:")
		unique_id = input("Enter unique id:")
		size = int(input("Enter your size:"))

		print("Select the type of dress you want\n\
				1. Shirts\n\
				2. Trousers\n")

		choice1 = int(input("Enter your option:"))

		if choice1 == 1:
			print("")


		if choice1 == 2:
			print("")


	elif choice == 3:
		print("Hey! Do you want to rent a dress?")
		unique_id = input("Enter your unique id:")
		acc_name = input("Enter your account name:")
		print("Thanks for choosing us!")

	elif choice == 4:
		print("Thanks for choosing us!")
		print("Choose what would you like to puchase today from our store:\n\n\
			1. Black Shirts\n\
			2. Beige trousers\n\
			3. Blue Shirt\n\
			4. Black trousers\n")
			

		choice2 = int(input("Enter your choice:"))


		if choice2 == 1:


		elif choice2 == 2:


		elif choice2 == 3:


		elif choice2 == 4:



		elif choice2 == 5:




	else:
		print("Thanks for shopping with us. Have a nice day!!")
		
