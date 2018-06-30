from files import *
class Publicledger:
  
    obj = None

    def ____init__(self):
        self.__no_of_transactions=0
        self.__amount=25000.982
        self.fileName="record.txt"
        file=open(self.fileName,"x") #main ledger files which keeps public key of user
        file.close()
        #this function is called every time a user is made 
        #this function updates the public ledger file which keeps the public key of every user
        

    def NewUser(self,publicKey):        
        if not self.verify(publicKey):
            file=open(self.fileName,"a")     
            file.write(publicKey)               #updating public ledger file
            file.write("\n")
            file.close()
        else:
            return False
    def getFileName(self):
        return self.fileName
    def verify(self,PK):
        file=open(self.fileName,"r")
        str=""
        while True:
            str=file.readline();
            if str=="":
                break
            str=convertline(str)
            if PK==str:
                return True
        return False

    @staticmethod
    def create(self):
        if(Publicledger.obj == None):
            Publicledger.obj = Publicledger()
            Publicledger.obj.____init__()
            return Publicledger.obj
        else:
            return Publicledger.obj

