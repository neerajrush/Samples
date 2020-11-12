#!/usr/bin/python3

import csv, sys
import os
import json

def read_csv_as_json(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        try:
            field_names = reader.fieldnames
            print(field_names)
            result = ""
            for row in reader:
                if 'count' in row:
                    x = row['count']
                    row['count'] = int(x)
                result += json.dumps(row, indent=4, sort_keys=False) + ","
            result = "[" + result[:len(result)-1] + "]"
            jsonFile = filename.replace(".csv", ".json")
            with open(jsonFile, 'w') as jFile:
                jFile.write(result)
                jFile.close()
            print("Created Json file: ", jsonFile)
            print("---")
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

if __name__ == "__main__":
    dir_name = "Test-CSV-Data"
    files = os.listdir(dir_name)
    csv_files = []
    for f in files:
        if not ".zip" in f and ".csv" in f:
            filename = dir_name + "/" + f
            print("Reading CSV  file: ", filename)
            read_csv_as_json(filename)
