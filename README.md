* # **Analyze RMS in CSV Files**

This Python module, `analyze_rms_csv.py`, is designed to process multiple CSV files to find the curve with the maximum Root Mean Square (RMS) value. It calculates the RMS value for every curve within each CSV file and identifies the curve with the highest RMS value. It then returns the tripled RMS value along with the corresponding element identifier.

* # **Installation**

No additional installation is required except for the standard Python libraries used in the script, which are `pandas`, `numpy`, and `glob`. Ensure these are installed by running:


```bash
!pip install pandas numpy
```

* # **Usage**
To use this module, simply import the analyze_rms_csv function from the script and pass the directory path containing your CSV files as an argument. Here's a quick example:

```bash
from analyze_rms_csv import analyze_rms_csv
analyze_rms_csv()
```





