import pandas as pd
import plotly.express as px
from data_cleaning import merge_data


def employer_support(df: pd.DataFrame):
    # Wellness
    # df = df[['year'] == year]
    wellness = df['wellness_program']
    wellness.replace(["No", "Don't know", "I don't know", "Yes"],
                     [0, 0.2, 0.2, 1], inplace=True)
    # Care Option
    care = df['care_options']
    care.replace(["No", "I am not sure", "Yes"], [0, 0.2, 1], inplace=True)
    # Benefits
    benefits = df['benefits']
    benefits.replace(["No", "Don't know", "I don't know", "Yes",
                      'Not eligible for coverage / N/A',
                      'Not eligible for coverage / NA'],
                     [0, 0.2, 0.2, 1, 0, 0], inplace=True)
    # Leave
    # leave = df['leave']
    # Calculate support score
    df['support_score'] = wellness + care + benefits


def employee_comfortable(df):
    # Do you think that discussing a mental health issue with your employer
    # would have negative consequences?
    # df[['year'] == year]
    mental_consequence = df['mental_health_interview']
    mental_consequence.replace(["No", "Maybe", "Yes"], [1, 0.25, 0],
                               inplace=True)
    coworkers = df['coworkers']
    coworkers.replace(["No", "Maybe", "Yes"], [0, 0.4, 1],
                      inplace=True)
    supervisor = df['supervisor']
    supervisor.replace(["No", "Maybe", "Yes"], [0, 0.6, 1],
                       inplace=True)
    # comfortable score
    df['comfortable_score'] = mental_consequence + coworkers + supervisor


def graph_relation(df):
    df_group = (df.groupby(['year', 'support_score'])['comfortable_score']
                .mean()
                .reset_index()
                .rename(columns={'comfortable_score': 'comfortable_score'}))
    print(df_group)
    x_column = 'support_score'
    y_column = 'comfortable_score'
    fig = px.scatter(df_group, x=x_column, y=y_column,
                     trendline='ols', animation_frame="year")
    fig.update_layout(yaxis_range=[1.2, 2.4])
    fig.show()


def main():
    df = merge_data().dropna()
    employer_support(df)
    employee_comfortable(df)
    graph_relation(df)


if __name__ == '__main__':
    main()
