"""
CSE 163 WI23
Cade Jeong, Pooja Thorail, Hans Xu

This file provides testing on the prevalence of work interference
experienced by employees seeking treatment for mental health issues.
"""

from data_cleaning import merge_data
import pandas as pd


def find_most_common_work_interference(dataframe: pd.DataFrame) -> str:
    """
    Returns the level of work interference that occurs most
    often for employees seeking treatment.

    Args:
        dataframe (pd.DataFrame):
            A pandas dataframe containing the relevant columns.

    Returns:
        A string containing the level of work interference
        that occurs most often for employees seeking treatment
    """
    data = dataframe.dropna()
    filtered_data = data[data['treatment'] == 'Yes']
    filtered_data = filtered_data[
        filtered_data['work_interfere'] != 'Not applicable to me'
    ]
    most_common_work_interference = filtered_data['work_interfere'].mode().values[0]

    return most_common_work_interference


def main():
    df = merge_data()
    most_common_work_interference = find_most_common_work_interference(df)
    print(most_common_work_interference)


if __name__ == '__main__':
    main()