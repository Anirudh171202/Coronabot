import json
import os

with open(f"{name}.json","w+") as f :
	
	x = f.read()
	if not x:
		jsonData = {}

	else:	
		jsonData = json.load(f)		
	print("just got json: ", jsonData)
	
	while True:
		
			
			
				
		mode = input("Enter i to insert d to delete v to view e to exit")
		if mode == "i":
			question = input("Enter qs: ")
			answer = input("Enter ans: ")
			source = input("Enter source :")
			jsonData[question] = {"answer":answer,"source":source}
			

		elif mode == "d":
			
			word = input("Enter first word of question to delete")
			ans = None
			for key in jsonData.keys() :
				if key.split(' ')[0] == word:
					ans = key
			if not ans:
				del jsonData[ans]
			json.dump(jsonData, f)
		elif mode == "v":
			print(jsonData)
			print(json.dumps(jsonData, indent=4))

		elif mode == "e":
			break
		else:
			print("Pls try again....")

		


	print("Bye")