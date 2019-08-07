#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : query.py
# Create date : 2019-08-07 18:37
# Modified date : 2019-08-07 19:23
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from word_correct import WordCorrect
from pypinyin import lazy_pinyin

def query_word(word):
    print(word)
    corrector = WordCorrect()
    word_pinyin = ','.join(lazy_pinyin(word))
    candiwords = corrector.edit1(word)
    #print(candiwords)
    #print(word_pinyin)
    print(corrector.pinyin_dict.get(word_pinyin, 'na'))

def query_item():
    word = '我门'
    query_word(word)
    word = '田安门'
    query_word(word)
    word = '你好'
    query_word(word)
    word = '中国'
    query_word(word)
    word = '美国'
    query_word(word)
