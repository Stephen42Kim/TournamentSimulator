# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 04:17:37 2023

@author: Stephen
"""

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import TournamentSimulator

class MLB2022Simulator(TournamentSimulator):
    '''Class to simulate MLB 2022 Playoff scenario'''
    
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
    

def BuildDataset(year):
    '''Function that builds dictionaries for the national and american league playoff
    teams. Extract data from baseball-reference.com'''
    
    with open('https://www.baseball-reference.com/leagues/majors/2022-team-pitching-staffs.shtml') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        
    print(soup)