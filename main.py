import random
import os
import json
import time

SAVESFOLDER = "saves/"

def save(savename, name, balance, stocks, dob, email):
	data = {
		"savename": savename,
		"name": name,
		"balance": balance,
        "stocks": stocks,
        "dob": dob,
        "email": email,
        "phoneno": phoneno}
	with open(SAVESFOLDER+savename+'.json', 'w') as file:
		json.dump(data, file, indent=4)

def load(path):
	with open(path, 'r') as file:
		data = json.load(file)
	return data["savename"], data["name"], data["balance"], data["stocks"], data["dob"], data["email"], data["phoneno"]

if __name__ == '__main__':
	# Load File and Save File
	if len(os.listdir(SAVESFOLDER))==0:
		os.system("cls")
		print("=================================Welcome to the Stock Market Simulator=================================")
		print("This is a text-based simulation of a simple stock market. You can buy, sell, and manage your portfolio.")
		print("Please fill in the following details(they are not nessary and can be random):")
		name=input("Name Of Your Portfolio: ")
		balance=1000.00
		stocks=[]
		dob=input("Date Of Birth(dd/mm/yyyy): ")
		email=input("Email Address: ")
		phoneno=input("Phone Number: ")
		savename=input("Name For Your Save File: ")
		save(savename, name, balance, stocks, dob, email)
	elif len(os.listdir(SAVESFOLDER))==1:
		savename, name, balance, stocks, dob, email, phoneno = load(SAVESFOLDER+os.listdir(SAVESFOLDER)[0])
	else:
		file = input("Enter The Name of The Save You Want To Load: ")
		fileLoc = SAVESFOLDER+file+".json"
		savename, name, balance, stocks, dob, email, phoneno = load(fileLoc)

	# Main Loop
	while True:
			os.system('cls')
			print("=================================The Stock Market Simulator=================================")
			print("\nOptions:")
			print("1. Buy Stock")
			print("2. Sell Stock")
			print("3. View Portfolio")
			print("4. Update Personal Information")
			print("5. Save")
			print("6. Exit")
			choice = input("Enter Your Choice: ")
			if choice=='1':
				pass
			elif choice=='2':
				pass
			elif choice=='3':
				print("Your Portfolio:")
				print(f"Name: {name}")
				print(f"Current Balance: ${balance:.2f}")
				print("Current Stocks:", end="")
				for stock in stocks:
					print("Stock: {stock[0]}:{stock[1]}", end="")
				print(f"\nDate Of Birth: {dob}")
				print(f"Email Address: {email}")
				print(f"Phone Number: {phoneno}")
				input("Press Enter to continue...")
			elif choice=='4':
				print("Enter Your New Personal Information:")
				name=input("Name Of Your Portfolio: ")
				dob=input("Date Of Birth(dd/mm/yyyy): ")
				email=input("Email Address: ")
				phoneno=input("Phone Number: ")
				save(savename, name, balance, stocks, dob, email)
				print("Personal Information Updated")
				input("Press Enter to continue...")
			elif choice=='5':
				save(savename, name, balance, stocks, dob, email)
				print("Changes Saved")
				input("Press Enter to continue...")
			elif choice=='6':
				confirm = input("Are You Sure You Want To Exit [y/n]: ").lower()
				if confirm=='y':save(savename, name, balance, stocks, dob, email)
				print("Changes Saved, Thank For Playing")
				time.sleep(1)
				exit(0)
			else:
				print("Invalid Choice")
				time.sleep(1)