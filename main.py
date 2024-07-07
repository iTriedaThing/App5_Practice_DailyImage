import requests
import streamlit as st


api_key = 'NBMpF3xlJykDnRCcEoXudPXucBTCOZGC7og9U8yx'
api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

# get the response from the NASA API and parse it
response = requests.get(url=api_url)
content = response.json()

# create the web page
st.set_page_config(layout='wide')

# write the title to the web page
st.header(content['title'])

# write the image to the web page
st.image(content['url'])

# write the explanation to the web page
st.write(content['explanation'])
