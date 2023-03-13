"""
This file contains a function that creates a test df that can be used
to test whether the question_2.py file is producing the correct result as
expected
"""
import pandas as pd


def question_2_testing_df() -> pd.DataFrame:
    """
    This function creates a testing dataframe for research question 2
    """
    import pandas as pd
    # create dictionary with column names and data
    data = {
        'wellness_program': ['Yes', 'No', 'Yes', 'Don\'t know', 'No'],
        'care_options': ['I am not sure', 'No', 'Yes', 'No', 'I am not sure'],
        'benefits': ['Yes', 'Don\'t know', 'No', 'No', 'Don\'t know'],
        'mental_health_interview': ['No', 'No', 'Yes', 'Yes', 'No'],
        'coworkers': ['Maybe', 'No', 'Yes', 'Yes', 'Maybe'],
        'supervisor': ['Yes', 'No', 'Yes', 'No', 'Maybe'],
        'year': [2016, 2014, 2016, 2019, 2016]
    }
    # create DataFrame from dictionary
    df = pd.DataFrame(data)
    return df
