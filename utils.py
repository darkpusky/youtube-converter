from os import path as Path

def debug(info, message):
    print('['+info+']'+' --> ' + message)

def isExistDir(path):
    return Path.exists(path)

def isDir(path):
    return Path.isdir(path)

def isNotSingle(array): #Ritorna true se c'è almeno un elemento nella lista
    return len(array) >= 1 #False se l'array è vuoto

def formatDuration(sec):
    hours = sec // 3600
    sec = sec - hours * 3600
    minutes = sec // 60
    sec = sec - minutes * 60
    if hours > 0:
        return addZeros(hours) + ":" + addZeros(minutes) + ":" + addZeros(sec)
    else:
        return addZeros(minutes) + ":" + addZeros(sec)

        
def addZeros(n):
    if n < 10:
        return "0" + str(n)
    return str(n)
