__author__ = 'bneufeld'

import csv, os, sys
from time import strftime

def print_version_info():
	return "	<!--\n" \
		   "		Generated using Compound Alarm Updater  \n" \
		   "			by Brahm Neufeld at Agrium VPO	  \n" \
		   "			   brahm.neufeld@agrium.com\n" \
		   "	https://github.com/b-neufeld/fox-compound-alarm-updater \n" \
		   "		\n" \
		   "			   Version 0.3 - 2016-05-27		\n" \
		   "	--> \n\n"

def build_beginning_of_xml_file():
	return "<?xml version='1.0' encoding='utf-8'?> \n<DirectAccess>\n\n" + print_version_info()

def build_END_of_xml_file():
	return "</DirectAccess>"

def time_string():
	return strftime("%Y-%m-%d_%I-%M-%S")

	
compound_alarm_groups = [
	'GR1DV1',
	'GR1DV2',
	'GR1DV3',
	'GR1DV4',
	'GR1DV5',
	'GR1DV6',
	'GR1DV7',
	'GR1DV8',
	'GR2DV1',
	'GR2DV2',
	'GR2DV3',
	'GR2DV4',
	'GR2DV5',
	'GR2DV6',
	'GR2DV7',
	'GR2DV8',
	'GR3DV1',
	'GR3DV2',
	'GR3DV3',
	'GR3DV4',
	'GR3DV5',
	'GR3DV6',
	'GR3DV7',
	'GR3DV8'
]
	
def find_data_file(filename):
	if getattr(sys, "frozen", False):
		# The application is frozen
		datadir = os.path.dirname(sys.executable)
	else:
		# The application is not frozen
		# Change this bit to match where you store your data files:
		datadir = os.path.dirname(__file__)

	return os.path.join(datadir, filename)

def compounds_main():
	# define input file and open it
	# it expects a .csv file called Compounds.csv
	my_file = find_data_file("Compounds.csv")
	# open .csv file to dictionary object.
	my_array = csv.DictReader(open(my_file))
	# define output file.
	output_file = 'CAU_'+time_string()+'_output.xml'

	####################################################################################################################
	# start putting together the XML file. s = blank string.
	s = ""
	# headers
	s += build_beginning_of_xml_file()

	####################################################################################################################
	# This needs to be the where all the main action happens 
	# Each row (eg, each Compound) needs a unique filter number, so I am using my_array.line_num to build that
	for row in my_array:
		################################################################################################################
		# put the actual XML on the string.
		################################################################################################################
		# Query Filter needs the following
		# Value= COMPOUND_NAME
		# Condition= NamedLike
		# Filter= FilterX where X = a unique filter for each compound
		s += '\t<QueryFilter Value="'+row['Compound']+'" Condition="NamedLike" Filter="Filter'+str(my_array.line_num)+'" />\n'

		# BlockQueryFilter needs the following
		# Value= COMPOUND_NAME
		# Condition= NamedLike
		# Filter= FilterX where X = a unique filter for each compound
		s += '\t\t<BlockQueryFilter Value="'+row['Compound']+'" Condition="DerivedOrInstantiatedFrom" Filter="Filter'+str(my_array.line_num)+'" />\n'

		# Now for each DEVICE GROUP we need to specify:
		# ParmValue= DEVICE GROUP (eg GR1DV1)
		# ParmName= NAME OF DEVICE TO SEND ALARMS (eg CP2AW3)
		# Filter= FilterX where X = a unique filter for each compound
		for i in range(0, len(compound_alarm_groups)):
			# debug - print the i-value and the associated device group eg. GR1DV1
			# print(str(i)+' '+compound_alarm_groups[i])
			s += '\t\t\t<UpdateCompoundAttribute Filter="Filter'+str(my_array.line_num)+'" ParmValue="'+row[compound_alarm_groups[i]]+'" ParmName="'+compound_alarm_groups[i]+'" />\n'
		s += '\n'

	# footers
	s += build_END_of_xml_file()

	# uncomment to see output of script in command line interface. 
	#print(s)

	# write xml string to output file. 
	with open(output_file,"w") as f:
		f.write(s)

compounds_main()
