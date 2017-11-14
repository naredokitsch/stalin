# -*- coding: utf-8 -*-
"""
 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
Created on Sat Feb 27 02:12:58 2016
puzzle.py
15 Puzzle implementation

Artificial Intellence 1766
Engineering Faculty
UNAM

@author: Stan (stalinmunoz@yahoo.com)
"""
from functools import reduce
import random

seq = list(range(0,16))

actions = ['E','W','N','S']

x_mask = lambda i: 15<<(4*i)

extract = lambda i,c: (c&(x_mask(i)))>>(4*i)

e_most = lambda z: (z%4)==3

w_most = lambda z: (z%4)==0

n_most = lambda z: z<=3

s_most = lambda z:z>=12

valid_moves = {i:list(filter(lambda action:\
((not action=='E') or (not e_most(i))) and \
((not action=='W') or (not w_most(i))) and \
((not action=='S') or (not s_most(i))) and \
((not action=='N') or (not n_most(i))),actions)) for i in seq}

def move_east(puzzle):
    if(not e_most(puzzle.zero)):
        puzzle.zero += 1;
        mask = x_mask(puzzle.zero)
        puzzle.configuration = \
        (puzzle.configuration&mask)>>4 | \
        (puzzle.configuration&~mask)

def move_west(puzzle):
    if(not w_most(puzzle.zero)):
        puzzle.zero -= 1;
        mask = x_mask(puzzle.zero)
        puzzle.configuration = \
        (puzzle.configuration&mask)<<4 | \
        (puzzle.configuration&~mask)

def move_north(puzzle):
    if(not n_most(puzzle.zero)):
        puzzle.zero -= 4;
        mask = x_mask(puzzle.zero)
        puzzle.configuration = \
        (puzzle.configuration&mask)<<16 | \
        (puzzle.configuration&~mask)

def move_south(puzzle):
    if(not s_most(puzzle.zero)):
        puzzle.zero += 4;
        mask = x_mask(puzzle.zero)
        puzzle.configuration = \
        (puzzle.configuration&mask)>>16 | \
        (puzzle.configuration&~mask)

class Puzzle:

    def __init__(self, parent=None, action =None, depth=0):
        self.parent = parent
        self.depth = depth
        if(parent == None):
            self.configuration =  \
                reduce(lambda x,y: x | (y << 4*(y-1)), seq)
            self.zero = 15
        else:
            self.configuration = parent.configuration
            self.zero = parent.zero
            if(action != None):
                self.move(action)

    def __str__(self):
        return '\n'+''.join(list(map(lambda i:\
        format(extract(i,self.configuration)," x")+\
        ('\n' if (i+1)%4==0 else ''),seq)))+'\n'

    def __repr__(self):
        return self.__str__()

    def __eq__(self,other):
        return (isinstance(other, self.__class__)) and \
        (self.configuration==other.configuration)

    def __ne__(self,other):
        return not self.__eq__(other)
        
    def __lt__(self,other):
        return self.depth < other.depth

    def __hash__(self):
        return hash(self.configuration)

    def move(self,action):
        if(action =='E'):
            move_east(self)
        if(action =='W'):
            move_west(self)
        if(action =='N'):
            move_north(self)
        if(action =='S'):
            move_south(self)
        return self


    @staticmethod
    def to_list(puzzle):
        return [extract(i,puzzle.configuration) for i in seq]

    def shuffle(self,n):
        for i in range(0,n):
            self.move(random.choice(valid_moves[self.zero]))
        return self

    def expand(self):
        #filtering the path back to parent
        return list(filter(lambda x: \
        (x!=self.parent), \
        [Puzzle(self,action,self.depth+1) \
        for action in valid_moves[self.zero]]))

