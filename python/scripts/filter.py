#/usr/bin/python
#_*_ coding:utf-8 _*_

import os
import os.path
import random
import uuid
import datetime

def getfiles(path, *exclude, *filelset):
    ''' 
    params:
        - path : source files path
        - exclude : exclude files path
        - fileset : those need to translate
    '''
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            if child in exclude:
                continue
            else:
                getfiles(child, exclude, *fileset)
        else:
            print(child)
            fileset.append(child)

if __name__ == "__main__":
    path = "/Users/air/opt/python/image_filter"
    codepath = "/Users/air/Documents/" 
    exclude = ["/Users/air/opt/python/image_filter/非政治人物"]
    angle = [0, 90, 180, 270]
    n = len(angle)
    percent = 0.5
    prefix = "政治敏感_"
    fileset = []
    partitions = []
    getfiles(path, exclude, fileset)
    print("========================")
    print(len(fileset))
    b_list = range(0,len(fileset))
    num = int(len(fileset) * percent)
    roset=random.sample(b_list, num)
    step = num/n
    for i in range(n-1):
        partitions.append(roset[i*step:i*step+step])
    else:
        partitions.append(roset[i*step+step:])

    print("总共文件:" + str(num))
    for i in range(len(partitions)):
        for n in range(len(partitions[i])):
            print(fileset[partitions[i][n]])
            filetype = fileset[partitions[i][n]].split('.')[-1]
            outpath = codepath + prefix + datetime.date.today().strftime('%m%d') + '_' + str(str(angle[i])) + '/'
            print("源文件：" + fileset[partitions[i][n]])
            print("生成文件：" + outpath)
            if os.path.exists(outpath) == False:
                os.popen('mkdir -p ' + outpath)
            cmd='convert ' + fileset[partitions[i][n]] + ' -rotate ' + str(angle[i]) + ' '  + outpath + str(uuid.uuid1()) + '.' + filetype
            os.popen(cmd)
