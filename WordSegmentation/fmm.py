# -*- coding: utf-8 -*-
from prepare import *


def getSeg(text):
    word_dict = make_dict()

    if not text:
        return ''

    if len(text) == 1:
        return text

    if text in word_dict:
        return text
    else:
        small = len(text) - 1
        text = text[0:small]
        return getSeg(text)


def fmm_cut(text, max_len=5):
    text = unicode(text, "UTF-8").strip()
    str_len = len(text)
    result_str = []
    i = 0
    while text:
        tmp_str = text[0:max_len]
        seg_str = getSeg(tmp_str)
        seg_len = len(seg_str)
        if seg_str.strip():
            result_str.append(seg_str)
        text = text[seg_len:]
    return "/".join(result_str)


def main():
    test_str = u"我爱自然语言处理"
    print fmm_cut(test_str)

if __name__ == '__main__':
    main()
