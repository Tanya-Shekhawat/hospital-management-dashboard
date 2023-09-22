import streamlit as st
import numpy as np
import pandas as pd
import plotly_express as px
import altair as alt

# Create a title for your app
st.set_page_config(page_title="Hospital Report", 
                   page_icon=":bar_chart:",
                   layout="wide")
# st.title("Hospital Report")

# Provide the path to your Excel file
excel_file_path = "/Users/aynat/Developer/Dev-Prpphests-visual-dashboard/streamlit/data/main_admin.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# ------- SIDE BAR ----------
st.sidebar.header("Select Filters from here:")
city = st.sidebar.multiselect(
    "City: ",
    options=df["place"].unique(),
    default=df["place"].unique()
)
doctor_name = st.sidebar.multiselect(
    "Doctor Name: ",
    options=df["doctorname"].unique(),
    default=df["doctorname"].unique()
) 

category = st.sidebar.multiselect(
    "Category: ",
    options=df["category"].unique(),
    default=df["category"].unique()
) 

age_group = st.sidebar.multiselect(
    "Age Group: ",
    options=df["age_group"].unique(),
    default=df["age_group"].unique()
)

gender = st.sidebar.multiselect(
    "Gender: ",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

df_selection = df.query(
    "place == @city & doctorname == @doctor_name & category == @category &  age_group == @age_group &  gender == @gender "
)

# -------------MAIN PAGE --------------
st.title(":bar_chart: Hospital Report")

# Create Streamlit columns for charts
col1, col2 = st.columns(2) 

# with col1:


# with col2:
    # # [BAR CHART - Age Group of Patients]
    # count_patient_age_group = df_selection['age_group'].value_counts().reset_index()
    # count_patient_age_group.columns = ['age_group', 'count']

    # fig_patient_age = px.bar(
    #     count_patient_age_group,
    #     x="age_group",
    #     y="count",
    #     title="Age Group of Patients",
    #     color_discrete_sequence=["#0083B8"] * len(count_patient_age_group),
    #     template="plotly_white",
    # )

    # fig_patient_age.update_layout(
    #     plot_bgcolor="rgba(0,0,0,0)",
    #     yaxis=dict(showgrid=False)
    # )
    # st.plotly_chart(fig_patient_age)

# [PIE CHART - Gender Distribution of Patients]
# col3, col4 = st.columns(2)

with col1:
    count_patient_gender = df_selection['gender'].value_counts().reset_index()
    count_patient_gender.columns = ['gender', 'count']

    custom_colors = ['#B2A4FF', '#CDF0EA']  

    st.plotly_chart(px.pie(
        count_patient_gender,
        names='gender',
        values='count',
        title="Gender Distribution of Patients",
        color_discrete_sequence=custom_colors,
        template="plotly_white",
    ).update_traces(textposition='inside', textinfo='percent+label'))

with col2:
    # [PIE CHART - Age Group Distribution]
    count_age_group = df_selection['age_group'].value_counts().reset_index()
    count_age_group.columns = ['age_group', 'count']

    custom_colors = ['#EDB7ED', '#8DDFCB', '#D9ACF5', '#EA907A', '#556FB5']  

    st.plotly_chart(px.pie(
        count_age_group,
        names='age_group',
        values='count',
        title="Age Group Distribution",
        color_discrete_sequence=custom_colors,
        template="plotly_white",
    ).update_traces(textposition='inside', textinfo='percent+label'))

# [PIE CHART - Disease Distribution of Patients]
col3, col4 = st.columns(2)

with col3:
    count_patient_disease = df_selection['category'].value_counts().reset_index()
    count_patient_disease.columns = ['category', 'count']

    custom_colors = ['#E87D0D', '#3CB44B']  

    st.plotly_chart(px.pie(
        count_patient_disease,
        names='category',
        values='count',
        title="Disease Distribution of Patients",
        color_discrete_sequence=custom_colors,
        template="plotly_white",
    ).update_traces(textposition='inside', textinfo='percent+label'))

with col4:
    # [PIE CHART - Doctor Distribution]
    count_doctor = df_selection['doctorname'].value_counts().reset_index()
    count_doctor.columns = ['doctorname', 'count']

    custom_colors = ['#E87D0D', '#3CB44B']  

    st.plotly_chart(px.pie(
        count_doctor,
        names='doctorname',
        values='count',
        title="Doctor Distribution",
        color_discrete_sequence=custom_colors,
        template="plotly_white",
    ).update_traces(textposition='inside', textinfo='percent+label'))

# Display the DataFrame in the app
st.dataframe(df_selection)
st.markdown("##")
