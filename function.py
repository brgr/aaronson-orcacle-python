#################################################################
#   This function receives a binary sequence. The last 5 digits #
#   of that sequence is considered. The next input bit is then  #
#   saved in [+1 if new bit = 0, +1 if new bit = 1]. From that  #
#   value a prediction about the next bit, knowing the last     #
#   sequence is done.                                           #
#################################################################

import pprint
import numpy as np

def init() -> dict:
    # init the five_grams with all possible 5 digit combinations initialized with [0,0]
    bin_i = []
    for i in range(0, 32):
        bin_i.append(bin(i)[2:].zfill(5))
    five_grams = {}
    for j in range(len(bin_i)):
        five_grams[bin_i[j]] = [0, 0]
    return five_grams


def aaronson(all_input, five_grams: dict):

    # update the five_grams
    last_six = all_input[-6:]
    current_five_gram = five_grams[str(last_six[:5])]
    if int(int(last_six[5])) == 0:
        current_five_gram[0] = current_five_gram[0] + 1
    if int(last_six[5]) == 1:
        current_five_gram[1] = current_five_gram[1] + 1

    #prediction
    if five_grams[str(all_input[-5:])][0]<five_grams[str(all_input[-5:])][1]: #check if for the last sequence more 0 than 1 proceded
        prediction=1

    elif five_grams[str(all_input[-5:])][0]==five_grams[str(all_input[-5:])][1]: #check if it's equally probable
        prediction=np.random.randint(2, size=1)

    else:
        prediction=0

    return five_grams, int(prediction)


prediction = None
five_grams=init()
five_grams, pred = aaronson('10011010101010', five_grams)


pprint.pprint(five_grams)
