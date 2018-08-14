# Readme

Shane Wilkins

## Intro

This directory contains the tools I'm building to help NRCS analyze the data provided to us by Accenture.


### Contents

* /rawData  <<< put the accenture data here so tcr can find it. This folder should contain 255 .xlsx files-one for each state (counting Pacific Island Area as the state of Hawaii) and one for the Caribbean Island area.
* /tidyData <<< where tcr will put the tidied data.
* tcr.py <<< a python script to **tidy, convert, and rename** the Accenture data spreadsheets into csv files.
* tidy.sh <<< a bash script to call tcr on every file in /rawData, save an intermediate, tidied csv file to /tidyData, then concatenate everything in tidyData together into one file, called data.csv located in the main directory.
* data.csv <<< the tidied data, all in one big file.
* dataDictionary.md <<< a markdown file that describes the source data.
* license.md <<< the license file for the project--it's public domain.
* 


### Howto

* First, export the individual data tables from the Accenture Access Database as .xslx files, keeping the default naming convention in Access. There should be about 250 of them: one for each state for each week.
* Second, put those data tables into /rawData.
* Third, make import.sh executable by doing <chmod 777 tidy.sh>
* Fourth, run the import script with <./tidy.sh>
