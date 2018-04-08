from random import randint
from numpy import *
from collections import Counter
#zad1
#generuje przyblizenie pierwszego rzedu
def generatorRand(alfabet,number):
    tab=""
    for i in range(number):
        tab+=alfabet[randint(0,len(alfabet)-1)]
    return tab

#liczy srednia dlugosc slowa w tablicy podanej jako argument
def avgWordLen(tab):
    space=0
    splitText=tab.split(" ")
    length=len(splitText)
    for i in splitText:
        if (len(i)>0): #tylko te elementy ktore po splicie nie sa spacja
            space+=len(i)
        else: #jak sa to zmniejszamy liczbe slow w tekscie
            length=length-1
    return  space/length

#zad2
#czestosc wystepowania w text, znakow w alfabet
def calculateFreq(text):
    result={}

    #sprawdzam pokolei litery w tekscie i sprawdzam czy jest ona kluczem w slowniku, jesli nie to dodaje z wart 0, jesli jest inkrementuje
    for i in text:
        if (i not in result):
            result[i] = 0
        result[i] += 1

    #ilosc wystapien / dlugosc tekstu
    for i in result:
        result[i] = (result[i] / len(text))

    return result

#zad3
#zwraca znak ktory jest w momencie wylosowanego przedzialu kola
def generateUsingDict(dict,number):
    sum=0
    for i in dict:
        sum+=dict[i]
        if(number<sum):
            return i
    return ''

#tworzy nowa waidomosc z zadanym prawdopodobienstwem
def givenProbabiltyText(dict,length):
    newMsg=""
    for i in range(length):
        number = random.uniform(0,1)
        newMsg+=generateUsingDict(dict,number)
    return  newMsg

#zad4
#zlicza number najczesciej wystepujacych znakow w text
def mostCommon(text,number):
    return dict(Counter(text).most_common(number))

#zlicza prawdopodobienstwo wystapienia znakow po character w text, characterCount
def makeProbablityAfterChar(text,character):
    dict={}
    characterCount=0
    for i in range(1,len(text)):
        if (text[i]==character):
            characterCount+=1
        if(text[i-1]==character):
            if (text[i] not in dict):
                dict[text[i]]=1
            else:
                dict[text[i]]+=1

    for j in dict:
        dict[j]=dict[j]/characterCount

    return dict

#zad5
#przy uzyciu finda
def makeMarkow(text,length,degree ):
    myText = "probability"
    for i in range(length):
        x=""
        for j in range(degree,0,-1):
            x+=myText[len(myText)-j]

        newChar = nextCharacter(text,x)
        myText+=newChar
    return myText

def nextCharacter(text,subString):
        it =0
        while(it ==0):
            begin = randint(0,len(text)-1)
            #end = randint(begin,len(text)-1)
            idx = text.find(subString,begin,len(text)-1)
            if (idx!=-1):
                it=1

        return text[idx+len(subString)]

#slownik slownikow na calym tekscie
def makeMarkowUsingDict(text,degree,lenText):

    dictMain={'xxxxxx':{'bbbbb':0}}
    dictCount={}

    for i in range (0,len(text)-degree):
        key=""

        for j in range(0,degree):
            key+=text[i+j]

        if (key not in dictMain):
            dictMain[key] = {}
            dictCount[key]=1
        else:
            dictCount[key]+=1


        if (text[i+j+1] not in dictMain[key]):
            dictMain[key][text[i+j+1]]=1
        else:
            dictMain[key][text[i + j + 1]] +=1

    del dictMain['xxxxxx']

    for i in dictMain:
        for j in dictMain[i]:
            dictMain[i][j]=(dictMain[i][j]/dictCount[i])



    myText = "probability"

    for j in range(1, lenText):
        number = random.uniform(0, 1)
        key1 = ""
        for p in range(degree, 0,-1):
            key1 += myText[len(myText)-p]
        sign = generateUsingDict(dictMain[key1], number)
        myText += sign

    return myText


def main():
    #wczytane pliku
    text = open('./norm_wiki_sample.txt').read()
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'p', 'r', 's', 't', 'u','w', 'x',  'y', 'z','v', ' ']

    #zadanie1
    print("----------------ZAD 1---------------")
    tab=generatorRand(alfabet,3000)
    print("Wygenrowany tekst(O RZAD):", tab)
    avgWordLength=avgWordLen(text)
    print("Srednia dlugosc slwoa w wiki:" , avgWordLength)
    print()

    #zadanie2
    print("----------------ZAD 2---------------")
    dict=calculateFreq(text)
    print("Zawartosc slownika" , dict)
    print()

    #zadanie3
    print("----------------ZAD 3---------------")
    newTab=givenProbabiltyText(dict,300)
    print("Wygenerowany teskt(1 rzad):",newTab)
    newTabAvg=avgWordLen(newTab)
    print("Srednia dlugosc slowa w tekscie(1 rzad): ", newTabAvg)
    print()

    #zadanie4
    print("----------------ZAD 4---------------")
    textZad4 = "beekeepers keep bees in a beehive"
    mostFreq= mostCommon(textZad4,2)
    for i in mostFreq:
        print("znak",i + " liczba wystapien : ",mostFreq[i])
        x=makeProbablityAfterChar(textZad4,i)
        print(x)
    print()

    #zadanie5
    print("----------------ZAD 5---------------")

    #PRZY UZYCIU SLOWNIKOW NA CALYM TEKSCIE
    #POPRAWIC LOSOWANIE

    print("-------- PRZY UZYCIU SLOWNIKA SLOWNIKOW NA CALYM TEKSCIE ---------------")
    firstText = makeMarkowUsingDict(text,1,5000)
    avgFirst = avgWordLen(firstText)
    print("Przyblizenie dla zrodla Markowa 1-szego rzedu :")
    print(firstText)
    print("Srednia dlugosc slowa: ", avgFirst)
    print()

    thirdText = makeMarkowUsingDict(text,3,5000)
    avgThird = avgWordLen(thirdText)
    print("Przyblizenie dla zrodla Markowa 3-ciego rzedu :")
    print(thirdText)
    print ("Srednia dlugosc slowa: ", avgThird)
    print()

    fiveText = makeMarkowUsingDict(text,5,5000)
    avgFive = avgWordLen(fiveText)
    print("Przyblizenie dla zrodla Markowa 5-tego rzedu :")
    print(fiveText)
    print("Srednia dlugosc slowa: ", avgFive)
    print()


    #PRZY UZYCIU FUNKCJI FIND

    # print("-------- PRZY UZYCIU FUNKCJI FIND ---------------")
    # firstText =makeMarkow(text,500,1)
    # avgFirst = avgWordLen(firstText)
    # print("Przyblizenie dla zrodla Markowa 1-szego rzedu :")
    # print(firstText)
    # print("Srednia dlugosc slowa: ", avgFirst)
    # print()
    #
    # thirdText = makeMarkow(text,500,3)
    # avgThird = avgWordLen(thirdText)
    # print("Przyblizenie dla zrodla Markowa 3-ciego rzedu :")
    # print(thirdText)
    # print ("Srednia dlugosc slowa: ", avgThird)
    # print()
    #
    # fiveText = makeMarkow(text,500,5)
    # avgFive = avgWordLen(fiveText)
    # print("Przyblizenie dla zrodla Markowa 5-tego rzedu :")
    # print(fiveText)
    # print("Srednia dlugosc slowa: ", avgFive)
    # print()


if __name__ == '__main__':
    main()