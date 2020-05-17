#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:10:14 2020

@author: lilpkstud
"""

import glassdoor_scrapper as gs
import pandas as pd
path = "/Users/lilpkstud/Desktop/github_repo/glassdoor_datascience/chromedriver"


df = gs.get_jobs('social media', 70, False, path, 15)

#df = gs.get_jobs('Canva', 50, False, path, 15)

df.to_csv('sharon_socialMedia.csv', index = False)

