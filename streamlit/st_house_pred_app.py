import numpy as np
import streamlit as st
import PIL
import datetime
import time
import plotly.express as px
import pandas as pd

st.title("My app Title 🎉")

st.header("I am using a header. See below a subheader")

st.subheader("Subheader here 🙋🏽‍♂️")

st.markdown("""I can write in markdown format. Observe: 

# Header Nro1

## Header Nro 2

### Header Nro 3

#### Header Nro 4

* **Bullet**

* *Bullet* 2

> Indented line

~~Weird symbol~~

---

* [Last bullet](www.google.com)
""")

st.text("I am the most simple text")


st.success("Congrats. u know how to use success ✔")

st.info("Here I would display some info 💬")

st.warning("Here I would display a warning ⚠")

st.error("Displaying my custom error 🚫")

st.exception("Exception encountered: No name 'careticulium' found")

st.help(map)

st.write(""" 
We can also write in markdown with st.write (superfunction)
# A Prediction App
This app predicts the **AMOUNT CHOCOLATE** you will eat !
Data obtained from the somewhere.
""")
st.write(range(10))
st.write("# See below some examples of image, vid and audio displayed in Streamlit")
img = PIL.Image.open("Screenshot 2021-03-02 102415.png")
vid = open("vid.mp4", "rb").read()
aud = open("song.mp3", "rb").read()

st.image(img, width=300, caption="Screenshot Caption")
st.video(vid)
st.audio(aud, format="audio/mp3")


st.write("# see below a check box, check circle, select box, multiselect box, slider, "
         "button, text input in Streamlit")

# check box
if st.checkbox("Click Here for info"):
    st.text("Showing or Hiding Text")
    st.info("Today is gona be sunny")
# radio box
hungryness = st.radio("Are you hungry", ("Yes", "No"))
if  hungryness == "Yes":
    st.success("Go and eat a nice burger")
# if hungryness == "No":
else:
    st.warning("Do some nice exercise")

# select box
st.text("Select Box")
sport = st.selectbox("Select your favourite sport", ["Football", "Tennis", "Basketball", "Baseball", "Ping-Pong", "Badminton"])

st.write("You chose {}".format(sport))

# multiselect box
st.text("Multiselect box")
sports = st.multiselect("Select your favourite sports", ["Football", "Tennis", "Basketball", "Baseball", "Ping-Pong", "Badminton"])

st.write("You chose {}".format(", ".join(sports)))

# select slider
st.text("Select Slider")
sport_levels = st.select_slider("Select your level", ["Low", "Medium", "High", "Semi-Pro", "Professional"])
st.write("Your level is {}".format(sport_levels))


# slider
st.text("Slider")
years_played = st.slider("How many years have you played this sport", 1, 80, 1)


# button very uselful with if statements
st.text("Button")
butoon = st.button("About")

if butoon: # once the button is click
    st.text("This is my first app to ckeck some of the Streamlit functionalities")

# number input
st.text("Number Input")
st.number_input("You can input a number here")

# text input
fav_player = st.text_input("What is your favourite player?:", "Type here")

response = st.write("Your favourite player is {}". format(fav_player))

# text area
fav_players = st.text_area("What is your favourite players?:", "Type here")

response = st.write("Your favourite players are {}". format(fav_players))

st.write("# Displaying date, time, json code, raw code, all code in Streamlit")

# date, time input
st.text("Date Input")
today = st.date_input("Choose the time here", datetime.datetime.now())
st.text("Time Input")
time_ = st.time_input("Choose the time here", datetime.time())

# json, raw code, all code
st.text("Json fornat")
st.json({'name': "Pancer", 'nationality': "German", 'code': "Json"})
st.text("COde Format")
st.code({'name': "Pancer", 'nationality': "German", 'code': "Json"})
st.code("import pandas as pd")

with st.echo():
    # This will also show as a comment
    import seaborn as sns
    import sklearn

st.write("# Displaying bar progress, spinner, ballons in Streamlit")

# progress bar
st.text("Progress Bar")
progress_bar = st.progress(0)
for p in range(100):
    time.sleep(0.01)
    progress_bar.progress(p + 1)

# spinner
st.text("Spinner")
with st.spinner("Sleeping .."):
    time.sleep(3)
st.success("Finished!")

# balloons
st.balloons()

# sidebar
st.write("# Displaying sidebar, functions in Streamlit")

st.sidebar.header("Header Sidebar")
st.sidebar.text("In this sidebar we can place user inputs for instance")

# multiselect box at side bar
st.sidebar.text("Multiselect box")
variable = 123
sports=[variable, "Football", "Tennis", "Basketball", "Baseball", "Ping-Pong", "Badminton"]
st.sidebar.multiselect("Select your favourite sports",sports, sports)


@st.cache # we can use it to save the result
def run_fxn():
    return range(100)

st.write(run_fxn())

st.write("# Displaying df, table, plots in Streamlit")
# plots, dataframes and tables

# read a csv
df_map = pd.read_csv("df_map.csv") 

def plot_func(df):
    # make a plot 
    plot = px.scatter_geo(data_frame=df, 
                          title="2nd Hand Cars in Spain",
                          lat="latitud", 
                          lon="longitud", 
                          size="number_cars",
                          size_max=30,
                          #text = "comunidad",
                          color = "price(€)",
                          color_continuous_scale="Jet",
                          range_color = (6000,18000),
                          hover_name = "region",
                         hover_data = ["price(€)","years_old", "horse_power", "population_region", 
                                       "percentage_professional", "adds_per_1000_people", "km", "km/year"],
                         projection = "aitoff",
                          scope = "europe",
                          width = 800,
                          height = 600,
                          template= "ggplot2") 

    return st.plotly_chart(plot, use_container_width=True) # for plotly


# OTHER PLOT COMMANDS
# st.pyplot(fig) for sns and plt
# st.bokeh_chart(p, use_container_width=True)
# st.bar_chart(chart_data) # plotting directly a barchart
# st.area_chart(chart_data) # plotting directly a areachart
# st.line_chart(chart_data) # plotting directly a linechart
# st.map(df)

if st.checkbox("Make plot "):
    plot_func(df_map)

st.text("df head showing")
st.dataframe(df_map.head())

#
st.table(df_map) # ⚠ high memory demand

st.write("# Using beta_ functionality in Streamlit")

# You can use "with" notation to insert any element into a column:

col1, col2, col3 = st.beta_columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", use_column_width=True)

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", use_column_width=True)

   
# Or you can just call methods directly in the returned objects:

col1, col2 = st.beta_columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)