#!/usr/bin/env python

"""
Converts a Turnitin .rbc rubric file into Excel format
"""

import json
import pandas as pd

class parser:

	def parse(self, rbc):
		"""
		Parses rbc file, returning a tidied up dict

		:param rbc: Path to Turnitin .rbc format file
		:type rbc: str, required

		:return data: Parsed data
		:rtype data: dict
		"""

		with open(rbc) as in_handle:
			data = json.load(in_handle)

		# The RubricScale dict within data includes an ID which maps to individual 
		# criteria as well as the name and grade (stored as name and value)

		# First create a dict mapping id to the scale item which is used
		# to create a pd.DataFrame which has the id has column name and contains
		# one row - the name and grade, indexed as 'RubricScale'

		scales = dict()
		for item in data['RubricScale']:
			scales[item['id']] =  [f"{item['name']} ({item['value']})"]
		
		df = pd.DataFrame.from_dict(scales, dtype='string')
		df = df.rename(index={0: 'RubricScale'})

		# Now add an empty row for each criteria ID, also extracting a mapping
		# of ID to criteron name for later use...
		criterion_mapping = dict()
		for item in data['RubricCriterion']:
			df = df.reindex(df.index.values.tolist()+[item['id']])
			criterion_mapping[item['id']] = item['name']

		# Next, iterate through each member of the RubricCriterionScale and
		# update the appropriate cell with the description
		for item in data['RubricCriterionScale']:
			df.at[item['criterion'], item['scale_value']] = item['description']

		# Reset column names to scale values...
		df.columns = df.iloc[0]
		df = df.drop(df.index[0])

		# and reindex to use criterion as index...
		df.rename(index = criterion_mapping, inplace = True)
		
		return(df)
