# coding:utf-8
file_object = open('words.txt')
try:
    all_the_text = file_object.readlines()
finally:
    file_object.close()

file_object = open('words_list','w')
for i in range(len(all_the_text)):
    line = all_the_text[i].split()
    print len(line[0]) > 1
    print len(line[0])
    print line[0]
    if len(line[0]) > 3:
        file_object.write(line[0]+'\n')
file_object.close()
