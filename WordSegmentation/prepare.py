# -*- coding: utf-8 
def make_dict():
    word_list = []
    words = {}
    file_object = open('../data/words_list')
    try:
        word_list = file_object.readlines()
    finally:
        file_object.close()
    for i in range(len(word_list)):
    	# print word_list[i][:-1].decode('utf-8')
        words[word_list[i][:-1].decode('utf-8')] = 1
    return words