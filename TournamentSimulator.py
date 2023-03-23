# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 03:52:15 2023

@author: Stephen
"""

class TournamentSimulator():
    '''Base class to create any kind of playoff simulator'''

    def __init__(self):
        pass


    def SimulateMatchup(self):
        '''Function to simulate one game'''
        pass
    
    def SimulatePlayoffs(self):
        '''Function to simulate the entire playoffs'''
        pass
    
    def RunSimulation(self, nTrials = 100000):
        '''Function to run playoff simulation nTrials times set at default 100,000'''
        pass