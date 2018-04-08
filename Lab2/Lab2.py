from numpy import *

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

#ruletka
def generateUsingDict(dict,number):
    sum=0
    for i in dict:
        sum+=dict[i]
        if(number<sum):
            return i
    return ''

#slownik slow w tekscie
def generateDict(text,degree1,degree2):

    dictMain={'xxxxxx':{'bbbbb':0}}
    dictCount={}
    #text.remove('')
    for i in range (0,len(text)-degree1-2):
        key1=""
        key2=""
        for j in range(0,degree1):
            key1+=text[i+j]
        for z in range(0, degree2):
            key2 += text[i + z]

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


        if (text[i+j+1] not in dictMain[key1]):
            dictMain[key1][text[i+j+1]]=1
        else:
            dictMain[key1][text[i + j + 1]] +=1

        if (text[i + z + 1] not in dictMain[key2]):
            dictMain[key2][text[i + z + 1]] = 1
        else:
            dictMain[key2][text[i + z + 1]] += 1

    del dictMain['xxxxxx']
    for i in dictMain:
        for j in dictMain[i]:
            dictMain[i][j]=(dictMain[i][j]/dictCount[i])
    return dictMain

def makeMarkowUsingDict(degree,lenText,initDict,dictMain,startWord):
    #generowanie na podstawie slow
    if startWord :
        myText='probability '
    else:
        myText = ""

    for j in range(1, lenText):
        number = random.uniform(0, 1)
        if(j<=2 and startWord==0):
            sign = generateUsingDict(initDict, number)
            myText += sign +' '
        else:
            myTextSplit=myText.split(" ")
            myTextSplit.remove('')
            key1 = ""
            for p in range(degree, 0,-1):
                key1 +=myTextSplit[len(myTextSplit)-p]

            if key1 not in dictMain:
                sign=generateUsingDict(dictMain[key1[1]],number)
                myText += sign + ' '
            else:
                sign = generateUsingDict(dictMain[key1], number)
                myText +=sign + ' '
    return myText

def main():
    #wczytane pliku
    text = open('./norm_wiki_sample.txt').read()
    textPom = text.split(' ')
    #LAB2
    #zad1
    print('--------- ZAD1 ---------')
    dict={}
    for i in textPom:
        if (i not in dict):
            dict[i] = 1

        else:
            dict[i] += 1

    for j in dict:
        dict[j]=dict[j]/len(textPom)
    newDict=sorted(dict.items(),key= lambda x: x[1] , reverse=True)
    for i in range(3):
        print(newDict[i])
    probSixThousand=0
    for j in range(6000):
       probSixThousand+=newDict[j][1]
    print("Prawdopodobienstwo 6tys slow: ",probSixThousand)
    print()
    #zad2
    print('--------- ZAD2 ---------')
    ciag=""
    for i in range(100):
        prob=random.uniform(0,1)
        x=generateUsingDict(dict,prob)
        ciag+=x + ' '
    print(ciag)
    print()

    #zad3

    print('--------- ZAD3 ---------')
    dictMain = generateDict(textPom,1,2)

    firstDegreeWordsMarkow=makeMarkowUsingDict(1,5000,dict,dictMain,0)
    avgLenFirst=avgWordLen(firstDegreeWordsMarkow)
    print("Przyblizenie dla zrodla Markowa 1-szego rzedu zaczynajac od pustego tekstu:")
    print(firstDegreeWordsMarkow)
    print("Srednia dlugosc slowa: ", avgLenFirst)
    print()

    secondDegreeWordsMarkow=makeMarkowUsingDict(2,5000,dict,dictMain,0)
    avgLenSecond=avgWordLen(secondDegreeWordsMarkow)
    print("Przyblizenie dla zrodla Markowa 2giego rzedu zaczynajac od pustego tekstu:")
    print(secondDegreeWordsMarkow)
    print("Srednia dlugosc slowa: ", avgLenSecond)
    print()

    secondDegreeWordsMarkowProb= makeMarkowUsingDict( 2, 5000, dict,dictMain, 1)
    avgLenSecondProb = avgWordLen(secondDegreeWordsMarkowProb)
    print("Przyblizenie dla zrodla Markowa 2giego rzedu zaczynajac od slowa 'probability' :")
    print(secondDegreeWordsMarkowProb)
    print("Srednia dlugosc slowa: ", avgLenSecondProb)
    print()


if __name__ == '__main__':
    main()