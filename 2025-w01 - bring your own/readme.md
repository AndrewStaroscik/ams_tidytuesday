# TidyTuesday 2025 Week 1 - bring your own data

## Overview

Time and date of fatal accidents on U.S. Roadways in 2022. Data from the U.S. National Highway Traffic Safety Administration's Fatality Analysis Reporting System (FARS) [2022 data](https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/2022/National/)

## Data prep

The .csv file used is a small subset of the data as the original accident file is 25.2 megabytes. 

The following code was used to create a file with only the columns needed for this visualization: 

``` Python

import pandas as pd

accidentPopTargetCols = ['ST_CASE', 'MONTH', 'DAY', 'HOUR']
df = pd.read_csv('.{path to file}/accident.csv', encoding='utf-8', encoding_errors='ignore', usecols=accidentPopTargetCols, dtype={'STATE': str, 'COUNTY': str})

df.to_csv('../data/2025/accidentSM.csv', index=False)

```

## Chart Description

Heat map showing time and date of a year of fatal accidents. 

Some observations:

* The alternating high and low numbers of accidents along the bottom are likely related to early morning drunk driving, numbers appear to peak around bar closing times and with more accidents occurring later in the week and on the weekends.
* The curved pattern across the top shows variation in accident times that follow changes in daylight inidicating that visibility at and after dusk contributes to the accident rates. 
* Dusk/early evening accidents are more frequent later in the year. 
* New Years Eve shows up as dark areas at the bottom left (morning of Jan 01 2022), and top right (evening of Dec 31 2022).