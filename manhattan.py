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
    
Created on Sun Feb 28 10:09:57 2016
manhattan.py
Manhattan distance implementation

Artificial Intellence 1766
Engineering Faculty
UNAM

@author: Stan (stalinmunoz@yahoo.com)
"""
from puzzle import Puzzle
from puzzle import seq

row = lambda i: i//4
col = lambda i: i%4

class ManhattanDistance:
    
    def __init__(self,target = Puzzle()):
        self.target =target
        self.locations =self._find_locations(target)
        self.distances = self._precompute_distances(self.locations)
        
    def _find_locations(self,puzzle):
        locations = [None]*16
        for i in enumerate(Puzzle.to_list(puzzle)):
            locations[i[1]] = i[0]
        return locations
        
    def _precompute_distances(self,locations):
       distances = [[0]*16 for i in seq]
       for i in seq:
           for j in seq:
               distances[i][j] = abs(row(j)-row(locations[i]))+ \
               abs(col(j)-col(locations[i]))
       return distances
       
    def distance_to_target(self,puzzle):
        #zero's location is not considered in the sum
        return sum(map(lambda i:self.distances[i[0]+1][i[1]],\
        enumerate(self._find_locations(puzzle)[1:])))       
               
           
          
           
        
    