import json
import re
jsonData = None
with open("data.json", errors="ignore") as f:
    jsonData = json.load(f)

wordsToRemove = ['corona', 'coronavirus', 'covid', 'covid-19', 'virus', 'illness','corona-virus']
fillers = ['a', 'an', 'the', 'of', 'that', 'i', 'are', 'in', 'if', 'to']

with open("temp.md", "w+") as f:
    intent_list = []
    for key in jsonData.keys():
        ans = jsonData[key]
        text = key.split(' ')
        text = [word.lower() for word in text]
        for word in wordsToRemove:
            if word in text:
                text.pop(text.index(word))
            

        text_without_fillers = [word.lower() for word in text if word not in fillers]
        longest_words = sorted(text, key=lambda x: -len(x))
        longest3words = ''.join(longest_words[:3])
       
        print("## intent:"+re.sub('[^A-Za-z0-9]+', '', longest3words), file=f)
        print(f"- {' '.join(text_without_fillers)}",file = f)      
        print(f"- {' '.join(text)}",file=f)



        for i in range(3):
            intent = re.sub('[^A-Za-z0-9]+ ', '', ' '.join(text[text.index(longest_words[i])-1:text.index(longest_words[i])+2]))
            if len(intent.strip()) < 3:
                pass
            else:
                print(f"- {intent}", file=f)

        for i in range(3):
            print(f"- {re.sub('[^A-Za-z0-9]+ ', '', longest_words[i])}", file=f)
        
        print(file=f)

        print(f"  utter_{re.sub('[^A-Za-z0-9]+', '', longest3words)}:")
        print("  - text: "+jsonData[key]["answer"].replace(':', ''))