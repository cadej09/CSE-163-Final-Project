"""
CSE 163 WI23
Cade Jeong, Pooja Thorail, Hans Xu

This file reads in all of the datasets and cleans up each of the dataset
to contain the same columns and values. Uses pandas for dataframe manipulation.
Returns the combined datasets as a one data frame.
"""

import pandas as pd


def merge_data() -> pd.DataFrame:
    """
    Read in the three mental health survey datasets from 2014, 2016, and 2019.
    Clean up each dataset to contain the same columns and values.
    Concatenate the three datasets into one data frame.

    Returns:
    --------
    merged_df : pandas.DataFrame
        A data frame containing the cleaned and concatenated data from
        the three mental health surveys.
    """
    # Cleaning 2014 dataset.
    df_2014 = pd.read_csv('data/survey_14.csv')

    df_2014 = df_2014.loc[:, 'Age':].drop(columns=['Gender', 'remote_work',
                                                   'comments', 'mental_health_'
                                                   'consequence',
                                                   'phys_health_consequence',
                                                   'mental_vs_physical',
                                                   'obs_consequence'])

    # Match the answer/value
    df_2014["work_interfere"].fillna('Not applicable to me', inplace=True)
    df_2014[['coworkers', 'supervisor']] = (
        df_2014[['coworkers', 'supervisor']]
        .replace('Some of them', 'Maybe')
    )
    df_2014[['benefits', 'wellness_program', 'seek_help', 'anonymity']] = (
        df_2014[['benefits', 'wellness_program', 'seek_help', 'anonymity']]
        .replace("Don't know'", "I don't know")
    )
    df_2014['care_options'] = (
        df_2014['care_options'].replace('Not sure', 'I am not sure')
    )
    df_2014['year'] = 2014

    # Cleaning 2016 dataset.
    df_2016 = pd.read_csv('data/survey_16.csv')

    # Select only shared columns between three datasets.
    df_2016 = df_2016[['What is your age?',
                       'What country do you live in?',
                       'What US state or territory do you live in?',
                       'Are you self-employed?',
                       'Do you have a family history of mental illness?',
                       'Have you ever sought treatment for a mental health '
                       'issue from a mental health professional?',
                       'If you have a mental health issue, do you feel that '
                       'it interferes with your work when '
                       'NOT being treated effectively?',
                       'How many employees does your '
                       'company or organization have?',
                       'Is your employer primarily '
                       'a tech company/organization?',
                       'Does your employer provide mental health benefits '
                       'as part of healthcare coverage?',
                       'Do you know the options for mental health care '
                       'available under your employer-provided coverage?',
                       'Has your employer ever formally discussed '
                       'mental health (for example, as part of a '
                       'wellness campaign or other official communication)?',
                       'Does your employer offer resources '
                       'to learn more about mental health '
                       'concerns and options for seeking help?',
                       'Is your anonymity protected if you choose to take '
                       'advantage of mental health or substance abuse '
                       'treatment resources provided by your employer?',
                       'If a mental health issue prompted you to request '
                       'a medical leave from work, '
                       'asking for that leave would be:',
                       'Would you feel comfortable discussing a mental health '
                       'disorder with your coworkers?',
                       'Would you feel comfortable discussing a mental health '
                       'disorder with your direct supervisor(s)?',
                       'Would you bring up a mental health issue with '
                       'a potential employer in an interview?',
                       'Would you be willing to bring up a physical health '
                       'issue with a potential employer in an interview?']]
    df_2016['year'] = 2016

    # Match the column names
    df_2016.columns = ['Age', 'Country', 'state', 'self_employed',
                       'family_history', 'treatment', 'work_interfere',
                       'no_employees', 'tech_company', 'benefits',
                       'care_options', 'wellness_program', 'seek_help',
                       'anonymity', 'leave', 'coworkers', 'supervisor',
                       'mental_health_interview', 'phys_health_interview',
                       'year']

    # Match the answer/value
    df_2016[['self_employed', 'treatment', 'tech_company']] = (
        df_2016[['self_employed', 'treatment', 'tech_company']]
        .replace([1, 0], ['Yes', 'No'])
    )

    # Cleaning 2019 dataset.
    df_2019 = pd.read_csv('data/survey_19.csv')

    # Select only common columns between three datasets.
    df_2019 = df_2019[['What is your age?',
                       'What country do you *live* in?',
                       'What US state or territory do you *live* in?',
                       '*Are you self-employed?*',
                       'Do you have a family history of mental illness?',
                       'Have you ever sought treatment for a mental health '
                       'disorder from a mental health professional?',
                       'If you have a mental health disorder, how often do '
                       'you feel that it interferes with your work *when* '
                       '_*NOT*_* being treated effectively '
                       '(i.e., when you are experiencing symptoms)?*',
                       'How many employees does '
                       'your company or organization have?',
                       'Is your employer primarily '
                       'a tech company/organization?',
                       'Does your employer provide mental health benefits '
                       'as part of healthcare coverage?',
                       'Do you know the options for '
                       'mental health care available '
                       'under your employer-provided health coverage?',
                       'Has your employer ever formally discussed mental '
                       'health (for example, as part of a wellness campaign '
                       'or other official communication)?',
                       'Does your employer offer resources to '
                       'learn more about mental health disorders '
                       'and options for seeking help?',
                       'Is your anonymity protected if you choose to take '
                       'advantage of mental health or substance abuse '
                       'treatment resources provided by your employer?',
                       'If a mental health issue prompted you to request a '
                       'medical leave from work, how easy or difficult '
                       'would it be to ask for that leave?',
                       'Would you feel comfortable discussing a mental health '
                       'issue with your coworkers?',
                       'Would you feel comfortable discussing a mental health '
                       'issue with your direct supervisor(s)?',
                       'Would you bring up your *mental* health with a '
                       'potential employer in an interview?',
                       'Would you be willing to bring up a physical health '
                       'issue with a potential employer in an interview?']]
    df_2019['year'] = 2019

    # Match the column names
    df_2019.columns = ['Age', 'Country', 'state', 'self_employed',
                       'family_history', 'treatment', 'work_interfere',
                       'no_employees', 'tech_company', 'benefits',
                       'care_options', 'wellness_program', 'seek_help',
                       'anonymity', 'leave', 'coworkers', 'supervisor',
                       'mental_health_interview', 'phys_health_interview',
                       'year']

    # Match the answer/value
    df_2019[['self_employed', 'treatment', 'tech_company']] = (
        df_2019[['self_employed', 'treatment', 'tech_company']]
        .replace([True, False], ['Yes', 'No'])
    )
    df_2019["care_options"].fillna('I am not sure', inplace=True)

    # Merge the three datasets.
    merged_df = pd.concat([df_2014, df_2016, df_2019])
    merged_df = merged_df.replace({'state': {'Illinois': 'IL',
                                             'Tennessee': 'TN',
                                             'Virginia': 'VA',
                                             'California': 'CA',
                                             'Kentucky': 'KY',
                                             'Oregon': 'OR',
                                             'Pennsylvania': 'PA',
                                             'New Jersey': 'NJ',
                                             'Georgia': 'GA',
                                             'Washington': 'WA',
                                             'New York': 'NY',
                                             'Indiana': 'IN',
                                             'Minnesota': 'MN',
                                             'West Virginia': 'WV',
                                             'Florida': 'FL',
                                             'Massachusetts': 'MA',
                                             'North Dakota': 'ND',
                                             'Texas': 'TX',
                                             'Maryland': 'MD',
                                             'Wisconsin': 'WI',
                                             'Michigan': 'MI',
                                             'Vermont': 'VT',
                                             'North Carolina': 'NC',
                                             'Kansas': 'KS',
                                             'District of Columbia': 'DC',
                                             'Nevada': 'NV', 'Utah': 'UT',
                                             'Connecticut': 'CT',
                                             'Colorado': 'CO',
                                             'Ohio': 'OH',
                                             'Iowa': 'IA',
                                             'South Dakota': 'SD',
                                             'Nebraska': 'NE',
                                             'Maine': 'ME',
                                             'Missouri': 'MO',
                                             'Arizona': 'AZ',
                                             'Oklahoma': 'OK',
                                             'Idaho': 'ID',
                                             'Rhode Island': 'RI',
                                             'Alabama': 'AL',
                                             'Louisiana': 'LA',
                                             'South Carolina': 'SC',
                                             'New Hampshire': 'NH',
                                             'New Mexico': 'NM',
                                             'Montana': 'MT',
                                             'Alaska': 'AK',
                                             'Delaware': 'DE',
                                             'Wyoming': 'WY'}})

    return merged_df
