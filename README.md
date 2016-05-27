# WORK IN PROGRESS

# fox-compound-alarm-updater
For the Foxboro DCS. Take a spreadsheet of Compounds and alarm groups and turn it into a DirectAccess .xml file for quick updating. 

# What is it? 
Compound Alarm Updater helps a programmer make bulk changes to Compound Alarm Groups on Foxboro I/A. 

Using DirectAccess, the programmer can generate a .csv file of all Compounds, manipulate device groups (and other compound parameters like DESCRP) in Excel or equivalent, then use Compound Alarm Updater to quickly build a DirectAccess .xml file to deploy those changes to their FCS (Galaxy server)

# Example use case
You buy a new Foxboro workstation for your control room. It arrives with a new letterbug. You have 200 unique compounds on your Foxboro I/A control system, and now you have to manually edit them all with the letterbug of your new workstation. 

No more! With Compound Alarm Updater, you can open up Compounds.csv in Excel and add the letterbug of the new workstation to any compounds required. Then, run Compound Alarm Updater to generate a DirectAccess .xml script. Run that script, deploy changes to your compounds, and you're done. What might have taken hours before has now taken you under 30 minutes. 

# Requirements 
- Python 2.7.11 (https://www.python.org/downloads/release/python-2711/) installed on a NON-FOXBORO computer. I do not recommend installing unsupported software on Foxboro engineering stations. 
- FCS 5.0.0.0 (minimum). Has been tested all the way to FCS 6.1. 
- A working knowledge of DirectAccess (see document B0750BM)

# Instructions
1. Make a .cab file backup of your Galaxy server. It is advisable to do this before executing ANY DirectAccess script that modifies your Galaxy database. 
2. Open DirectAccess on your Galaxy and run the script generate_csv_export.xml. This will (as the name implies) generate a .csv export of everything in your Galaxy, to the folder D:\ExportFiles
3. When complete, navigate to D:\ExportFiles and copy the file Compounds.csv to a computer where you have installed Python 2.7
4. Open Compunds.csv in Excel. Before starting to make changes, clean up the .csv file to show only the columns we care about (steps follow). 
5. In Compounds.csv: Zoom out and select all used cells and rows with your mouse - do NOT "Select all". 
6. In Compounds.csv: Right click on the selected cells and Copy. 
7. In Compounds.csv: On a new worksheet, right click in cell A1 and click Paste Transpose. 
8. In Compounds.csv: With the transposed data, Select All, then click the button to "Sort A to Z". We are making sure that the compound block's parameters are in order, alphabetically. 
9. 
# to be comtinued
