import plotly.express as px

def plot_work_interference(dataframe):
    # Drop rows with missing values
    data = dataframe.dropna()

    # Filter for rows where treatment is "Yes"
    filtered_data = data[data['treatment'] == 'Yes']

    # Filter out rows where 'work_interfere' is "Not applicable to me"
    filtered_data = filtered_data[filtered_data['work_interfere'] != 'Not applicable to me']


    # Group by 'work_interfere' and count the number of responses for each category
    grouped_data = filtered_data.groupby('work_interfere').size().reset_index(name='count')

    # Create pie chart using Plotly Express
    fig = px.pie(grouped_data, values='count', names='work_interfere', 
                 color_discrete_sequence=px.colors.sequential.RdBu)

    # Add title and labels to the plot
    fig.update_layout(title='Work Interference for Employees Seeking Treatment for Mental Health Issues',
                      xaxis_title='Level of Work Interference',
                      yaxis_title='Number of Respondents')

    # Show the plot
    fig.show()