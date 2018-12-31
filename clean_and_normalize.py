import pandas as pd
import numpy as np

import re
import time
import os
import calendar
from datetime import datetime
os.environ['TZ']='EST'

def clean_text_df(df):
    """
    Cleans and normalizes columns in text data frame.
    
    Arguments:
        df: Dataframe to be cleaned. 
    
    Returns:
        df: Clean and normalized dataframe.
    """
    
    # Clean ID column and change data type to integer
    ids = [int(re.sub(r"#", "", val)) for val in df['ID'].values]
    df['ID'] = ids
    
    # Clean Races column and changed data type to integer 
    races = [int(re.sub(r',', '', val)) for val in df['Races'].values]
    df['Races'] = races
    
    # Normalize Top Score column
    top_score = [re.split(r" — ", val) for val in df['Top Score'].values]
    
    top_score_wpm = [float(re.sub(r',', '', val[0])) for val in top_score]
    top_score_name = [val[1] for val in top_score]
    top_score_full_name = [re.sub(r'\(([a-zA-Z0-9]+)\)', '', val).strip() for val in top_score_name]
    top_score_nick_name = [re.findall(r'\(([a-zA-Z0-9]+)\)', val)[0] if re.findall(r'\(([a-zA-Z0-9]+)\)', val) else np.nan for val in top_score_name]

    df['Top Score WPM'] = top_score_wpm
    df['Top Score Full Name'] = top_score_full_name
    df['Top Score Nickname'] = top_score_nick_name
    
    df = df.drop(['Top Score'], axis=1)
    
    # Normalize date
    date = [val.split(' ') for val in df['Active Since'].values]
    
    month = [val[0].strip() for val in date]
    day = [int(val[1].strip(",")) for val in date]
    year = [int(val[2].strip()) for val in date]

    df["Active Since Month"] = month
    df["Active Since Day"] = day
    df["Active Since Year"] = year

    df = df.drop("Active Since", axis = 1)
    
    return df

def clean_race_df(df):
    
    # Convert Race Id into integer
    df.Race = df.Race.astype('int')
    
    # Set timezone
    os.environ['TZ'] = 'EST'
    
    # Convert datetime to epoch
    pattern = '%Y-%m-%d %H:%M:%S'
    df["Date_Epoch"] = df.Date.apply(lambda x: int(time.mktime(time.strptime(x, pattern))))
    
    # Normalize datetime to month, year and day
    df["Date_Month"] = df.Date.apply(lambda x: calendar.month_name[datetime.strptime(x.split()[0],'%Y-%m-%d').month])
    df["Date_Year"] = df.Date.apply(lambda x: int(datetime.strptime(x.split()[0],'%Y-%m-%d').year))
    df["Date_Day"] = df.Date.apply(lambda x: int(datetime.strptime(x.split()[0],'%Y-%m-%d').day))
    df["Date"] = df.Date.apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    #df = df.drop("Date", axis=1)
    
    # Convert accuracy into float
    df.Accuracy = df.Accuracy.apply(lambda x: float(re.sub(r'%', '', x))/100)
    
    # Normalize outcome
    df["Outcome_Rank"] = df.Outcome.apply(lambda x: int(re.findall(r'\(([0-9]+)\sof', x)[0].strip()))
    df["Outcome_No_Racers"] = df.Outcome.apply(lambda x: int(re.findall(r'of\s([0-9]+)\)', x)[0].strip()))

    df = df.drop('Outcome', axis=1)
    df.rename(columns = {'Text':'Text_Id'}, inplace = True)
    
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/texts.csv")
    df_cleaned_texts = clean_text_df(df)
    df_cleaned_texts.to_csv("data/cleaned_texts_data.csv")

    df = pd.read_csv("data/races.csv")
    df_cleaned_races = clean_race_df(df)
    df_cleaned_races.to_csv("data/cleaned_races_data.csv")