"""
CSE 163 WI23
Cade Jeong, Pooja Thorail, Hans Xu

This file contains a function that creates a bar chart to show the
distribution of treatment groups by age group.
The resulting plot is saved as a PNG image in the 'output' folder.
"""
from data_cleaning import merge_data
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio


def treatment_by_age_group(df: pd.DataFrame) -> None:
    """
    Create a bar chart showing the distribution of
    treatment groups by age group.

    Args:
        df (pd.DataFrame): A pandas dataframe containing the relevant columns.

    Returns:
        None. This function displays the plot and saves it as a
        PNG image in the 'output' folder.
    """
    data = df[['Age', 'treatment']].dropna()
    data = data[(data['Age'] >= 15) & (data['Age'] < 80)]

    # define the age bins
    bins = [15, 18, 22, 29, 39, 49, 59, 69, 79]

    # create the age groups
    data['age_group'] = pd.cut(data['Age'], bins=bins).astype(str)

    # Group by age group and get counts for each treatment group
    grouped_data = data.groupby(['age_group',
                                 'treatment']).size().reset_index(name='count')

    # Create bar chart
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=grouped_data[grouped_data['treatment'] == 'Yes']['age_group'],
        y=grouped_data[grouped_data['treatment'] == 'Yes']['count'],
        name='Treatment: Yes'
    ))

    fig.add_trace(go.Bar(
        x=grouped_data[grouped_data['treatment'] == 'No']['age_group'],
        y=grouped_data[grouped_data['treatment'] == 'No']['count'],
        name='Treatment: No'
    ))

    fig.update_layout(
        title_text="Distribution of Treatment Groups by Age Group",
        xaxis_title_text="Age Group",
        yaxis_title_text="Count"
    )

    # Save figure
    pio.write_image(fig, 'output/question_3_graph.png')


def main():
    merged_df = merge_data()
    treatment_by_age_group(merged_df)


if __name__ == '__main__':
    main()
