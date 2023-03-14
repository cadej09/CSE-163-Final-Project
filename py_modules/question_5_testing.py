"""
CSE 163 WI23
Cade Jeong, Pooja Thorail, Hans Xu

This file tests the question:
    'How does the state ofresidence impact the likelihood of
    seeking mental health treatment?'
It tests to see what state has the most number of
participants seeking treatment
"""

from data_cleaning import merge_data
import pandas as pd


def find_max_state(dataframe: pd.DataFrame) -> str:
    """
    Returns the state with the most number of participants
    saying yes to treatment.

    Args:
        dataframe (pd.DataFrame):
            A pandas dataframe containing the relevant columns.

    Returns:
        A string containing the state with the most
        number of participants seeking treatment
    """
    data = dataframe.dropna()
    map_data = data[['state', 'treatment']]
    map_data['treatment'] = map_data['treatment'].replace({
        'Yes': 1,
        'No': 0
    }).values

    map_data = map_data.groupby('state')['treatment'].sum().reset_index()
    max_treatment_state = map_data.loc[map_data['treatment'].idxmax()]['state']

    return max_treatment_state

