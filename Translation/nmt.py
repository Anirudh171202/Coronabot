import requests

def convertLang(msg, initlang, finlang):
    link = f"https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200328T211017Z.ab2eb594adaba721.7c008849ce33008b5aa263bd3053e3604d886c64&text={msg.replace(' ', '+')}&lang={initlang}-{finlang}"
    jsonData = requests.post(url=link)
    try:
        return (eval(jsonData.text)["text"])[0]
    except:
        return "Conversion not found"
print(convertLang("Luv is nice boy", "en", "sp"))