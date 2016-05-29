# WORK IN PROGRESS

# fox-compound-alarm-updater - What is it? 
Compound Alarm Updater helps a programmer make bulk changes to Compound Alarm Groups on Foxboro I/A. 

Using DirectAccess, the programmer can generate a .csv file of all Compounds, manipulate device groups (and other compound parameters like DESCRP) in Excel or equivalent, then use Compound Alarm Updater to quickly build a DirectAccess .xml file to deploy those changes to their FCS (Galaxy server)

# Example use case
You buy a new Foxboro workstation for your control room. It arrives with a new letterbug. You have 200 unique compounds on your Foxboro I/A control system, and now you have to manually edit them all with the letterbug of your new workstation. 

No more! With Compound Alarm Updater, you can open up Compounds.csv in Excel and add the letterbug of the new workstation to any compounds required. Then, run Compound Alarm Updater to generate a DirectAccess .xml script. Run that script, deploy changes to your compounds, and you're done. What might have taken hours before has now taken you under 30 minutes. 

# Requirements 
- Python 2.7.11 (https://www.python.org/downloads/release/python-2711/) installed on a NON-FOXBORO computer. I do not recommend installing unsupported software on Foxboro engineering stations. 
- FCS 5.0.0.0 (minimum). Has been tested all the way to FCS 6.1. I have not tested it on 4.x and below (but it may work). 
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
9. In Compounds.csv: Once again, select all used cells/rows but do NOT "Select All". Right click and copy. 
10. In Compounds.csv: On a third worksheet, once again Paste Transpose. You should now have a Compound in each row (in order alphabetically), and Compound Parameters as rows sorted alphabetically left-to-right. 
11. In Compounds.csv: Delete ALL columns EXCEPT for "Compound", "GR1DVx", "GR2DVx", "GR3DVx". Optionally, you can keep columns like DESCRP and CINHIB if you want to modify those fields. 
12. In Compounds.csv: Your file should now be cleanly sorted and ready to modify. Delete any rows (Compounds) that you do not want to modify. Take advantage of Excel's conditional formatting and find-and-replace functions to set up all of your Compound Alarm Groups as your DCS requires. 
13. When complete, save the active worksheet as *Compounds.csv*. This must be the filename; it is what the script looks for to build the DirectAccess .xml file. 
14. Put Compunds.csv in the same folder as Compounds.py. Shift-right-click in that folder with Windows Explorer and select "Open Command Prompt Here". 
15. Type the path to python.exe, followed by Compounds.py to run the script. For example: "C:\Python27.python.exe Compounds.py"
16. The script will output an .xml file named CAU_2016-05-27_04-59-10_output.xml (current date & time will be substituted). Copy this file over to your Galaxy server. 
17. Open DirectAccess and run the CAU_2016-05-27_04-59-10_output.xml file. This will modify your Galaxy database. When DirectAccess is finished, any Compounds that you had included in your Compounds.csv file will have had their alarm groups updated. 
18. The final step is to review and deploy the changes to your Compounds. The DirectAccess script modifies your Galaxy, but it WILL NOT AUTOMATICALLY DEPLOY COMPOUNDS TO CONTROLLERS WHEN IT EXECUTES. 

# Examples
See example input and output files:
* example_Compunds.csv (rename to Compunds.csv and you can verify the output is identical to the example .xml file)
* example_CAU_2016-05-27_05-09-28_output.xml

# Tips
- B0750BM is a great reference if you need more details on DirectAccess. 
- If you want to validate the script before making changes in bulk, manually copy & edit the .xml file to modify just one compound. 
- If you have Excel installed on your 6.0.1+ Galaxy, I think this functionality is built-in with the Grid Editor feature. 
- This might seem like a lot of effort, but if you add or modify workstations a few times a year, this can save a ton of time (depending on how many compounds you have).
- 
# Feedback
I'd love to hear feedback on if this script saves you time. If you need help, submit an "issue" on Github. I can't guarantee a quick response. The Foxboro freelist is also a great reference.
