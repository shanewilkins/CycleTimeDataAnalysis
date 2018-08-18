# Readme

Shane Wilkins

## Intro

This directory contains the tools I'm building to help NRCS analyze the data provided to us by Accenture.


### Contents

* /rawData  <<< put the Accenture data here so tcr can find it. This folder should contain 255 .xlsx files-one for each state (counting Pacific Island Area as the state of Hawaii) and one for the Caribbean Islands Area.
* /tidyData <<< where tcr will put the tidied data.
* tcr.py <<< a python script to **tidy, convert, and rename** the Accenture data spreadsheets into csv files.
* tidy.sh <<< a bash script to call tcr on every file in /rawData, save an intermediate, tidied csv file to /tidyData, then concatenate everything in tidyData together into one file, called data.csv located in the main directory.
* data.csv <<< the tidied data, all in one big file.
* dataDictionary.md <<< a markdown file that describes the source data.
* license.md <<< the license file for the project--it's public domain.


### Howto

* First, export the individual data tables from the Accenture Access Database as .xslx files, keeping the default naming convention in Access. There should be about 250 of them: one for each state for each week.
* Second, put those data tables into /rawData.
* Third, make import.sh executable by doing <chmod 777 tidy.sh>
* Fourth, run the import script with <./tidy.sh>

### Questions and Answers

* "help! i'm getting some kind of weird error . . . . XLRD? BOF? what?"
  - you've probably got a hidden temporary file in the rawData directory. (Do you have one of the files open in excel? if so close excel.)
  - the bash script tries to feed everything with the xlsx extension into tcr, which will choke on a temporary file.
  - show all files, delete the hidden files (anything in /rawData that starts with a . or a $), and rerun tidy.sh.

* "help! i'm getting an output to the console saying tcr cant find a name."
  - what's happening is that the regex can't parse the string in the created by or modified by field of the underlying spreadsheet. the regex wants to separate the substrings on ' - ' exactly,
  - probably you have somebody whose name isn't formatted right in the system.
  - make sure you don't have names where a letter character rather than a space is touching the hyphen separating the employees name from their location. (internal hyphens in last names should be fine.)
  - also doublecheck that the comma separating the employee's first and last name are there.
  - if you end up having to modify these manually, the error in tcr will tell you which record number in the spreadsheet has the goofy name. filter and sort in excel and just update all the records from that employee at once.
