# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @leet imports end

# @leet start
class Trie:

    def __init__(self):
        self.keys = {}
        

    def insert(self, word: str) -> None:
        curr_char = ""
        dict = self.keys
        i = 0

        while i < len(word):
            curr = word[i]
            if curr not in dict: break
            dict = dict[curr]
            i+=1
        
        # loop through remaining characters and add tree node for each
        for _ in range(i, len(word)-1):
            curr = word[_]
            dict.insert({curr: {}}) # insert current character as key with empty treen node
            dict = dict[curr] 
        
        # add asterisk to indicate this prefix is a complete word
        if "*" not in dict: dict.insert('*')



    def search(self, word: str) -> bool:
        for s in word:

        if key = "*": return True


        

    def startsWith(self, prefix: str) -> bool:
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @leet end
