question_a_read = open('qa.txt','r')
word = question_a_read.readlines()
word.reverse()
question_a_read.close()

question_a_write = open('qa2.txt','w')
for x in word:
    question_a_write.write(x)
question_a_write.close()

print(word)