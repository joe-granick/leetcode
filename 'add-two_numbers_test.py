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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        r=0 # initialize remainder value to carryover if sum >10
        ##### note this may not be necessary as if set up right the residual can just 
        l1_val, l2_val = l1.val, l2.val
        l3 = ListNode()
        while l1 or l2:
        # logic for calculating new sum and determining carryover
           l3_val = l1_val + l2_val + r
           if l3_val>10: r = l3_val/10
           else:         r = 0
           l3_val%=10
           l3.val = l3_val

        # generate new node with new value

        # move l1 and l2 to next nodes and repeat
     
           if not l1.next: 
            l1_val = 0
           else: 
            l1 = l1.next
            l1_val = l1.val
           if not l2.next: 
            l2_val = 0
           else: 
            l2 = l2.next
            l2_val = l2.val

           l3.next = ListNode()
           l3 = l3.next
        
        if r !=0:
           l3.next = ListNode(r)
           l3 = l3.next
        return l3

# @leet end
