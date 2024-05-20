#to open and write to a file 
"""
my_file = open('test.txt', 'w')
my_file.write('Hello, Niggermizu\n')
my_file.write('You fat as f')
my_file.close()

"""
#to open and read a file
reading_file = open('listofname.txt','r')
"""
while True:
    line = reading_file.readline()
    if len(line) == 0 :
        break
    print(line,end = " ")

"""
        
reading = reading_file.readlines()
reading_file.close()
"""
file2  = open('listofname.txt')
result_read = file2.read()
file2.close()
print(result_read)

"""
reading.sort()

new_write = open('sortedlines.txt','w')
for i in reading:
    new_write.write(i)
new_write.close()
 
print(reading)