#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:44:57 2020

@author: lilpkstud
"""

import glassdoor_scrapper as gs
import pandas as pd
path = "/Users/lilpkstud/Desktop/github_repo/glassdoor_datascience/chromedriver"


df = gs.get_jobs('project manager', 15, False, path, 15)

