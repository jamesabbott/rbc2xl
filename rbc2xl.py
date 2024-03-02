#!/usr/bin/env python

"""
GUI interface for rbc to excel conversion
"""

from rbc_parse import parser
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from sys import platform

class gui:
	"""gui class to defined the interface"""

	def __init__(self) -> None:
		self.rbc_path = None # Path to .rbc rubric
		self.xl_path = None # Path to write excel file
		self.drop_empty = tk.BooleanVar() # Should columns without criteria be dropped

	def browse_rbc(self) -> None:

		"""
		File chooser to select .rbc file.
		Updates self.rbc_path with path to selected file, updates displayed 
		path to selected file and enables save button once selection made
		"""

		f_path = askopenfilename(initialdir=".",
			title="Select File", filetypes=[("Rubric files","*.rbc")])
		
		if f_path != "":
			self.rbc_path = f_path

		if self.rbc_path is not None:
			save_button.configure(state = 'active')
			selected.configure(text = f"Selected file: {self.rbc_path}")

	def convert(self) -> None:

		"""
		Carries out conversion using rpc_parse.parser(), writing out 
		resulting dataframe as an excel file.

		If the 'drop empty columns checkbox is checked, carries out 
		drop prior to saving file.
		"""

		f_path = asksaveasfilename(initialdir=".",
			title="Select File", filetypes=[("Excel files","*.xlsx")])
		self.xl_path = f_path

		p = parser()
		df = p.parse(self.rbc_path)

		if self.drop_empty.get() == True:
			df.dropna(axis = 1, how = 'all', inplace = True)

		df.to_excel(self.xl_path, header = True, index = True)

def exit() -> None:
	window.destroy()


# Build the interface...
if platform.startswith('win'):
	but_width = 14
	font_size = 10
else:
	but_width = 20
	font_size = 14

window = tk.Tk()
window.title('rbc2xl')
interface = gui()

drop_empty = tk.IntVar()

rbc_button  = tk.Button(window, width = but_width, text = "Select rubric", 
						font = ("Roboto", font_size), command = interface.browse_rbc)

save_button = tk.Button(window, width = but_width, text = "Save", 
						font = ("Roboto", font_size), state = 'disabled', command = lambda: interface.convert())

exit_button  = tk.Button(window, width = but_width,text = "Exit", 
						 font = ("Roboto", font_size), command = lambda: exit())

selected = tk.Label(text = f"Selected file: {interface.rbc_path}")

var = tk.BooleanVar()
drop_check = tk.Checkbutton(text = 'Drop empty columns', variable = var, offvalue = False, onvalue = True)
interface.drop_empty = var

rbc_button.grid( row = 0, column = 0, padx = 10, pady = 2, sticky = 'W')
drop_check.grid( row = 0, column = 1, padx = 10, pady = 2, sticky = 'W')
selected.grid(   row = 1, column = 0, padx = 10, pady = 2, sticky = 'W', columnspan = 2)
save_button.grid(row = 2, column = 0, padx = 10, pady = 2, sticky = 'W')
exit_button.grid(row = 2, column = 1, padx = 10, pady = 2, sticky = 'W')

window.mainloop()