question_b_read = open('qb.txt','r')   

while True:
    word = question_b_read.readline()
    if len(word) == 0:
        break

    if 'snake' in word:
        print(word)
question_b_read.close()



