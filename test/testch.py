#! -*- coding:utf-8 -*-
'''
# test jieba
import jieba
seg_list = jieba.cut("�����������廪��ѧ", cut_all = True)
print "Full Mode:", ' '.join(seg_list)

seg_list = jieba.cut("�����������廪��ѧ")
print "Default Mode:", ' '.join(seg_list)
'''

# test chinese txt
