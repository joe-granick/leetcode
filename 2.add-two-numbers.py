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
        p, q = l1, l2
        l3 = ListNode()
        head = l3

        while p or q or r:
        # logic for calculating new sum and determining carryover
           p_val = p.val if p else 0
           q_val = q.val if q else 0
           l3_val = p_val + q_val + r
           
           r = l3_val//10
           l3_val = l3_val%10
           
           l3.next = ListNode(l3_val)

           l3 = l3.next
           p=p.next if p else None
           q=q.next if q else None

          

        return head.next

# @leet end
