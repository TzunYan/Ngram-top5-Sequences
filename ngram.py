from string import maketrans
from nltk.util import ngrams
name = raw_input('請輸入檔名: ')
fh = file(name+'.txt', 'r')
myDict = {}
index = 0
n = int (raw_input('請輸入N值: '))
i = 0
intab = "!@#$~`$%^&*()_+=?><,./*\-[]{}\""
outtab = "                              "
trantab = maketrans(intab, outtab)
while True:
    line = fh.readline()
    if line == '':
        break
    else:
        i+=1
        #print i
        #print line.translate(trantab).split()
        sixgrams = ngrams(line.translate(trantab).split(), n)
    for grams in sixgrams:
        if grams in myDict:
            myDict[grams][0] += 1
            myDict[grams].append(i) 
        else:
            myDict[grams]=[1, i]
dict = sorted(myDict.iteritems(), key=lambda d:d[1], reverse = True)
print "The top-5 sequences :\n"+str(dict[0])+"\n"+str(dict[1])+"\n"+str(dict[2])+"\n"+str(dict[3])+"\n"+str(dict[4])
fh.close()
