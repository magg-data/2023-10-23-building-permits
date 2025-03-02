Important files 
-------------------------

* Building_Permits_20231024_saved.zip - original file opened in VS Code on Linux,
  saved, and compressed (read below) (no other modifications)
* Building_Permits_20231024_clean.zip - processed dataset, compressed, 
  will be generated every time when the notebook data-cleanup.ipynb is run
  if the file is not present.
* Building_Permits_20231024_cost_csv.zip - The file generated by
  building-permits.ipynb that is the base for results presentations in file
  building-permits-dash.ipynb
* csv_descr.csv - the description of the fields in the main dataset
* diff.log - the log of differences between the files Building_Permits_20231024.csv
  and Building_Permits_20231024_saved.csv

2023-11-27
-----------------

Building_Permits_20231024_saved.zip is a compressed csv file that was created
by opening the original csv file in VS Code on Linux and then saved.

Before the conversion, when the cleaned-up dataframe was written to a file 
and read from the file, there was a warning about mixed-type fields in certain 
columns. It was because some rows were shifted. 

After closer inspection, it occurs that there are lines in the original file
that contain CR which are in the middle of the "", that confuses the pd.read_csv()
that it is a new line. The lines typically end with LF in the original file. Those
CR in the middle of "" break the line. After opening and saving it in VS Code,
those characters are changed to LF.

The file diff.log contains the complete log of the bash diff showing the 
affected lines and places. The example is shown below:

$ diff Building_Permits_20231024.csv Building_Permits_20231024_saved.csv 
63361c63361,63362
< 6474377-CN,Single Family/Duplex,Residential,Building,New,"Construct west single family residence, per plan. (Establish use as and construct 2 sin.",,0,1,"180,255",2015-05-18,2016-01-20,2017-07-20,2017-03-07,Completed,,509 26TH AVE S,SEATTLE,WA,98144,,https://cosaccela.seattle.gov/portal/customize/LinkToRecord.aspx?altId=6474377-CN,47.59779122,-122.29922708,"(47.59779122, -122.29922708)"
---
> 6474377-CN,Single Family/Duplex,Residential,Building,New,"Construct west single family residence, per plan. (Establish use as and construct 2 single family residences). Review and processing for 2 A/P's under 6461513
> .",,0,1,"180,255",2015-05-18,2016-01-20,2017-07-20,2017-03-07,Completed,,509 26TH AVE S,SEATTLE,WA,98144,,https://cosaccela.seattle.gov/portal/customize/LinkToRecord.aspx?altId=6474377-CN,47.59779122,-122.29922708,"(47.59779122, -122.29922708)"
....



Note
----------
Trying to convert the end of line from Windows to Linux with the command:

$ tr -d 'r' < ../../src/Building_Permits_20231024.csv > Building_Permits_20231024_lin.csv

did not work because pandas complains about missing ExpiresDate column. So 
I stayed with the above solution.


