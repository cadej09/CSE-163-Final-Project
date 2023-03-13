"""
This file aims to answer the question of how working in a tech company and the number of employees impact the
likelihood of seeking mental health treatment, and it produces a stacked bar graph.
"""
from data_cleaning import merge_data
import plotly.express as px
import pandas as pd
import plotly.io as pio


def plot_help_seeking_by_company_size(dataframe):
    data = dataframe.dropna()
    data = data.sort_values(by=["no_employees"], ascending=True)
    emp_data = data[['no_employees','seek_help']]
    
    # Clean data
    data = data[data["seek_help"].isin(["Yes", "No", "I don't know"])]

    # Create bar chart with color-coded bars
    fig = px.bar(data, 
                 x="no_employees", 
                 color="seek_help", 
                 title="Mental Health Help-Seeking by Company Size",
                 labels={"no_employees": "Number of Employees in a Company", "seek_help": "Mental Health Help-Seeking"},
                 color_discrete_map={"Yes": "#3D9970", "No": "#FF4136", "Don't know": "#FF851B"})

    # Adjust layout
    fig.update_layout(showlegend=True, legend_title="Does your employer provide mental health resources?",
                      xaxis={"categoryorder": "array", "categoryarray": ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000']})
    fig.update_xaxes(type='category')
    fig.update_yaxes(title="Count of Participants")
    pio.write_image(fig, 'output/question_4_graph.png')


def main():
    df = merge_data()
    plot_help_seeking_by_company_size(df)
    

if __name__ == '__main__':
    main()