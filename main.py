"""
Cade Jeong, Pooja Thorail, Hans Xue
CSE 163 WI 23
Final Project

A file that contains the main method
"""

import pandas as pd
from data_cleaning import merge_data
import question1


def main():
    merged_df = merge_data()
    data = merged_df[['Age', 'self_employed', 'family_history',
                      'no_employees', 'tech_company', 'wellness_program',
                      'treatment']].dropna()
    features = data.loc[:, data.columns != 'treatment']
    features = pd.get_dummies(features)
    labels = data['treatment']
    question1.dtc_model(features, labels)
    question1.rfc_model(features, labels)


if __name__ == '__main__':
    main()
