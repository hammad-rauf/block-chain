from PublicLedger import Publicledger
from Miner import miner
from user import user


PL=Publicledger.create(Publicledger)


mminer=miner(PL.getFileName())
user1=user("Zohaib","zohaib007",PL,mminer)
user2=user("hammad","lololol",PL,mminer)
user3=user("Sunil","kothari",PL,mminer)
user4=user("haider","sheikh",PL,mminer)

user1.maketransaction()
user2.maketransaction()



