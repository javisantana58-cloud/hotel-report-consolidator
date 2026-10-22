# Hotel Report Consolidator

A Python script that merges monthly Excel reports from multiple hotel properties into a single consolidated report — automatically.

## The problem it solves

Hotel groups with multiple properties waste hours every month copying and pasting data from separate Excel files. This script does it in seconds.

## How to use it

1. Drop your hotel Excel files into the `datos/` folder
2. Double-click `ejecutar.bat`
3. Check `reporte_consolidado.xlsx` for the results

No coding needed on your end.

## What it generates

- A combined view of all properties in one sheet
- A monthly summary with total revenue and rooms sold across all hotels

## Setup

Requires Python 3 and pandas:

pip install pandas openpyxl
