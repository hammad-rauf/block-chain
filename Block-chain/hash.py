import hashlib


#this function generated hash of parameter passed
def genHash(string):                      
    hash=hashlib.sha256()
    hash.update(string.encode('utf-8'))
    return hash.hexdigest()
