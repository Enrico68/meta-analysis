import os
import sys
import md5
import random



def getsubSystemVersion(*args):
    if sys.platform.startswith('win'):
        return 'EPUBCONV1'
    elif sys.platform == 'darwin':
        return 'EPUBCONV2'
    else:
        return 'EPUBCONV3'

def getIntVal(vals):
    return ord(vals)		

VERSION = "9.5.3"
GLOBAL_APP_NAME = 'EPUB Converter'



def usage():
	print "AniceSoft {} v{} - kEYGEN".format(GLOBAL_APP_NAME, VERSION)
	print


def GenerateSN(myname):
    #input = mykey
    text = md5.new(GLOBAL_APP_NAME + '_@_' + getsubSystemVersion() + '_@_' + myname).hexdigest().upper()
    #print "Text is {}".format(text)
    groupA = None
    groupB = None
    groupC = None
    groupD = None
    dellAll = 0
    cmpSect = ''
    groupA = (220 + getIntVal(text[0]) * getIntVal(text[1])) % 255
    groupB = getIntVal(text[2]) * getIntVal(text[13]) % 255
    groupB ^= 255
    groupC = getIntVal(text[3]) * getIntVal(text[4]) % 255
    groupC ^= 255
    cmpSect = ''
    cmpSect = cmpSect + '%02X' % groupA
    cmpSect = cmpSect + '%02X' % groupB
    cmpSect = cmpSect + '%02X' % groupC
    cmpSect = cmpSect + '00'
    #print "{} must be {}".format(input[0:6],cmpSect[0:6])
    part1 = cmpSect[0:6]
    #if input[0:6] != cmpSect[0:6]:
    #    raise Exception()
    #f1 = int(input[6:8])
    #print "f1 is {}".format(f1)
    #print "text5 is {} and formatted {}".format(text[5],getIntVal(text[5]))
    #print "Caluclation result1: {}".format((getIntVal(text[5]) + f1) % 10)
    #print "Caluclation result2: {}".format((getIntVal(text[5]) - f1) % 10)
    if (getIntVal(text[5]) + (getIntVal(text[5])+1)) % 10 == 1:
	    part2 = getIntVal(text[5]) + 1
    if (getIntVal(text[5]) - (getIntVal(text[5])-1)) % 10 == 1:
	    part2 = getIntVal(text[5]) - 1
    #if (getIntVal(text[5]) + f1) % 10 != 1 and (getIntVal(text[5]) - f1) % 10 != 1:
    #    raise Exception()
    dellAll = abs(groupA + groupB * groupC)
    groupA = (dellAll + getIntVal(text[14]) * getIntVal(text[7])) % 255
    groupB = (dellAll + abs(getIntVal(text[7]) - getIntVal(text[8]))) % 255
    groupB ^= 255
    groupC = int(dellAll + 100.0 * getIntVal(text[10]) / getIntVal(text[12])) % 255
    cmpSect = ''
    cmpSect = cmpSect + '%02X' % groupA
    cmpSect = cmpSect + '%02X' % groupB
    cmpSect = cmpSect + '%02X' % groupC
    cmpSect = cmpSect + '00'
    #print "{} must be {}".format(input[9:15],cmpSect[0:6])
    part3 = cmpSect[0:6]
    #if input[9:15] != cmpSect[0:6]:
    #    raise Exception()
    #f1 = int(input[15:17])
    #print "f1 is {}".format(f1)
    #print "text11 is {} and formatted {}".format(text[11],getIntVal(text[11]))
    #print "Caluclation result1: {}".format((getIntVal(text[11]) + f1) % 10)
    #print "Caluclation result2: {}".format((getIntVal(text[11]) - f1) % 10)
    if (getIntVal(text[11]) + (getIntVal(text[11])+9)) % 10 == 9:
	    part4 = getIntVal(text[11])+9
    if (getIntVal(text[11]) - (getIntVal(text[11])-9)) % 10 == 9:
	    part4 = getIntVal(text[11])-9
    #if (getIntVal(text[11]) + f1) % 10 != 9 and (getIntVal(text[11]) - f1) % 10 != 9:
    #    raise Exception()
    dellAll += abs(groupA - groupB + groupC)
    groupA = (dellAll + getIntVal(text[9]) * getIntVal(text[10])) % 255
    groupB = abs(getIntVal(text[1]) - getIntVal(text[2])) % 255
    groupC = abs(int(500 + 100.0 * dellAll / getIntVal(text[13]) * getIntVal(text[15]) - getIntVal(text[0]))) % 255
    groupC ^= 255
    cmpSect = ''
    cmpSect = cmpSect + '%02X' % groupA
    cmpSect = cmpSect + '%02X' % groupB
    cmpSect = cmpSect + '%02X' % groupC
    cmpSect = cmpSect + '00'
    #print "{} must be {}".format(input[18:24],cmpSect[0:6])
    part5 = cmpSect[0:6]
    #if input[18:24] != cmpSect[0:6]:
    #    raise Exception()
    #f1 = int(input[24:26])
    #print "f1 is {}".format(f1)
    #print "text14 is {} and formatted {}".format(text[14],getIntVal(text[14]))
    #print "Caluclation result1: {}".format((getIntVal(text[14]) + f1) % 10)
    #print "Caluclation result2: {}".format((getIntVal(text[14]) - f1) % 10)
    if (getIntVal(text[14]) + (getIntVal(text[14])+3)) % 10 == 3:
	    part6 = getIntVal(text[14])+3
    if (getIntVal(text[14]) - (getIntVal(text[14])-3)) % 10 == 3:
	    part6 = getIntVal(text[14])-3
    #if (getIntVal(text[14]) + f1) % 10 != 3 and (getIntVal(text[14]) - f1) % 10 != 3:
    #    raise Exception()
    serial = "Serial: {}{}{}{}{}{}{}{}{}".format(part1,part2,random.randint(0,9),part3,part4,random.randint(0,9),part5,part6,random.randint(0,9))
    print serial
    return True
	
if __name__ == "__main__":
    usage()
    if len(sys.argv) == 1:
        name = raw_input('Enter Name: ')
        GenerateSN(name)
    else:
        #print "0: %s " % sys.argv[0:]
		#print "1: %s " % sys.argv[1:]
		#print "2: %s " % sys.argv[2:]		
        name=sys.argv[1]
        print "Name: {}".format(name)
        GenerateSN(name);
		#key=sys.argv[2];
		#CompareSN(name,key)
		#extract(unicode(sys.argv[1]))
    waitkey = raw_input('')
		
