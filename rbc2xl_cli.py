#!/usr/bin/env python

"""
Converts a Turnitin .rbc rubric file into Excel format
"""

import click
from rbc_parse import parser

@click.command()
@click.option('-rbc',required = True, help = "Path to Turnitin rbc file")
@click.option('-xl', required = True, help = "Path to output excel file")
@click.option('-drop_empty', is_flag = True, help = "Don't include empty columns in output")

def main(rbc, xl, drop_empty):

	p = parser()
	df = p.parse(rbc)

	if drop_empty:
		df.dropna(axis = 1, how = 'all', inplace = True)
	df.to_excel(xl, header = True, index = True)

if __name__ == "__main__":
	main()