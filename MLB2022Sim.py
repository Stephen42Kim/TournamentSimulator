# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 04:17:37 2023

@author: Stephen
"""

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import TournamentSimulator as ts

class MLB2022Simulator(ts.TournamentSimulator):
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
    
    driver.get('https://www.baseball-reference.com/leagues/majors/2022-team-pitching-staffs.shtml')
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 1500);")
    
BuildDataset(2022)



## Pulls a single table from a url provided by the user.
## The desired table should be specified by tableID.
## This function is used in all functions that do more complicated pulls.
def pullTable(url, tableID):
    res = requests.get(url)
    ## Work around comments
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("", res.text), 'lxml')
    tables = soup.findAll('table', id = tableID)
    data_rows = tables[0].findAll('tr')
    data_header = tables[0].findAll('thead')
    data_header = data_header[0].findAll("tr")
    data_header = data_header[0].findAll("th")
    game_data = [[td.getText() for td in data_rows[i].findAll(['th','td'])]
        for i in range(len(data_rows))
        ]
    data = pd.DataFrame(game_data)
    header = []
    for i in range(len(data.columns)):
        header.append(data_header[i].getText())
    data.columns = header
    data = data.loc[data[header[0]] != header[0]]
    data = data.reset_index(drop = True)
    return(data)
## For example:
## url = "http://www.baseball-reference.com/teams/KCR/2016.shtml"
## pullTable(url, "team_batting")

url = "https://www.baseball-reference.com/leagues/majors/2022-team-pitching-staffs.shtml"
pullTable(url, "pitchers")


url = "http://www.baseball-reference.com/teams/KCR/2016.shtml"
pullTable(url, "team_batting")