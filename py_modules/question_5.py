"""
CSE 163 WI23
Cade Jeong, Pooja Thorail, Hans Xu

This file answers the question:
    'How does the state ofresidence impact the likelihood of
    seeking mental health treatment?'
This data visualization displays a choropleth map of the United States.
"""

from data_cleaning import merge_data
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio


def plot_treatment_by_state(dataframe: pd.DataFrame) -> None:
    """
    Plots a choropleth map of the United States with color-coded states
    based on the mental health treatment rate.

    Args:
        dataframe (pd.DataFrame):
            A pandas dataframe containing the relevant columns.

    Returns:
        None. This function displays the plot and saves it as a
        PNG image in the 'output' folder.
    """
    data = dataframe.dropna()
    map_data = data[['state', 'treatment']].copy()
    map_data['treatment'] = map_data['treatment'].replace({
        'Yes': 1,
        'No': 0
    }).values

    map_data = map_data.groupby('state')['treatment'].sum().reset_index()

    fig = go.Figure(data=go.Choropleth(
        # Spatial coordinates
        locations=map_data['state'],
        # Data to be color-coded
        z=map_data['treatment'].astype(float),
        # set of locations match entries in `locations`
        locationmode='USA-states',
        colorscale='Blues',
        colorbar_title="Treatment Rate",
    ))

    fig.update_layout(
        title_text='Mental Health Treatment Seeking by State: Exploring the'
                   'Impact of Location on Help-Seeking Behaviors',
        geo_scope='usa',
    )

    pio.write_image(fig, 'output/question_5_graph.png')


def main():
    df = merge_data()
    plot_treatment_by_state(df)


if __name__ == '__main__':
    main()
