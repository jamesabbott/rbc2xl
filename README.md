# RBC2XL

Converter of exported Turnitin Rubric .rbc files to MS Excel format

Turnitin will export rubrics in it's own .rbc format, which is a JSON based format, however for sharing rubrics with students this is impractical.

This tool reads exported .rbc files and converts them to Excel format. It is written in Python, and binary packages are made available for Windows and MacOS. These don't have the greatest startup speed since they have to unpack a lot of Python libraries before they can run, so installing the native Python code and libraries will result in a faster startup time, but is less convenient.

## Installation

### Windows/MacOS binaries

The Windows and MacOS builds do not require installation - just download them to a convenient location and double-click them to run.

### Native Python Code (MacOS/Linux)

#### Requirements
*  Python 3 (Tested with 3.10 and 3.12.1 on MacOS)
*  git

1.  Clone this repository

```
git clone https://github.com/jamesabbott/rbc2xl.git

```
2.  Change into the local copy of the repository

```
cd rbc2xl
```
3.  Install prerequisites

```
pip install -r requirements.txt
```

4. Run it!
```
./rbc2xl.py
```

## Usage

This hopefully requires little explanation. 

1.  Click the 'Select Rubric' button and navigate to the exported .rbc file. The interface will update to display the path to the selected rubric

2.  Rubrics may have grades without defined criteria resulting in empty columns. These can be removed to just retain the columns containing criteria by select the 'Drop empty columns' option

3.  Click the 'Save' button and navigate to the desired location, then enter a filename to save the Excel format file.

4.  Either repeat with another .rbc file or click 'Exit'