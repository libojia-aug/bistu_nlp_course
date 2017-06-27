# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from fmm import fmm_cut
from bmm import bmm_cut

file_object = open('../data/1/1.txt')
try:
    all_text = file_object.readlines()
finally:
    file_object.close()

file_object_w_fmm = open('../output/1_fmm.txt', 'w')
file_object_w_bmm = open('../output/1_bmm.txt', 'w')

for i in range(len(all_text)):
    file_object_w_fmm.write(fmm_cut(all_text[i]).decode('utf-8') + '\n')
    file_object_w_bmm.write(bmm_cut(all_text[i]).decode('utf-8') + '\n')
    if i > 2:
        break
file_object_w_bmm.close()
file_object_w_fmm.close()
