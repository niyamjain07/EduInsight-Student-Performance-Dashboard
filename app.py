import streamlit as st
import pandas as pd
import plotly.express as px
from utils import clean_data, calculate_total_percentage, add_grade
from analysis import (
    dashboard_summary,
    descriptive_statistics,
    top_students,
    weak_students,
    insights,
)
from charts import (
    subject_chart,
    grade_chart,
    attendance_chart,
    histogram,
    heatmap,
)

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="EduInsight",
    page_icon="📊",
    layout="wide",
)

# ---------------- HEADER ----------------

st.title("📊 EduInsight")
st.caption("Student Performance Analytics Dashboard")

st.sidebar.header("📁 Upload Dataset")
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍💻 Developer")

st.sidebar.info("""
**Name:** Niyam

**Course:** B.Tech AI & DS

**College:** JECRC Foundation

**Project:** EduInsight
""")

uploaded_file = st.sidebar.file_uploader(
    "Choose CSV File",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Upload studentdata.csv from the sidebar.")
    st.stop()

# ---------------- READ DATA ----------------

df = pd.read_csv(uploaded_file)

df = clean_data(df)
df = calculate_total_percentage(df)
df = add_grade(df)

# ---------------- PREVIEW ----------------

st.success("Dataset Loaded Successfully ✅")

with st.expander("📄 Dataset Preview"):
    st.dataframe(df, use_container_width=True)

# ---------------- DASHBOARD ----------------

summary = dashboard_summary(df)

st.subheader("📌 Dashboard Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Students",
        summary["students"]
    )

with c2:
    st.metric(
        "Average %",
        summary["average_percentage"]
    )

with c3:
    st.metric(
        "Topper",
        summary["topper"]
    )

with c4:
    st.metric(
        "Attendance",
        f"{summary['attendance']}%"
    )

st.divider()

# ---------------- CHARTS ----------------

st.subheader("📊 Subject Performance")

st.plotly_chart(
    subject_chart(df),
    use_container_width=True
)

st.plotly_chart(
    grade_chart(df),
    use_container_width=True
)

st.plotly_chart(
    attendance_chart(df),
    use_container_width=True
)

st.plotly_chart(
    histogram(df),
    use_container_width=True
)

st.divider()
# ---------------- SEARCH ----------------

st.subheader("🔍 Search Student")

search = st.text_input("Enter Student Name")

if search:
    result = df[df["Name"].str.contains(search, case=False)]

    if result.empty:
        st.error("No Student Found")
    else:
        st.success("Student Found")
        st.dataframe(result, use_container_width=True)

st.divider()

# ---------------- FILTER ----------------

st.subheader("🎯 Filter Students")

grade_filter = st.multiselect(
    "Select Grade",
    sorted(df["Grade"].unique())
)

attendance_filter = st.slider(
    "Minimum Attendance",
    0,
    100,
    0
)

filtered = df.copy()

if grade_filter:
    filtered = filtered[
        filtered["Grade"].isin(grade_filter)
    ]

filtered = filtered[
    filtered["Attendance"] >= attendance_filter
]

st.dataframe(
    filtered,
    use_container_width=True
)

st.divider()

# ---------------- TOP STUDENTS ----------------

st.subheader("🏆 Top 5 Students")

st.dataframe(
    top_students(df),
    use_container_width=True
)

st.divider()

# ---------------- WEAK STUDENTS ----------------

st.subheader("⚠ Students Needing Improvement")

weak = weak_students(df)

if weak.empty:
    st.success("No Weak Students 🎉")
else:
    st.dataframe(
        weak,
        use_container_width=True
    )

st.divider()

# ---------------- STATISTICS ----------------

st.subheader("📊 Descriptive Statistics")

stats = descriptive_statistics(df)

st.dataframe(
    stats,
    use_container_width=True
)

st.divider()
# ---------------- DATA CLEANING REPORT ----------------

st.subheader("🧹 Data Cleaning Report")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

with col2:
    st.metric(
        "Duplicate Records",
        int(df.duplicated().sum())
    )

missing = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values
})

st.dataframe(
    missing,
    use_container_width=True
)

st.divider()

# ---------------- HEATMAP ----------------

st.subheader("🔥 Correlation Heatmap")

st.plotly_chart(
    heatmap(df),
    use_container_width=True
)

st.divider()

# ---------------- INSIGHTS ----------------

st.subheader("🤖 Automatic Insights")

info = insights(df)

st.success(
    f"🏆 Highest Performing Subject : {info['highest_subject']}"
)

st.warning(
    f"📉 Lowest Performing Subject : {info['lowest_subject']}"
)

st.info(
    f"👨‍🎓 Students Below 75% Attendance : {info['low_attendance']}"
)

st.write("### Recommendations")

st.markdown("""
- Improve attendance of students below **75%**.
- Arrange extra classes for the lowest-performing subject.
- Reward top-performing students.
- Monitor students scoring below **60%**.
""")

st.divider()

# ---------------- DOWNLOAD ----------------

st.subheader("📥 Download Processed Dataset")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download CSV",
    data=csv,
    file_name="Processed_Student_Data.csv",
    mime="text/csv"
)

st.divider()

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "EduInsight • Student Performance Analytics Dashboard"
)
st.markdown("---")
st.caption("Developed using ❤️ Python • Streamlit • Pandas • Plotly")