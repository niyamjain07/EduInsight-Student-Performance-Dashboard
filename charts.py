import pandas as pd
import plotly.express as px

subjects = ["Maths", "Physics", "Python", "English"]

def subject_chart(df):

    subject_avg = pd.DataFrame({
        "Subject": subjects,
        "Average Marks": [
            df["Maths"].mean(),
            df["Physics"].mean(),
            df["Python"].mean(),
            df["English"].mean()
        ]
    })

    fig = px.bar(
        subject_avg,
        x="Subject",
        y="Average Marks",
        color="Subject",
        text="Average Marks",
        title="Average Marks by Subject"
    )

    fig.update_traces(textposition="outside")

    return fig


def grade_chart(df):

    return px.pie(
        df,
        names="Grade",
        hole=0.45,
        title="Grade Distribution"
    )


def attendance_chart(df):

    return px.scatter(
        df,
        x="Attendance",
        y="Percentage",
        color="Grade",
        hover_name="Name",
        size="Percentage",
        title="Attendance vs Performance"
    )


def histogram(df):

    return px.histogram(
        df,
        x="Percentage",
        nbins=10,
        title="Percentage Distribution"
    )


def heatmap(df):

    corr = df[
        ["Maths","Physics","Python","English","Attendance"]
    ].corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="Viridis",
        title="Correlation Heatmap"
    )

    return fig