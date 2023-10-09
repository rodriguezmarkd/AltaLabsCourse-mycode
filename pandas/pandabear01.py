#!/usr/bin/python3

import pandas as pd

def main():
    excel_file = 'movies.xls'

    movies = pd.read_excel(excel_file)

    print(movies.head())

    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)

    print(movies_sheet1.head())

    movies_sheet1.head(5).to_excel("5movies.xlsx")

    movies_sheet1.head(5).to_json("5movies.json")

    movies_sheet1.head(5).to_csv("5movies.csv")


if __name__ == "__main__":
    main()
