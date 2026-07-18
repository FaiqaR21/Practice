import string
#open file
with open("file.txt","r") as file:
    data=file.read()

#ignore puntuations
data =data.lower()

for punc in string.punctuation:
    data=data.replace(punc,"")

#counts frequency
words=data.split()

freq={}

for w in words:
    if w in freq:
        freq[w]+=1

    else:
        freq[w]=1

for word,count in freq.items():
    print(word,":",count)





