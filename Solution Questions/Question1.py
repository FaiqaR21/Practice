import string
#open file
with open("file.txt", "r") as file:
    data = file.read()

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

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_freq[:10]:
    print(word, ":", count)





