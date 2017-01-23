# -*- coding: utf-8 -*-  
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')  

import os
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

'''
Learning from https://github.com/fyuanfen/wordcloud
However, it cant't work, so modify it.
'''

stopwords = {}

def importStopword(filename=''):
    global stopwords
    #f = open(filename, 'r', encoding='utf-8')
    f = open(filename, 'r')
    line = f.readline().rstrip()

    while line:
        stopwords.setdefault(line, 0)
        #stopwords[line] = 1
        stopwords[line.decode('utf-8')] = 1
        line = f.readline().rstrip()

    f.close()

def processChinese(text):
    seg_generator = jieba.cut(text)  # 使用结巴分词，也可以不使用

    seg_list = [i for i in seg_generator if i not in stopwords]

    seg_list = [i for i in seg_list if i != u' ']

    seg_list = r' '.join(seg_list)

    return seg_list


importStopword(filename='./stopwords.txt')


# 获取当前文件路径
# __file__ 为当前文件, 在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)

# old code
# text = open(path.join(d, 'love.txt'),encoding ='utf-8').read()

# new code
text = open(path.join(d, 'futest.txt')).read()

# 如果是中文
text = processChinese(text)#中文不好分词，使用Jieba分词进行

# read the mask / color image
# taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
# 设置背景图片
back_coloring = imread(path.join(d, "./image/gift3.jpg"))

wc = WordCloud( font_path='./font/jiankai.ttf',#设置字体
                background_color="white", #背景颜色
                max_words=588,# 词云显示的最大词数
				#stopwords=STOPWORDS.add("短信"),
                mask=back_coloring,#设置背景图片
                #max_font_size=400, #字体最大值
                random_state=42,
                )
# 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
wc.generate(text)

# 从背景图片生成颜色值
image_colors = ImageColorGenerator(back_coloring)

# 普通展示，词颜色随机
#plt.figure()
#plt.imshow(wc)
#plt.axis("off")
#plt.show()

# 以词背景颜色作为基础颜色展示
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor

#plt.figure()
#plt.imshow(image_colors, cmap=plt.cm.gray)
#plt.axis("off")
#plt.show()

plt.figure()
plt.imshow(wc.recolor(color_func=image_colors), cmap=plt.cm.gray)
plt.axis("off")
plt.show()

'''
# 原始代码展示3张图片
# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
'''
# 保存图片
wc.to_file(path.join(d, "./mine/gift3_out_1.jpg"))