#! -*- coding:utf-8 -*-
'''
# test jieba
import jieba
seg_list = jieba.cut("我来到北京清华大学", cut_all = True)
print "Full Mode:", ' '.join(seg_list)

seg_list = jieba.cut("我来到北京清华大学")
print "Default Mode:", ' '.join(seg_list)
'''

# test chinese txt
