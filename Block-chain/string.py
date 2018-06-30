import copy

# this function split and convert into numerics
def split(string):
    word=""
    word2=""
    flag=False
    for i in string:
        if i==" ":
            flag=True
        elif flag==False:
            word+=i
        else:
            word2+=i
    return word,float(word2)


#removing \n character from the last of every line 
def convertline(string):
    string2=""
    for i in string:
        if i=='\n':
            string2+=""
        else:
            string2+=i
    string=""
    return string2
