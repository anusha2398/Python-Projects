from bank import AccountManager
acc1 = AccountManager("Anusha", 123, 10000)
acc1.show_balance()
acc1.deposit(1000)
acc1.show_balance()
acc1.withdraw(4000)
acc1.show_balance()
acc1.withdraw(8000)   #to show insufficient balance