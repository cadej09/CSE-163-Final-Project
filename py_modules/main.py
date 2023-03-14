"""
CSE 163 WI23
Cade Jeong, Pooja Thorail, Hans Xu

A file that contains the main method which runs all of our testing
functions at once
"""

import pandas as pd
from data_cleaning import merge_data
from cse163_utils import assert_equals
from question_2 import employer_support, employee_comfortable
from question_2_testing import question_2_testing_df
from question_3_testing import treatment_count_in_group
from question_5_testing import find_max_state
from question_6_testing import most_common_work_interference

def test_question_2(df: pd.DataFrame, df_expected: pd.DataFrame) -> None:
    """
    This function compares the expected updated dataframe and the actual
    updated dataframe.

    Args:
        df: pandas DataFrame, this is the actual updated df
        df_expected: pandas DataFrame, this is the expected df

    Return:
        None.
    """
    assert_equals(df, df_expected)


def test_question_3(df) -> None:
    assert_equals(771, treatment_count_in_group(df, '(29, 39]'))

def test_question_5(df) -> None:
    assert_equals('CA', find_max_state(df))

def test_question_6(df) -> None:
    assert_equals('Often', most_common_work_interference(df))


def main():
    # Test Question 2
    df_2 = question_2_testing_df()
    employer_support(df_2)
    employee_comfortable(df_2)
    expected_output = {
        'wellness_program': [10, 0, 10, 2, 0],
        'care_options': [2, 0, 10, 0, 2],
        'benefits': [10, 2, 0, 0, 2],
        'mental_health_interview': [10, 10, 0, 0, 10],
        'coworkers': [4, 0, 10, 10, 4],
        'supervisor': [10, 0, 10, 0, 6],
        'year': [2016, 2014, 2016, 2019, 2016],
        'support_score': [22, 2, 20, 2, 4],
        'comfortable_score': [24, 10, 20, 10, 20]
    }
    df_expected = pd.DataFrame(expected_output)
    test_question_2(df_2, df_expected)
    # Test Question 3
    df = merge_data()
    test_question_3(df)
    # Test Question 5
    df = merge_data
    test_question_5(df)

    df = merge_data
    test_question_6(df)



if __name__ == '__main__':
    main()
