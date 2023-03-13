"""
CSE163 WI23
Cade Jeong, Pooja Thorail, Hans Xu

This file provides an analysis on the prevalence of work interference
experienced by employees seeking treatment for mental health issues.
The main output of the analysis is a pie chart, displaying the
percentages of individuals who reported experiencing work interference due to
their mental health treatment.
"""

from data_cleaning import merge_data
import plotly.express as px
import pandas as pd
import plotly.io as pio


def plot_work_interference(dataframe: pd.DataFrame) -> None:
    """
    Plots a pie chart showing the prevalence of work interference experienced
    by employees seeking treatment for mental health issues.

    Args:
        dataframe (pd.DataFrame):
            A pandas dataframe containing the relevant columns.

    Returns:
        None. This function displays the plot and saves it as a
        PNG image in the 'output' folder.
    """
    # Drop rows with missing values
    data = dataframe.dropna()

    # Filter for rows where treatment is "Yes"
    filtered_data = data[data['treatment'] == 'Yes']

    # Filter out rows where 'work_interfere' is "Not applicable to me"
    filtered_data = filtered_data[
        filtered_data['work_interfere'] != 'Not applicable to me'
    ]
    # Group by 'work_interfere' and count the number of
    # responses for each category
    grouped_data = (
        filtered_data
        .groupby('work_interfere')
        .size()
        .reset_index(name='count')
    )
    # Create pie chart using Plotly Express
    fig = px.pie(grouped_data, values='count', names='work_interfere',
                 color_discrete_sequence=px.colors.sequential.RdBu)

    # Add title and labels to the plot
    fig.update_layout(title='Work Interference for Employees Seeking Treatment'
                            'for Mental Health Issues',
                      xaxis_title='Level of Work Interference',
                      yaxis_title='Number of Respondents')

    # Show the plot
    pio.write_image(fig, 'output/question_6_graph.png')


def main():
    df = merge_data()
    plot_work_interference(df)


if __name__ == '__main__':
    main()
