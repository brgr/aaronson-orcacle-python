#################################################################
#   This function receives a binary sequence. The last 5 digits #
#   of that sequence is considered. The next input bit is then  #
#   saved in [+1 if new bit = 0, +1 if new bit = 1]. From that  #
#   value a prediction about the next bit, knowing the last     #
#   sequence is done.                                           #
#################################################################

import pprint

def aaronson(input):

    #init the database with all possible 5 digit combinations initialized with [0,0]
    bin_i=[]
    for i in range(0,32):
        bin_i.append(bin(i)[2:].zfill(5))
    database= {}
    for j in range(len(bin_i)):
        database[bin_i[j]] = [0,0]


    #update the database
    last_six = input[-6:]
    sequence = last_six[:5]
    print(str(sequence))
    print(str(last_six[5]))
    if int(last_six[5]) == 0:
        database[str(sequence)][0]+=1
        print("it was a 0")
    if int(last_six[5]) == 1:
        database[str(sequence)][1]+=1
        print("it was a 1")


    return database

database = aaronson('10011010101010')
pprint.pprint(database)
