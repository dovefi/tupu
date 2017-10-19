import datetime
import os
import sys

def getday(n,dformat):
    ''' get formard date '''
    today = datetime.date.today()
    oneday = datetime.timedelta(days=n)
    return (today - oneday).strftime(dformat)


def getdaylist(n,dformat):
    ''' return formard date list '''
    datelist = []
    for i in range(n):
        datelist.append(getday(i,dformat))
    return datelist

def getfilelist(path):
    ''' return files list without dir and files start with .'''
    dirs = os.listdir(path)
    result = []
    for i in range(len(dirs)):
        if dirs[i].startswith('.') != True and os.path.isfile(path+'/'+dirs[i]):
            result.append(dirs[i])
    return result

def getdirlist(path):
    ''' return dir list without dir and files start with .'''
    dirs = os.listdir(path)
    result = []
    for i in range(len(dirs)):
        if dirs[i].startswith('.') != True and os.path.isdir(path+'/'+dirs[i]):
            result.append(dirs[i])
    return result

if __name__ == "__main__":
    print("today is :", datetime.date.today().strftime('%m%d'))
