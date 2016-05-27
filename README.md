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
- FCS 5.0.0.0 (this is the earliest version this has been tested on) 

# Instructions
