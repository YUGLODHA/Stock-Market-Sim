import random
import os
import json

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
	return data["name"], data["balance"], data["stocks"], data["dob"], data["email"], data["phoneno"]

if __name__ == '__main__':
	# Load File and Save File
	if len(os.listdir(SAVESFOLDER))==0:
		os.system("cls")
		print("=================================Welcome to the Stock Market Simulator=================================")
		print("This is a text-based simulation of a simple stock market. You can buy, sell, and manage your portfolio.")
		print("Please fill in the following details(they are not nessary and can be random):")
		name=input("Name Of Your Portfolio: ")
		balance=10000.00
		stocks=[]
		dob=input("Date Of Birth(dd/mm/yyyy): ")
		email=input("Email Address: ")
		phoneno=input("Phone Number: ")
		savename=input("Name For Your Save File: ")
		save(savename, name, balance, stocks, dob, email)
	elif len(os.listdir(SAVESFOLDER))==1:
		name, balance, stocks, dob, email, phoneno = load(SAVESFOLDER+os.listdir(SAVESFOLDER)[0])
	else:
		file = input("Enter The Name of The Save You Want To Load: ")
		fileLoc = SAVESFOLDER+file+".json"
		name, balance, stocks, dob, email, phoneno = load(fileLoc)

	# Main Loop
	while True:
			os.system("cls")
			print("=================================Welcome to the Stock Market Simulator=================================")
			print(f"Portfolio: {name}")
			print(f"Current Balance: ${balance:.2f}")
			print("Current Stocks:", end="")
			for stock in stocks:
				print("Stock: {stock[0]}:{stock[1]}", end="")
			print("\nOptions:")
			print("1. Buy Stock")
			print("2. Sell Stock")
			print("3. View Portfolio")
			print("4. Update Personal Information")
			print("5. Exit")
			choice = input("Enter Your Choice: ")