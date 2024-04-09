# -*- coding: utf-8 -*-
"""analyze_rms_csv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PJ10uv8PS1cR2A-CYW8oYO9oE2Flu56g
"""

import pandas as pd
import numpy as np
import glob

def calculate_curve_rms(time_series, value_series):
    trapezoid_areas = 0.5 * (time_series.diff().fillna(0) * (value_series + value_series.shift().fillna(0)))
    total_area = trapezoid_areas.sum()
    return np.sqrt(total_area)

def find_max_rms_curve(file_path):
    df = pd.read_csv(file_path, skiprows=1)
    df = df.dropna(axis=1, how='all')

    max_rms = 0
    max_rms_element = None

    for column in df.columns[1:]:
        rms = calculate_curve_rms(df['time'], df[column])
        if rms > max_rms:
            max_rms = rms
            max_rms_element = column

    element_no = max_rms_element.split('@')[1].strip()
    return 3 * max_rms, element_no

def analyze_rms_csv(directory_path='*.csv'):
    files = glob.glob(directory_path)
    results = []

    for file in files:
        triple_rms, element = find_max_rms_curve(file)
        results.append((file, triple_rms, element))

    comparison_df = pd.DataFrame(results, columns=['File', '3xRMS', 'Element'])
    return comparison_df

# 這樣，您就可以直接調用analyze_csv_files函式來分析當前目錄中的所有CSV檔案
# 例如：
# result_df = analyze_csv_files()
# print(result_df)