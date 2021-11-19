import streamlit as st
import datetime as dt
import requests
'''
# NYC Taxi Fares
'''

st.markdown('''
### You can use this website to find out how much a taxi ride costs around The Big 🍎
''')
'''
## Please enter your location and your destination 🚕 '''

d = st.date_input(
    "When do you want to travel?",
    dt.date(2019, 7, 6))

t = st.time_input('At what time?', dt.time(8, 45))

pickup_longitude = st.text_input('Enter your pick-up longitude', '-73.9918926')
pickup_latitude = st.text_input('Enter your pick-up latitude', '40.7410605')
dropoff_longitude = st.text_input('Enter your drop-off longitude',
                                 '-73.9878584')
dropoff_latitude = st.text_input('Enter your drop-off latitude',
                                 '40.7484405')

passengers = st.selectbox('How many passengers will be traveling?', range(1,7))

#Trying to improve the UI by only asking the user to input location, currently not working
#map_url = 'https://nominatim.openstreetmap.org/search'
#location_response = requests.get(map_url).json()

pickup_datetime = dt.datetime.combine(d, t)
url = 'https://taxifare.lewagon.ai/predict'

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude ,
    "passenger_count": passengers,
}

response = round(requests.get(url,params = params).json()['prediction'],2)

'''
## This is how much you're expected to pay for this trip 💸💸 :
'''
st.metric('',f'${response}')
