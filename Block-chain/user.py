from hash import genHash
from files import *
import copy
from PublicLedger import Publicledger
import Miner

class user:
    def __init__(self,Name,Password,obj,Miner1):            #aggregation of Miner and Public Ledger
        self.__privateKey=genHash((Password))           #assuming name and password together will make it unique
        self.__publicKey=genHash(Name)                      #assuming name as unique attributes
        self._Amount=198.392
        obj.NewUser(self.__publicKey)                       #update public ledger
        #creating a file with the name of user's public key
        self._file=open((self.__publicKey+".txt"),"x+")     #user ledger file which will keep record of all the transactions
        self.__name=Name                                    #to compare public key later
        self._Miner_Obj=Miner1
        self._file.close()
        #copying all old files
        copyAll(obj.getFileName(),self.__publicKey)
        #this function will make first transaction into user
        #this will add 198.392 amount in new user amount
        update_AllFiles(obj.getFileName(),self.__publicKey,self._Amount)
    def getName(self):
        Name=self.name.copy()
        return Name
    def getPublicKey(self):
        PK=self.__publicKey.copy()
        return PK
    def getAmount(self):
        return self._Amount
    #this function authenticates user identity then call miner's transaction function which authenticates transaction"""
    def maketransaction(self):
        password = input('enter your password:')
        password=genHash(password)
        if(password==self.__privateKey):                #compares private key of user with generated private key
            amount=input('enter amount to be transafered:')
            pk=input('enter Name of reciever:')
            pk=genHash(pk)                                  #generate public's key to which amount needs to be transfered
            if self._Miner_Obj.transac(self.__publicKey,amount,pk):
                self._Amount-=amount
        else:
            print("Wrong Password")




    

        



