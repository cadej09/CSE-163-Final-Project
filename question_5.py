"""
This file answers the question: 'How does the state ofresidence impact the likelihood of
seeking mental health treatment?' This data visualization displays a choropleth map of the United States.
"""

# plot_treatment_by_state(merged_df)

from data_cleaning import merge_data
import plotly.graph_objects as go
import plotly.io as pio

def plot_treatment_by_state(dataframe):
    data = dataframe.dropna()
    map_data = data[['state', 'treatment']]
    map_data['treatment'] = map_data['treatment'].replace({'Yes': 1, 'No': 0})

    map_data['treatment'] = map_data['treatment'].astype(int)
    map_data = map_data.groupby('state')['treatment'].sum().reset_index()
    
    fig = go.Figure(data=go.Choropleth(
        locations=map_data['state'], # Spatial coordinates
        z = map_data['treatment'].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'Blues',
        colorbar_title = "Treatment Rate",
    ))

    fig.update_layout(
        title_text = 'Mental Health Treatment Seeking by State: Exploring the Impact of Location on Help-Seeking Behaviors',
        geo_scope='usa',
    )

    pio.write_image(fig, 'output/question_5_graph.png')


def main():
    df = merge_data()
    plot_treatment_by_state(df)
    

if __name__ == '__main__':
    main()