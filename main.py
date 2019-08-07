#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-07 18:29
# Modified date : 2019-08-07 18:48
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from query import query_item
from train import build_model

def run():
    build_model()
    query_item()

run()
