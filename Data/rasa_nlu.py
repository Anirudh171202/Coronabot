import json
import re
jsonData = None
with open("data.json", errors="ignore") as f :
    jsonData = json.load(f)


wordsToRemove=['corona', 'coronavirus', 'covid', 'covid-19', 'virus', 'illness']


with open("markdown.md", "w+") as f:
    intent_list = []
    for key in jsonData.keys():
        ans = jsonData[key]
        text = key.split(' ')
        text = [word.lower() for word in text]
        for word in wordsToRemove:
            if word in key:
                key.pop(key.index(word))
                      

        longest_words = sorted(text, key=lambda x : -len(x))
        longest3words = ''.join(longest_words[:3])
        print(f"  utter_{re.sub('[^A-Za-z0-9]+', '', longest3words)}:")
        print(f"  - text: {jsonData[key]['answer']}")
        print()
        print("## intent:"+re.sub('[^A-Za-z0-9]+', '', longest3words), file=f)

        print(f"- {re.sub('[^A-Za-z0-9]+', '', longest3words)}")
        for i in range(3):
            print(f"- {re.sub('[^A-Za-z0-9]+ ', '', ' '.join(text[text.index(longest_words[i])-1:text.index(longest_words[i])+2]))}", file=f)
        
        for i in range(3):
            print(f"- {re.sub('[^A-Za-z0-9]+ ', '', longest_words[i])}", file=f)

        
    
        
        print(file=f)

        
       

        
