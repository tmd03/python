scoreDic = {'kor':85, 'eng':90, 'mat':92, 'sci':79, 'his':82}

uri = 'c:/pythontxt/'
for key in scoreDic.keys():
    with open(uri + 'score_dictionary.txt', 'a') as f:
        f.write(key + '\t: ' + str(scoreDic[key]) + '\n')