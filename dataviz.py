"""
Pooja Thorali
CSE 163 AI
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
sns.set()


def compare_family_history(data: pd.DataFrame) -> pd.DataFrame:
    """
    Are there any significant differences in the rates of mental health treatment-seeking
    between those who report a family history of mental illness and those who do not?
    """
    print('pooja')


def main():
    # data for the functions
    data = pd.read_csv('data/survey_14.csv', na_values=['---'])
    # functions to call here
    compare_family_history(data)


if __name__ == '__main__':
    main()