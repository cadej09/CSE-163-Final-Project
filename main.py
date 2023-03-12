"""
Cade Jeong, Pooja Thorail, Hans Xue
CSE 163 WI 23
Final Project

A file that contains the main method
"""

# import pandas as pd
from data_cleaning import merge_data
import question1


def main():
    merged_df = merge_data()
    question1.clf_model(merged_df)


if __name__ == '__main__':
    main()
