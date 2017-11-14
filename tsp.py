# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:11:57 2016

@author: stan
"""
from environment import Environment
import numpy as np
import matplotlib.pyplot as plt
class TSP(Environment):
    def __init__(self,n=10,interactive=False):
        self.n = n
        self.interactive = interactive
        
        #generate random cities
        self.cities = np.random.uniform(size=(n,2))
        if(interactive):
            plt.ion()
        
    def evaluate(self,population):
        for individual in population.individuals:
            individual.fitness = 1/self.compute_cost(individual.phenotype)
        
    def decode(self,population):
        return
        
    def get_chromosome_length(self):
        return self.n   
        
    def compute_cost(self,permutation):
        n = len(permutation)
        M = self.cities[permutation,:]        
        return np.sum(np.sqrt(np.sum(\
        (M-M[[i%n for i in range(1,n+1)],:])**2,axis=1)))
        
    @staticmethod
    def compute_distance(individual1,individual2):
        return np.count_nonzero(individual1.phenotype-individual2.phenotype)
        
    def compute_normalized_distance(self,individual1,individual2):
        return TSP.compute_distance(individual1,individual2)/self.n
        
    def show(self,population,colors='blue',clear=False):
        if(clear):
            plt.clf()
        best = min(population.individuals,\
        key=lambda i:self.compute_cost(i.phenotype))
        M = self.cities[best.phenotype,:]
        X = M[[i%self.n for i in range(0,self.n+1)],0]
        Y = M[[i%self.n for i in range(0,self.n+1)],1]
        plt.scatter(X,Y,color = 'red',marker="o")
        plt.plot(X,Y,color=colors)
        plt.title('best individual, cost='+\
        str(self.compute_cost(best.phenotype)))
            
        plt.grid()
        if(self.interactive):
            plt.pause(0.05)
        else:
            plt.show()
        