from string import *

#this function update all files
def update_AllFiles(file,P,A):
    A=str(A)
    f=open(file,"r")
    line=f.readline()
    line=convertline(line)
    count=0
    #this will open every file and update them with transaction
    while True:
        if line=="":
            break
        file2=open(line+".txt","a")
        file2.write(P+" "+A+'\n')
        line=f.readline()
        line=convertline(line)

#this function copy old transactions to new created user's file
def copyAll(file,P):
    f=open(file,"r")
    f2=open(P+".txt","a+")
    line=f.readline()
    line=convertline(line)
    f3=open(line+".txt","r")
    while True:
        lin2=f3.readline()
        if lin2=="":
            break
        lin2=convertline(lin2)
        f2.write(lin2+'\n')
        


