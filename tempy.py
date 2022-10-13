




    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
st.title('Welcome to my Application!:tada:')


import pandas as pd
population= pd.read_csv("world_population.csv") 

import plotly.express as px


# Data wrangling
import pandas as pd
import numpy as np

# Data vislization using plolty graph object(go)
import plotly.graph_objects as go





# For showing plotly plots on notebook
import plotly.offline as py




st.header("Wold Population")
st.subheader("The Dataset contains Population data of every Country/Territory in the world")
st.markdown("""
	This app performs simple webscraping and visualisation of wikipedia world population data . 
In 2018, the world’s population growth rate was 1.12%. Every five years since the 1970s, the population growth rate has continued to fall. The world’s population is expected to continue to grow larger but at a much slower pace. By 2030, the population will exceed 8 billion. In 2040, this number will grow to more than 9 billion. In 2055, the number will rise to over 10 billion, and another billion people won’t be added until near the end of the century. The current annual population growth estimates from the United Nations are in the millions - estimating that over 80 million new lives are added each year.
* **Data source:** [kaggle.com]( https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset
).
	""")
    

    
chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))
  
st.text_input("Please enter your name ", key="name")


clicked= st.button('Click')
st.write(f"Button Status:{clicked}")
disabled = True
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Who are you',['Student','Professor','other'])

st.multiselect('How did you know about our page ',['Social Media', 'Events', 'School'])
st.text_input('Email address')
st.date_input('Availability date')
st.time_input('Local time')

st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.subheader('Countries Population Growth Rate')

fig = go.Figure(data=go.Choropleth(
    locations= population['Country'],
    z = population['Growth_Rate'],
    locationmode = 'country names', 
    colorscale = 'jet',
    colorbar_title = "Growth_Rate",
))

fig.update_layout(
    title = dict(text = '<b>Countries Population Growth Rate</b>',
    x = 0.5)
)

st.plotly_chart(fig)
st.subheader("Insight")
st.markdown("Moldova is leading in population growth rate with a growth rate of 1.0691 followed by Poland, Niger and others.Ukraine has the lowest population growth rate of 0.912 followed by Lebanon, American Samoa and Ukraine have the lowest population growth rate of 0.912..")


st.subheader("Top 10 Countries with the least population")
top_least_population = population.groupby( 'Country')['2022 Population'].sum().sort_values(ascending=True).head(10)
fig1=px.bar(x=top_least_population.index,
          y=top_least_population.values,
          color=top_least_population.index,
          color_discrete_sequence=px.colors.sequential.PuBuGn,
          text=top_least_population.values,
          title="Top 10 Countries with the least population",
          template= 'plotly_dark')
fig.update_layout(
    xaxis_title="Countries",
    yaxis_title="Population",
    font = dict(size=15,family="Franklin Gothic"))
st.plotly_chart(fig1)
st.subheader("Insight")
st.markdown("We note that most of these countries are not from the thrid world countries and each has it own economic strenght as tourism and trade meaning people are leaning towards smaller families and focused on business")

st.subheader("World Population through years")
df1 = (population.set_index(['Continent','Capital',"Country","CCA3",'Area','Density','Growth_Rate','World_Population_Percentage','Rank'])
         .stack()
         .reset_index(name='Population')
         .rename(columns={'level_9':'Year'}))
fig3= px.choropleth(df1.sort_values('Year'), 
              locations = 'CCA3',
              color="Population",
              animation_frame='Year',
              color_continuous_scale ='OrRd',
              title='World population through years' ,
              height=800)

st.plotly_chart(fig3)
st.subheader("Insight")
st.markdown("In every continent population is increasing by time. Population of Asia is increasing highly followed by Africa.")






    

# Colors for plots 
by_continent = population.groupby('Continent').sum().sort_values(by = '2022 Population',ascending = True)
cont_gr = by_continent[['Growth_Rate']].sort_values(by = 'Growth_Rate',ascending = True)
cont_gr

colors = ["#1d7874","#679289","#f4c095","#ee2e31","#ffb563","#918450","#f85e00","#a41623","#9a031e","#d6d6d6","#ffee32","#ffd100","#333533","#202020"]
slider_growth = st.slider("Choose growth Range", max_value = 12, min_value = 50, value = [12, 50],
                          step = 10)

df2 = population.loc[(population["Salary"] >= slider_growth[0]) & (population["Salary"] <= slider_growth[1])]
st.subheader("Population by Continent in 2022")
data = go.Bar(x = cont_gr.index, y = cont_gr['Growth_Rate'], text = cont_gr['Growth_Rate'],textposition ='outside',
              textfont = dict(size = 12,
                             color = 'black'),
              marker = dict(color = colors,
                            opacity = 0.7,
                            line_color = 'black',
                            line_width = 2))
             
layout = go.Layout(title = {'text': "<b>Continents Wise Population Growth Rate</b>",
                           'x':0.5,
                           'xanchor': 'center'},
                   xaxis = dict(title='<b>Continents</b>'),
                   yaxis =dict(title='<b>Growth Rate</b>'),
                   width = 900,
                   height = 600,
                   template = 'plotly_white')

fig5=go.Figure(data = data, layout = layout)
st.plotly_chart(fig5)


st.subheader("Insight")
st.markdown("The Continent with highest growth rate is Africa with growth rate of 58.2109.The Continent with lowset growth rate is South America with growth rate of 14.1114.")

    
    
    
st.select_slider('How much do you know about world population changes and effects?', ['Bad', 'Good', 'Excellent'])
st.slider('How many countries are in Asia?', 0,50)

d= st.number_input('How many continents are in the world?', 0,10)
st.write('Your answer is :', d)

import time
st.balloons()
st.progress(10)
 
    
st.empty()
placeholder = st.empty()




df = pd.DataFrame({
    'first column': ["India", "China", "Brazil", "Ethiopia"],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which Country has the highest population?',
     df['first column'])

'You selected: ', option

st.sidebar.header("Hello :smile:")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'Table of Content',
    ("Personal Information", "Countries Population Growth Rate","Top 10 countries with least population","World population through years","Population by continent 2022","Continents wise population growth rate", "General Information","Conclusion")
)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select the range you got of knowldge from this application',
    0.0, 100.0, (25.0, 75.0)
)





  


'Starting a long computation...'

st.header("Conclusion")
st.write("Africa is the Continent with highest growth rate, Asia continent has the highest population & largest World population percentage of 59.2 the country with the highest population is China and on second is India, the population growth difference of 859.67 Millions, China from (1970 to 2022) is 603.35 Millions and population growth difference of India from (1970 to 2022) is 859.67 and probaly after 10 years India will surpass the China and will become Top1 country with highest Population, population growth of Europe seems to be very low and in Europe Vatican City is the country with the lowest population from all over the world, Moldova have the highest population growth rate of 1.069 and Ukraine is the country with lowest growth rate of 0.921.")
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

   
x = st.slider('Rate the usefulness of this application')  # 👈 this is a widget
st.text_area('Enter your comments please')

agree = st.checkbox('I agree to be contacted for new updates')

if agree:
 st.write('Great!')






