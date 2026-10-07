import pandas as pd

subjects = ["Maths", "Physics", "Python", "English"]

def clean_data(df):
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df

def calculate_total_percentage(df):
    df["Total"] = df[subjects].sum(axis=1)
    df["Percentage"] = df["Total"] / len(subjects)
    return df

def grade(p):
    if p >= 90:
        return "A+"
    elif p >= 80:
        return "A"
    elif p >= 70:
        return "B"
    elif p >= 60:
        return "C"
    elif p >= 50:
        return "D"
    else:
        return "F"

def add_grade(df):
    df["Grade"] = df["Percentage"].apply(grade)
    return df