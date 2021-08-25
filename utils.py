from os import path as Path

def debug(info, message):
    print('['+info+']'+' --> ' + message)

def isExistDir(path):
    return Path.exists(path)

def isDir(path):
    return Path.isdir(path)
