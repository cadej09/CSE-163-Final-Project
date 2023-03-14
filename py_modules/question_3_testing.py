"""
CSE 163 WI23
Cade Jeong, Pooja Thorail, Hans Xu

This file contains a function that creates a testing to find value of
specified age_group and their count of treatment answer 'yes'.
to test whether the question_3.py file is producing the correct result as
expected
"""
import pandas as pd


def treatment_count_in_group(df: pd.DataFrame, group: str) -> int:
    """
    Given a pandas DataFrame of survey responses and a string representing an
    age group, this function returns the number of individuals in that
    age group who received treatment for their mental health.

    Args:
        df (pd.DataFrame): A pandas DataFrame of survey responses.
        group (str): A string representing an age group in the format
            '(min_age, max_age]'.

    Returns:
        The number of individuals in the specified age group who received
        treatment for their mental health.
    """
    # Filter data for individuals who received treatment
    data = df[df['treatment'] == 'Yes'][['Age', 'treatment']].dropna()
    data = data[(data['Age'] >= 15) & (data['Age'] < 80)]

    # Define the age bins
    bins = [15, 18, 22, 29, 39, 49, 59, 69, 79]

    # Create the age groups
    data['age_group'] = pd.cut(data['Age'], bins=bins).astype(str)

    # Group by age group and get counts for each treatment group
    grouped_data = data.groupby(['age_group',
                                 'treatment']).size().reset_index(name='count')

    # Get the count for the specified age group
    count = grouped_data[(grouped_data['age_group'] == group) &
                         (grouped_data['treatment'] == 'Yes')]['count'].values

    return count[0]
