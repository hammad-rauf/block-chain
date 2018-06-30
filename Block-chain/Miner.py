from string import *
from files import update_AllFiles
import hashlib

class miner:
    def __init__(self,publicLedger_File_Name):
        self.File=publicLedger_File_Name


    #this function validates the transaction and then perform it
    #this function validates the transaction and then perform it
    def transac(self,S_PublicKey,Amount,R_PublicKey):
        Amount=float(Amount)
        if(self.__exits(S_PublicKey,R_PublicKey)):
            file=open(self.File,"r")
            flag=True
           
            while True:
                line=file.readline()                    
                if(line==""):
                    break
                line=convertline(line)
                count=0
                file2=open(line+".txt","r")
                while True:
                    line=file2.readline()
                    if line=="":
                        if count <Amount:
                            flag=False
                        break
                    line=convertline(line)
                    p,a=split(line)
                    if(p==S_PublicKey):         #if transaction of either public key found
                        count+=a
                if flag==False:
                    return False
            update_AllFiles(self.File,S_PublicKey,Amount*-1)            #subtracting from senders amount
            update_AllFiles(self.File,R_PublicKey,Amount)               #adding to recivers amount
            return True
        return False            

                    


    def __exits(self,S_public,R_Public):
        #this function verifies both sender and reciever whether they exists in our system or not
        count=0
        file=open(self.File,"r")
        while True:
            line=file.readline()
            line=convertline(line)
            if(""==line):
                break
            else:
                if line==S_public or line==R_Public:            
                    count+=1
        if count==2:
            return True
        return False



