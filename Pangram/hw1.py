import sys
import array

def hw1( arg1, arg2 ):

        fo = open(arg1, "r")
        f = open(arg2, 'w')
        sentenses = fo.readlines()
        fo.close()

        for inner_list in sentenses:
                isPangram = True
                a = array.array('i',(0 for i in range(0,25)))
        
                for item in inner_list:
                        if ord(item) > 96:
                                if ord(item) < 122:
                                        a[ord(item)-97] = 1

                for character in a:
                        if character == 0:
                                isPangram = False

                if isPangram == True:
                        f.write('true\n')
                else:
                        f.write('false\n')
        f.close()

                
