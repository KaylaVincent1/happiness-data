import streamlit as st
import plotly.express as px
import pandas as pd

# Load the data
df = pd.read_csv("happy.csv")

# App title
st.title("In Search for Happiness")

# Dropdowns for X and Y axis selection
x_axis = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"))

# Display selected X and Y axis labels as a subtitle
st.subheader(f"{x_axis} and {y_axis}")

match x_axis:
    case "GDP":
        x_array = df["gdp"]
    case "Happiness":
        x_array = df["happiness"]
    case "Generosity":
        x_array = df["generosity"]

match y_axis:
    case "GDP":
        y_array = df["gdp"]
    case "Happiness":
        y_array = df["happiness"]
    case "Generosity":
        y_array = df["generosity"]

figure = px.scatter(x=x_array, y=y_array, labels={"x": f"{x_axis}", "y": f"{y_axis}"})
st.plotly_chart(figure)


# Another method
# import streamlit as st
# import plotly.express as px
# import pandas as pd
#
# # Load the data
# df = pd.read_csv("happy.csv")
#
# # App title
# st.title("In Search for Happiness")
#
# # Map selectbox choices to DataFrame column names
# axis_options = {
#     "GDP": "gdp",
#     "Happiness": "happiness",
#     "Generosity": "generosity"
# }
#
# # Dropdowns for X and Y axis selection
# x_axis_label = st.selectbox("Select the data for the X-axis", list(axis_options.keys()))
# y_axis_label = st.selectbox("Select the data for the Y-axis", list(axis_options.keys()))
#
# # Map selected labels to actual column names
# x_axis = axis_options[x_axis_label]
# y_axis = axis_options[y_axis_label]
#
# # Display selected X and Y axis labels as a subtitle
# st.subheader(f"{x_axis_label} and {y_axis_label}")
#
# # Generate and display the scatter plot
# figure = px.scatter(df, x=x_axis, y=y_axis, labels={"x": x_axis_label, "y": y_axis_label})
# st.plotly_chart(figure)