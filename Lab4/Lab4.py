from numpy import *
from bitarray import *
import operator

#encode text using dict
def encode(text,dict):
    encode=bitarray()
    for i in text:
        for bit in dict[i]:
            encode.append(bit)
    return encode

#decode text using dict
def decode(encodeContent,dict):
    decode = ""
    for index in range(0, math.floor(len(encodeContent)/6)*6, 6):
        tmp=bitarray()
        for i in range(0,6):
            tmp.append(encodeContent[index+i])
        for j in dict:
            if(dict[j]==tmp):
                decode+=j
    return decode

#save encodeText and encode dict to files
def save(encodeContent,dict):
    content = encodeContent.copy()
    for _ in range(8 - (content.length() % 8) ):
        content.append(1)

    with open('./encoded_result.bin', 'wb') as file:
        content.tofile(file)

    with open('./key.txt', 'w') as key_file:
        for key in dict.keys():
            key_file.write(key + "\t")
            key_file.write(str(dict[key].to01())+ "\t")

#load encode data form file and encode key
def load():
    encodeText=bitarray()
    with open('./encoded_result.bin', 'rb') as file:
        encodeText.fromfile(file)
    dict={}

    dictContent=open('./key.txt').read().split('\t')

    for i in range(0,len(dictContent)-1,2):
        if (dictContent[i] not in dict):
            dict[dictContent[i]]=bitarray(dictContent[i+1])

    return encodeText,dict

#create code for characters using char frequency in text
def create(text):
    freq={}
    dict={}
    for i in text:
        if (i not in freq):
            freq[i]=0
        freq[i]+=1

    for j in freq:
        freq[j]=freq[j]/len(text)

    for i in range(1,len(freq)+1):
        key=max(freq.items(), key=operator.itemgetter(1))[0]
        value= bin(i)[2:]
        dict[key]=bitarray(value.rjust(6, '0'))
        del freq[key]

    return dict

def main():
    fileName = './norm_wiki_sample.txt'
    text = open(fileName).read()

    #make dict from data
    data="abcdefghijklmnoqprstuwxyzv 01233456789"
    dict={}
    for i in range(0, len(data)):
        if (data[i] not in dict):
            if (ord(data[i]) >= 97 and ord(data[i]) <= 122):
                value = bin(ord(data[i]) - 97)[2:]
                value = bitarray(value.rjust(6, '0'))
                dict[data[i]] = value
            elif (ord(data[i]) >= 48 and ord(data[i]) <= 57):
                value = bin(ord(data[i]) - 22)[2:]
                value = bitarray(value.rjust(6, '0'))
                dict[data[i]] = value
            elif (ord(data[i]) == 32):
                value = bin(ord(data[i]) + 5)[2:]
                value = bitarray(value.rjust(6, '0'))
                dict[data[i]] = value

    #create dict using char frequency -> the bigger frequency the smaller bin value
    #dict = create(text)

    #encode text
    encodeText=encode(text,dict)

    #save encode text and dict to files
    save(encodeText, dict)

    #load encode content and dict from file
    encodeTextFile ,dictFile= load()

    #decode text from file using encodeContent from file and dict from file
    decodeTextFile = decode(encodeTextFile,dictFile)
    print("Odkodowany text: " , decodeTextFile)

    if(decodeTextFile==text):
        print('Udalo sie odkodowany text z pliku .bin == wczytanemu z .txt')

if __name__ == '__main__':
    main()
