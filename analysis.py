import pandas as pd

subjects = ["Maths", "Physics", "Python", "English"]

def dashboard_summary(df):
    topper = df.loc[df["Percentage"].idxmax()]

    return {
        "students": len(df),
        "average_percentage": round(df["Percentage"].mean(), 2),
        "attendance": round(df["Attendance"].mean(), 2),
        "topper": topper["Name"]
    }


def descriptive_statistics(df):
    return pd.DataFrame({
        "Mean": df[subjects].mean(),
        "Median": df[subjects].median(),
        "Maximum": df[subjects].max(),
        "Minimum": df[subjects].min(),
        "Standard Deviation": df[subjects].std()
    })


def top_students(df):
    return df.sort_values(
        by="Percentage",
        ascending=False
    ).head(5)


def weak_students(df):
    return df[
        (df["Percentage"] < 60) |
        (df["Attendance"] < 75)
    ]


def insights(df):

    highest_subject = df[subjects].mean().idxmax()
    lowest_subject = df[subjects].mean().idxmin()

    return {
        "highest_subject": highest_subject,
        "lowest_subject": lowest_subject,
        "low_attendance": len(df[df["Attendance"] < 75]),
        "average_attendance": round(df["Attendance"].mean(),2)
    }