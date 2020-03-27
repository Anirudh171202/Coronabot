import json
with open("data.json") as f :
	jsonData = json.load(f)
	while True:
		mode = input("Enter i to insert d to delete v to view e to exit")
		if mode == "i":
			question = input("Enter qs: ")
			answer = input("Enter ans: ")
			source = input("Enter source :")
			jsonData[question] = {"answer":answer, "source":source}
			json.dump(jsonData, f)

		if mode == "d":
			word = input("Enter first word of question to delete")
			for key in jsonData.keys() :
				if key.split(' ')[0] == word:
					del jsonData[key]
			json.dump(jsonData, f)
		if mode == "v":
			json.dumps(jsonData, indent=4)

		if mode == "e":
			break
		else:
			print("Pls try again....")


	print("Bye")