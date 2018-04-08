from numpy import *

#slownik slow w tekscie dla 1,2,3 rzedu znakow
def generateDictChar(text):
    degree1=1
    degree2=2
    degree3=3

    dictMain={'xxxxxx':{'bbbbb':0}}
    dictCount={}

    for i in range (0,len(text)-degree1-3):
        key1=""
        key2=""
        key3=""
        for j in range(0,degree1):
            key1+=text[i+j]
        for z in range(0, degree2):
            key2 += text[i + z]
        for y in range(0, degree3):
            key3 += text[i + y]

        if (key1 not in dictMain):
            dictMain[key1] = {}
            dictCount[key1]=1
        else:
            dictCount[key1]+=1

        if (key2 not in dictMain):
            dictMain[key2] = {}
            dictCount[key2] = 1
        else:
            dictCount[key2] += 1

        if (key3 not in dictMain):
            dictMain[key3] = {}
            dictCount[key3] = 1
        else:
            dictCount[key3] += 1


        if (text[i+j+1] not in dictMain[key1]):
            dictMain[key1][text[i+j+1]]=1
        else:
            dictMain[key1][text[i + j + 1]] +=1

        if (text[i + z + 1] not in dictMain[key2]):
            dictMain[key2][text[i + z + 1]] = 1
        else:
            dictMain[key2][text[i + z + 1]] += 1

        if (text[i + y+ 1] not in dictMain[key3]):
            dictMain[key3][text[i + y + 1]] = 1
        else:
            dictMain[key3][text[i + y + 1]] += 1

    del dictMain['xxxxxx']
    for i in dictMain:
        for j in dictMain[i]:
            dictMain[i][j]=(dictMain[i][j]/dictCount[i])

    for i in dictCount:
        dictCount[i]=(dictCount[i]/len(text))

    return dictMain,dictCount

#slownik slow w tekscie dla 1,2,3 rzedu wyrazow
def generateDictWords(text):
    degree2 = 2
    degree3 = 3

    dictMain = {'xxxxxx': {'bbbbb': 0}}
    dictCount = {}

    for i in range(0, len(text) - degree3 - 3):
        key1 = text[i]
        key2 = text[i]
        key3 = text[i]
        for z in range(1, degree2):
            key2 += " " +  text[i + z]
        for y in range(1, degree3):
            key3 += " " + text[i + y]

        if (key1 not in dictMain):
            dictMain[key1] = {}
            dictCount[key1] = 1
        else:
            dictCount[key1] += 1

        if (key2 not in dictMain):
            dictMain[key2] = {}
            dictCount[key2] = 1
        else:
            dictCount[key2] += 1

        if (key3 not in dictMain):
            dictMain[key3] = {}
            dictCount[key3] = 1
        else:
            dictCount[key3] += 1

        if (text[i + 1] not in dictMain[key1]):
            dictMain[key1][text[i + 1]] = 1
        else:
            dictMain[key1][text[i + 1]] += 1

        if (text[i + z + 1] not in dictMain[key2]):
            dictMain[key2][text[i + z + 1]] = 1
        else:
            dictMain[key2][text[i + z + 1]] += 1

        if (text[i + y + 1] not in dictMain[key3]):
            dictMain[key3][text[i + y + 1]] = 1
        else:
            dictMain[key3][text[i + y + 1]] += 1

    del dictMain['xxxxxx']
    for i in dictMain:
        for j in dictMain[i]:
            dictMain[i][j] = (dictMain[i][j] / dictCount[i])

    for j in dictCount:
        dictCount[j]=(dictCount[j]/len(text))
    return dictMain,dictCount

#entropia zerowego rzedu , number =0 dla liter , 1 dla slow
def makeEntropiaZero(isChar,dictCountChar,dictCountWords):
    if(isChar==1):
        dict = dictCountChar
    else:
        dict = dictCountWords
    entropia = 0

    for key, value in dict.items():
            if(len(key)==1 and isChar==1) :
                entropia += (-1) * (value * math.log(value, 2))
            if ( len(key.split(" ")) == 1 and isChar!=1 ):
                entropia += (-1) * (value * math.log(value, 2))

    return entropia

#entropia rzedu degree, dictMain slownik slownikow znakow/slow dla 1,2,3 rzedu, dict to slownik p(x), isChar ==1 to licze dla slow
def makeEntropia(dictMain,dict, degree, isChar):
    entropiaMain = 0
    entropiaPom =0

    if (isChar==1):
        for key, value in dictMain.items():
            if (len(key)==degree):
                for j in value:
                    entropiaPom += value[j] * dict[key] * math.log(value[j], 2)

                entropiaMain+=entropiaPom
                entropiaPom=0
    else:
        for key, value in dictMain.items():
            if (len(key.split(" ")) == degree):
                for j in value:
                    entropiaPom += value[j] * dict[key] * math.log(value[j], 2)

                entropiaMain += entropiaPom
                entropiaPom = 0

    return entropiaMain*(-1)

def main():
    print("----------------ZAD 2---------------")
    pliki=['./norm_wiki_en.txt','./norm_wiki_eo.txt','./norm_wiki_et.txt','./norm_wiki_ht.txt','./norm_wiki_la.txt','./norm_wiki_nv.txt','./norm_wiki_sample.txt','./norm_wiki_so.txt','./sample0.txt','./sample1.txt','./sample2.txt','./sample3.txt','./sample4.txt','./sample5.txt']
    for plik in pliki:
        text = open(plik).read()

        dictMainChar, dictCountChar = generateDictChar(text)
        dictMainWords, dictCountWords = generateDictWords(text.split(" "))
        entropiaZeroChar = makeEntropiaZero(1,dictCountChar,dictCountWords)
        entropiaZeroWords = makeEntropiaZero(0,dictCountChar,dictCountWords)
        print(plik, " entropia zerowego rzedu slowa : ", entropiaZeroWords)
        print(plik, " entropia zerowego rzedu litery : ", entropiaZeroChar , "\n")
        for i in range(1,4):
            entropiaChar =makeEntropia(dictMainChar,dictCountChar,i,1)
            entropiaWords =makeEntropia(dictMainWords,dictCountWords,i,0)
            print(plik, " entropia rzedu ", i, " slowa : ", entropiaWords)
            print(plik, " entropia rzedu ", i, " litery : ", entropiaChar ,"\n")
        dictMainChar.clear()
        dictCountChar.clear()
        dictCountWords.clear()
        dictCountWords.clear()
if __name__ == '__main__':
    main()