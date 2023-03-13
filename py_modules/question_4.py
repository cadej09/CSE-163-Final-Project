"""
CSE 163 WI23
Cade Jeong, Pooja Thorail, Hans Xu

This file aims to answer the question of how working in a tech company and the
number of employees impact the likelihood of seeking mental health treatment,
and it produces a stacked bar graph.
"""
from data_cleaning import merge_data
import plotly.express as px
import pandas as pd
import plotly.io as pio


def plot_help_seeking_by_company_size(dataframe: pd.DataFrame,
                                      output_filename: str) -> None:
    """
    Plots a stacked bar graph that shows the count of participants who seek
    mental health help and do not, grouped by the size of the company
    in terms of the number of employees.

    Args:
        dataframe (pd.DataFrame):
            A pandas dataframe that contains the cleaned data.

        output_filename (str): A string that represents the output file name.

    Returns:
        None.
        The function saves the plot as a PNG image in the 'output' folder.
    """
    data = dataframe.dropna()
    data = data.sort_values(by=["no_employees"], ascending=True)

    # Clean data
    data = data[data["seek_help"].isin(["Yes", "No", "I don't know"])]

    # Create bar chart with color-coded bars
    fig = px.bar(data,
                 x="no_employees",
                 color="seek_help",
                 title="Mental Health Help-Seeking by Company Size",
                 labels={"no_employees": "Number of Employees in a Company",
                         "seek_help": "Mental Health Help-Seeking"},
                 color_discrete_map={"Yes": "#3D9970", "No": "#FF4136",
                                     "Don't know": "#FF851B"})

    # Adjust layout
    fig.update_layout(showlegend=True, legend_title='Does your employer'
                                                    'provide mental health'
                                                    'resources?',
                      xaxis={"categoryorder": "array",
                             "categoryarray": ['1-5', '6-25', '26-100',
                                               '100-500', '500-1000',
                                               'More than 1000']})
    fig.update_xaxes(type='category')
    fig.update_yaxes(title="Count of Participants")
    pio.write_image(fig, output_filename)


def main():
    df = merge_data()
    plot_help_seeking_by_company_size(df, 'output/question_4_graph.png')
    df_14 = pd.read_csv('data/survey_14.csv')
    plot_help_seeking_by_company_size(df_14,
                                      'output/question_4_test_graph.png')


if __name__ == '__main__':
    main()
