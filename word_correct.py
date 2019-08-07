#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : word_correct.py
# Create date : 2019-08-07 18:28
# Modified date : 2019-08-07 19:26
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

class WordCorrect:

    def __init__(self):
        self.char_path = './data/char.txt'
        self.model_path = './model/pinyin2word.model'
        self.charlist = [word.strip() for word in open(self.char_path) if word.strip()]
        self.pinyin_dict = self.load_model(self.model_path)

    def load_model(self, model_path):
        f = open(model_path, 'r')
        a = f.read()
        word_dict = eval(a)
        f.close()
        return word_dict

    def edit1(self, word):
        n = len(word)
        return set([word[0:i]+word[i+1:] for i in range(n)] +                     # deletion
                   [word[0:i]+word[i+1]+word[i]+word[i+2:] for i in range(n-1)] + # transposition
                   [word[0:i]+c+word[i+1:] for i in range(n) for c in self.charlist] + # alteration
                   [word[0:i]+c+word[i:] for i in range(n+1) for c in self.charlist])  # insertion
