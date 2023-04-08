# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 23:43:10 2023

@author: tabis
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/tabis/OneDrive - Swinburne University/Semester I - 2023/Easter break_Project/ds_salary_proj/chromedriver_win32/chromedriver.exe"
df = gs.get_jobs("data scientist", 5, False, path, 5)
df