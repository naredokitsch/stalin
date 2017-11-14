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
  
August 2017  
    
rubik.py

3x3x3 Rubik's cube implementation

Artificial Intellence 1766
Engineering Faculty
UNAM
Mexico

@author: Stan (stalinmunoz@yahoo.com)
"""
"""
Encoding use in this class:

    ABC
    DEF
    GHI
JKL MNÑ OPQ RST
UVW XYZ abc def
ghi jkl mnñ opq
    rst
    uvw
    xyz

000 White
001 Green
010 Red
011 Blue
100 Cian (Orange not available in terminal)
101 Yellow
"""
from functools import reduce
from termcolor import colored
from random import choice
from itertools import product
#color identifiers
W = 0;
G = 1;
R = 2;
B = 3;
C = 4;
Y = 5;

color_map = {
    0:"white",
    1:"green",
    2:"red",
    3:"blue",
    4:"cyan",
    5:"yellow"}

# Encoding with maps is less eficient but is more legible
#
# Letter code : (block location, color)
code = {
    'A' : (0,W),
    'B' : (3,W),
    'C' : (6,W),
    'D' : (9,W),
    'E' : (12,W),
    'F' : (15,W),
    'G' : (18,W),
    'H' : (21,W),
    'I' : (24,W),
    'J' : (27,G),
    'K' : (30,G),
    'L' : (33,G),
    'M' : (36,R),
    'N' : (39,R),
    'Ñ' : (42,R),
    'O' : (45,B),
    'P' : (48,B),
    'Q' : (51,B),
    'R' : (54,C),
    'S' : (57,C),
    'T' : (60,C),
    'U' : (63,G),
    'V' : (66,G),
    'W' : (69,G),
    'X' : (72,R),
    'Y' : (75,R),
    'Z' : (78,R),
    'a' : (81,B),
    'b' : (84,B),
    'c' : (87,B),
    'd' : (90,C),
    'e' : (93,C),
    'f' : (96,C),
    'g' : (99,G),
    'h' : (102,G),
    'i' : (105,G),
    'j' : (108,R),
    'k' : (111,R),
    'l' : (114,R),
    'm' : (117,B),
    'n' : (120,B),
    'ñ' : (123,B),
    'o' : (126,C),
    'p' : (129,C),
    'q' : (132,C),
    'r' : (135,Y),
    's' : (138,Y),
    't' : (141,Y),
    'u' : (144,Y),
    'v' : (147,Y),
    'w' : (150,Y),
    'x' : (153,Y),
    'y' : (156,Y),
    'z' : (159,Y)    
}

# blank spaces
BLANK = ' '*6
# chr(FILL) character
FILL = 9608
# repeat cube
K = 2
    
actions = [
# x axis
[
    [('A','g'),('B','U'),('C','J'),('Q','A'),('c','B'),
     ('ñ','C'),('z','Q'),('y','c'),('x','ñ'),('g','z'),
     ('U','y'),('J','x'),('R','T'),('S','f'),('T','q'),
     ('d','S'),('f','p'),('o','R'),('p','d'),('q','o')],
#    [('D','h'),('E','V'),('F','K'),('P','D'),('b','E'),('n','F'),
#     ('w','P'),('v','b'),('u','n'),('h','w'),('V','v'),('K','u')],
    [('G','i'),('H','W'),('I','L'),('O','G'),('a','H'),
     ('m','I'),('t','O'),('s','a'),('r','m'),('i','t'),
     ('W','s'),('L','r'),('M','j'),('N','X'),('Ñ','M'),
     ('Z','N'),('l','Ñ'),('k','Z'),('j','l'),('X','k')]
],\
# y axis
[
    [('A','q'),('D','f'),('G','T'),('M','A'),('X','D'),
     ('j','G'),('r','M'),('u','X'),('x','j'),('T','x'),
     ('f','u'),('q','r'),('J','g'),('K','U'),('L','J'),
     ('U','h'),('W','K'),('g','i'),('h','W'),('i','L')],
#    [('B','p'),('E','e'),('H','S'),('N','B'),('Y','E'),('k','H'),
#     ('s','N'),('v','Y'),('y','k'),('p','s'),('e','v'),('S','y')],
    [('C','o'),('F','d'),('I','R'),('Ñ','C'),('Z','F'),
     ('l','I'),('t','Ñ'),('w','Z'),('z','l'),('o','t'),
     ('d','w'),('R','z'),('O','Q'),('P','c'),('Q','ñ'),
     ('a','P'),('c','n'),('m','O'),('n','a'),('ñ','m')]
],\
# z axis
[
    [('J','R'),('K','S'),('L','T'),('M','J'),('N','K'),
     ('Ñ','L'),('O','M'),('P','N'),('Q','Ñ'),('R','O'),
     ('S','P'),('T','Q'),('G','A'),('H','D'),('I','G'),
     ('F','H'),('C','I'),('B','F'),('A','C'),('D','B')],
#    [('U','d'),('V','e'),('W','f'),('X','U'),('Y','V'),('Z','W'),
#     ('a','X'),('b','Y'),('c','Z'),('d','a'),('e','b'),('f','c')], 
    [('g','o'),('h','p'),('i','q'),('j','g'),('k','h'),
     ('l','i'),('m','j'),('n','k'),('ñ','l'),('o','m'),
     ('p','n'),('q','ñ'),('r','x'),('s','u'),('t','r'),
     ('u','y'),('w','s'),('x','z'),('y','w'),('z','t')]
]]

# computed only once
initial_conf = reduce(lambda x,y:(x[0]|(y[1]<<y[0]),0), \
[(0,0)]+[v for k,v in code.items()])[0]

class RubikPuzzle:
    def __init__(self,parent = None,action=None,depth=0,pattern=None):
        self.parent = parent
        self.depth = depth
        if parent != None and action!=None:
            #initialize configuration from parent
            self.configuration = parent.configuration
            self.apply(action)
        elif pattern!=None:
            self.configuration = self.initialize(pattern)
        else:
            self.configuration = initial_conf
            
    def initialize(self,pattern):
        # configuration as a map {letter:color_code}
        return reduce(lambda x,y:x|y,\
        [val<<(code[key][0]) for key,val in pattern.items()])
            
    def cube(self,symbol):
        n = code[symbol][0]
        return \
        colored(chr(FILL),color_map[(((7<<n)&self.configuration)>>n)])*2
        
    def apply(self,action):
        # action tuple (axis,row,direction)
        #right to left turn
        if(action[2]==0):
            moved,mask = reduce(lambda x,y:(x[0]|y[0],x[1]|y[1]),\
            [self.move(x) for x in actions[action[0]][action[1]]])
        else: #left to right turn
            moved,mask = reduce(lambda x,y:(x[0]|y[0],x[1]|y[1]),\
            [self.move((b,a)) for a,b in actions[action[0]][action[1]]])
        self.configuration = moved | \
        ((((2<<162)-1)^mask)&self.configuration)
                
    def move(self,locations):
        # move from i to j on a vector of ones
        i = code[locations[0]][0]
        j = code[locations[1]][0]
        #returns the moved block and mask in a tuple
        return (((((7<<i)&self.configuration)>>i)<<j),(7<<i)|(7<<j))
        
            
    def __str__(self):
        return (
        BLANK+self.cube('A')+self.cube('B')+self.cube('C')+'\n'+
        BLANK+self.cube('D')+self.cube('E')+self.cube('F')+'\n'+
        BLANK+self.cube('G')+self.cube('H')+self.cube('I')+'\n'+
        self.cube('J')+self.cube('K')+self.cube('L')+
        self.cube('M')+self.cube('N')+self.cube('Ñ')+
        self.cube('O')+self.cube('P')+self.cube('Q')+  
        self.cube('R')+self.cube('S')+self.cube('T')+'\n'+
        self.cube('U')+self.cube('V')+self.cube('W') +
        self.cube('X')+self.cube('Y')+self.cube('Z') +
        self.cube('a')+self.cube('b')+self.cube('c')+ 
        self.cube('d')+self.cube('e')+self.cube('f') +'\n'+        
        self.cube('g')+self.cube('h')+self.cube('i')+
        self.cube('j')+self.cube('k')+self.cube('l') +
        self.cube('m')+self.cube('n')+self.cube('ñ')+ 
        self.cube('o')+self.cube('p')+self.cube('q') +'\n'+                
        BLANK+self.cube('r')+self.cube('s')+self.cube('t')+'\n'+
        BLANK+self.cube('u')+self.cube('v')+self.cube('w')+'\n'+
        BLANK+self.cube('x')+self.cube('y')+self.cube('z')+'\n' )
        
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
        
    def pattern_equals(self,pattern,target=initial_conf):
        mask = RubikPuzzle.get_pattern_mask(pattern)
        return ((mask&self.configuration)^(mask&target))==0
        
    @staticmethod
    def get_pattern_mask(pattern):
        return reduce(lambda x,y:x|y,[(7<<code[letter][0])\
        for letter in pattern])
        
    def shuffle(self,n):
        for i in range(0,n):
#            self.apply((choice([0,1,2]),choice([0,1,2]),choice([0,1])))
            self.apply((choice([0,1,2]),choice([0,1]),choice([0,1])))
            
    def expand(self):
        #filtering the path back to parent
        return list(filter(lambda x: \
        (x!=self.parent), \
        [RubikPuzzle(self,action,self.depth+1) \
#        for action in product([0,1,2],[0,1,2],[0,1])]))
        for action in product([0,1,2],[0,1],[0,1])]))