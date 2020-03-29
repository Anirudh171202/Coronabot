import sys
import json
import os
import re
l = []
directory = os.getcwd()
for file in os.listdir(directory):
    if file.endswith(".txt"):
        l.append(file)
print(l)
if "data.txt" not in l:
    with open("data.txt", "w+") as w:
        w.write("{}")
        w.close()


with open("data.txt", "r") as f:

    x = f.read()
    print(len(x))
    jsonData = {}
    if len(x) != 0:
        jsonData = eval(x)

    f.close()
    # windows ppl make /data.txt to \\data.txt
    os.remove(os.getcwd()+"/data.txt")
    print(jsonData)

    while True:
        mode = input("Enter i to insert d to delete v to view e to exit")
        if mode == "i":
            question = []
            answer = []
            source = []
            while True:

                try:
                    line = input('enter question : ')
                except EOFError:
                    break
                question.append(line)
            while True:
                try:
                    line = input('enter answer : ')
                except EOFError:
                    break
                answer.append(line)
            while True:
                try:
                    line = input('enter source : ')
                except EOFError:
                    break
                source.append(line)
            question = ' '.join(question)
            print("question: ", question)
            answer = ' '.join(answer)
            source = ' '.join(source)

            jsonData[question] = {"answer": answer, "source": source}

        elif mode == "d":
            word = input("Enter first word of question to delete")
            ans = None
            for key in jsonData.keys():
                if len(key) >= 1 and key.split(' ')[0] == word:
                    ans = key
            del jsonData[ans]

        elif mode == "v":
            print(json.dumps(jsonData, indent=4))

        elif mode == "e":
            # os.remove(os.getpwd()+"/data.json")
            with open("data.txt", "w+") as ff:
                ff.write(str(jsonData))

            break
        else:
            print("Pls try again....")
    # except:
    # 	with open("error.json", "w+") as ff:
    # 		json.dump(jsonData, ff)

    print("Bye")
