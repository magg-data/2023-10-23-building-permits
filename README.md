# Description

Clients want to remodel the house. They want to gather preliminary information 
about how much it costs, how long it takes and whether there are Seattle 
areas that are more expensive than others. Clients are interested in 
modification, or demolition, of their residential dwelling. Clients are 
interested in fairly recent projects, i.e., within last two years.

1. How much does it cost?
2. How long does it take from start to completion?
3. Are there areas in Seattle that are more expensive than others?

# Data source

[Seattle Department of Construction and Inspections, 2023.](https://data.seattle.gov/Permitting/Building-Permits/76t5-zqzr)

# Outcome

The following files were created during this project:

## Notebooks

* *data-cleanup.ipynb* - the notebook describing and performing the process of 
  cleaning the data to solve the business task. 
  It uses *Building_Permits_20231024_saved.zip* and produces 
  *Building_Permits_20231024_clean.zip* 
* *building-permits.ipynb* - exploratory analysis based on cleaned data; 
  running this notebook produces *Building_Permits_20231024_cost.csv.zip* 
  which is used by the notebook presenting the results
* *building-permits-dash.ipynb* - the presentation of the results

## Datasets

* *Building_Permits_20231024_saved.zip* - original file opened in VS Code on Linux,
saved, and compressed (read below) (no other modifications)
* *csv_descr.csv* - the description of the fields in the main dataset
* *Building_Permits_20231024_clean.zip* - processed dataset, compressed, 
  will be generated every time when the notebook data-cleanup.ipynb is run
  if the file is not present.
* *Building_Permits_20231024_cost.csv.zip* - the dataset produced by the exploratory
  analysis notebook - *building-permits.ipynb*

## Presentation Files

These are *.ipynb exported to HTML

* *data-cleanup.html* - exported *data-cleanup.ipynb* 
* *building-permits.html* - exported *building-permits.ipynb*
* *building-permits-dash.html* - exported *building-permits-dash.ipynb*

```bash
# to export to html without python code
jupyter nbconvert yourNotebook.ipynb --no-input --to html
```
