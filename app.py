import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

st.markdown("**Ans**: \n")

x_limit = 100
x_axis = np.arange(0,100,1)
y_data = [random.randint(0,100) for i in range(100)]
df = pd.DataFrame({'x': x_axis,'y': y_data})
st.write(df)

st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

st.markdown("**Ans**: \n")

scatter = alt.Chart(df).mark_point().encode(x='x',y='y')
st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("**Ans**: \n")

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Changed points to circles.
- Added Tooltip.
- Added Title to the graph.
- Made the chart Interactive.
- Added color scale based on the variation in the value of 'y'.
- Made the circle size change depending on the 'y' value.
""")

scatter = alt.Chart(df, title='Scatterplot').interactive().mark_circle().encode(x='x',y='y',color='y',size='y',tooltip=['x','y'])
st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("**Ans**: \n")

st.markdown("""
The 2 changes I made were:
- Made the visual Interactive.
- Added Title to the trail.
- Added Tooltip.
"""
)
source = pd.read_excel('Data_Wheat.xlsx')
st.write(source)

chart=alt.Chart(source, title='Line Chart with Varying Size').mark_trail().interactive().encode(
    x='year:T',
    y='wheat:Q',
    size='wheat:Q',
    tooltip=['year:T','wheat:Q']
)
st.altair_chart(chart, use_container_width=True)
