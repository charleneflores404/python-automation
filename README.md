## Build Executable

Make sure pyinstaller is installed on your computer.

```bash
pip install pyinstaller
```

### News Automation

Go to the folder containing the `3_news_automation.py` script. Run the following command:

```bash
pyinstaller --onefile 3_news_automation.py
```

### Excel Report

Go to the folder containing the `6.py_to_exe.py` script. Run the following command:

```bash
pyinstaller --onefile 6.py_to_exe.py
```

Then, move the exe file from dist to the same folder as the py script.

## Description

### Table Extraction

1. Extract table from pdf and save to a csv file
1. Extract table from website
1. Extract csv from website

### Automate the News

Webscraping for getting headlines of the football news. This saves you time from having to check the website and look at the cluttered UI with ads.

1. Manual (launches the driver)
1. Headless (runs in the background)
1. Automated, scheduled every morning

### Excel Report

Automating data manipulation and writing Excel sheets using Python.

1. Creating a pivot table from raw Excel file
2. Creating a chart from the pivot table data
3. Applying formulas and writing into a new Excel file
4. Applying formatting styles to cells
5. Creating one file that does 1-4
6. Make the script ready to be converted to en executable

---

---

Following freeCodeCamp's YouTube [tutorial video](https://youtu.be/PXMJ6FS7llk) by Frank Andrade aka PyCoach
