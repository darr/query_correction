#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : train.py
# Create date : 2019-08-07 18:33
# Modified date : 2019-08-07 19:13
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from pypinyin import lazy_pinyin

def _save_model(data):
    f = open('./model/pinyin2word.model', 'w')
    f.write(str(data))
    f.close()

def build_model():
    word_dict = {}
    count = 0
    for line in open('./data/dict.txt'):
        count += 1
        #print(count)
        line = line.strip().split(' ')
        word = line[0]
        word_count = line[1]
        word_pinyin = ','.join(lazy_pinyin(word))
        if word_pinyin not in word_dict:
            word_dict[word_pinyin] = word + '_' + word_count
        else:
            word_dict[word_pinyin] += ';' + word + '_' + word_count

    data = {}
    for pinyin, words in word_dict.items():
        tmp = {}
        for word in words.split(';'):
            word_word = word.split('_')[0]
            word_count = int(word.split('_')[1])
            tmp[word_word] = word_count
        data[pinyin] = tmp

    _save_model(data)
