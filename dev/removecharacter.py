import codecs
with codecs.open("data-abhinav.txt", 'r', encoding='utf-8',errors='ignore') as fdata:
    print(fdata.read())