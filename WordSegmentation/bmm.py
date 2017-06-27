# -*- coding: utf-8 -*-
from prepare import *


def get_k_words(text, i, k):
    if i + 1 < k:
        return text[0:i + 1], i + 1
    else:
        return text[i - (k - 1):i + 1], k


def segment_words(text, dict_words, max_len=5):
    seg_words = ""
    i = len(text) - 1
    while i >= 0:
        tmp_words, length = get_k_words(text, i, max_len)
        # print tmp_words.encode("utf-8"),length,i
        tmp_len = 0
        for j in range(length):
            if dict_words.has_key(tmp_words[j:length]):
                seg_words += (tmp_words[j:length] + " ")
                tmp_len = length - j
                break
            if j == length - 1 and not dict_words.has_key(tmp_words[j:length]):
                seg_words += (tmp_words[j:length] + " ")
                tmp_len = length - j
        i = i - tmp_len
    # print seg_words.encode("utf-8")
    return seg_words


def bmm_cut(text):
    seg_words = ""
    dict_words = {}
    dict_words = make_dict()
    seg_words = segment_words(unicode(text, "UTF-8"), dict_words)
    # print seg_words.encode("utf-8")
    words_list = seg_words.strip().split()
    words_list.reverse()
    seg_words = "/".join(words_list)
    return seg_words.encode("utf-8")

def main():
    text = u"我爱自然语言处理"
    print bmm_cut(text)

if __name__ == "__main__":
     main()