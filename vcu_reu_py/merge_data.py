import pandas as pd
from functools import reduce


def merge_csvs():
    # Add a suffix to all the comment columns
    df1 = pd.read_csv('data/connect.csv').rename(columns={'comment':'comment_connect'})
    df2 = pd.read_csv('data/else.csv').rename(columns={'comment':'comment_else'})
    df3 = pd.read_csv('data/mental_health.csv').rename(columns={'comment':'comment_mental_health'})
    df4 = pd.read_csv('data/miss.csv').rename(columns={'comment':'comment_miss'})
    df5 = pd.read_csv('data/school.csv').rename(columns={'comment':'comment_school'})
    df6 = pd.read_csv('data/surprise.csv').rename(columns={'comment':'comment_surprise'})

    dfList = [df1, df2, df3, df4, df5, df6]

    # merge all the data into one dataframe
    df = reduce(lambda x, y: pd.merge(x, y, on = 'participant'), dfList)

    # Save the new dataframe
    df.to_csv('data/comments.csv')

if __name__ == "__main__":
    merge_csvs()