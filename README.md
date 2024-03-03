# RBC2XL

Converter of exported Turnitin Rubric .rbc files to MS Excel format

Turnitin will export rubrics in it's own .rbc format, which is a JSON based format, however for sharing rubrics with students this is impractical.

This tool reads exported .rbc files and converts them to Excel format. It is written in Python, and binary packages are made available for Windows and MacOS. These don't have the greatest startup speed since they have to unpack a lot of Python libraries before they can run, so installing the native Python code and libraries will result in a faster startup time, but is less convenient.

## Installation

### Windows/MacOS binaries

The Windows and MacOS builds do not require installation - just download the appropriate package from [https://github.com/jamesabbott/rbc2xl/releases](releases) to a convenient location and double-click them to run.

### Native Python Code (MacOS/Linux)

#### Requirements
*  Python 3 (Tested with 3.10 and 3.12.1 on MacOS)
*  pip

1.  Clone this repository and change into the resulting directory

```
git clone https://github.com/jamesabbott/rbc2xl.git
cd rbc2xl
```

or download the tar.gz or zip file from the [https://github.com/jamesabbott/rbc2xl/releases](releases) section, and unpack:

*.tar.gz*
```
tar zxvf v1.0.0.tar.gz
cd 1.0.0
```

*.zip*

```
unzip v1.0.0.zip
cd 1.0.0
```

2.  Install prerequisites

```
pip install -r requirements.txt
```

3. Run it!

*GUI interface*
```
./rbc2xl.py
```

*Command line interface*

```
./rbc2xl-cli.py --help
```

## Usage

*GUI interface*

This hopefully requires little explanation. 

1.  Click the 'Select Rubric' button and navigate to the exported .rbc file. The interface will update to display the path to the selected rubric

2.  Rubrics may have grades without defined criteria resulting in empty columns. These can be removed to just retain the columns containing criteria by select the 'Drop empty columns' option

3.  Click the 'Save' button and navigate to the desired location, then enter a filename to save the Excel format file.

4.  Either repeat with another .rbc file or click 'Exit'

*Command line interface*

N.B. This is only available when the native Python code is installed, not from the Windows/MacOS packages.

Usage information is provided with the '--help' argument:
```
./rbc2xl.py --help
Usage: rbc2xl_cli.py [OPTIONS]

Options:
  -rbc TEXT    Path to Turnitin rbc file  [required]
  -xl TEXT     Path to output excel file  [required]
  -drop_empty  Don't include empty columns in output
  --help       Show this message and exit.
```

The path to the .rbc rubric file should be provided with the `--rbc` argument, and the path to the Excel file to create with `-xl`. Empty columns with no critera defined can be removed by adding the `-drop_empty` argument. i.e.

```
./rbc2xl.py -rbc rubric.rnc -xl converted.xlsx -drop_empty
```

