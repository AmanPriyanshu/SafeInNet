from map_builder import make_map
from streamlit_folium import folium_static
import streamlit as st
import folium
from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
from Reviews import get_reviews
from Ratings import get_ratings_bar
import os
from twilio.rest import Client

geolocator = Nominatim(user_agent="geoapiExercises")

project_name = "SafeInNet"
mission = "Here, we present to you SafeInNet, a dynamic social network to help women determine the safest roads and prevent their journey from being full of despair!"
base_loc = (40.6635697,-73.9299531)

def update_sidebar(x=None, y=None, max_len=60):
	if x is None:
		x, y = base_loc[0], base_loc[1]
	reviews = get_reviews(x, y, N=5)
	with st.sidebar:
		img_col, company_name_col = st.columns([4, 11])
		img_col.image('logo.jpg', use_column_width=True)
		rating_bar_path = get_ratings_bar(x, y, [i[1] for i in reviews])
		company_name_col.title("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+project_name)
		company_name_col.write(mission)
		st.title("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Safety Score")
		st.image(rating_bar_path)
		st.title("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Latest Reports")
		for index, (review, score) in enumerate(reviews):
			if len(review)>max_len:
				review = review[:max_len]+"..."
			with st.expander("", expanded=True):
				col1, col2 = st.columns([4, 1])
				with col1:
					if score>0.5:
						st.success(review)
					else:
						st.error(review)
				with col2:
					st.info(str(round(score*100, 1))+"%")

def update_map(placeholder_map, x, y):
	with placeholder_map.container():
			location = geolocator.reverse(str(x)+","+str(y))
			st.write(location)
			main_map = make_map(x, y)
			folium_static(main_map)

def app():
	st.markdown(
	"""
	<style>
	[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
	width: 500px;
	}
	[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
	width: 500px;
	margin-left: -500px;
	}
	</style>
	""",
	unsafe_allow_html=True
	)
	update_sidebar()
	_, col1, col2, _ = st.columns(4)
	with col1:
		x = st.text_input("X-Coordinate", value=str(base_loc[0]))
		try:
			x = float(x)
		except:
			st.error("Please enter appropriate value(/s). Eg: X="+str(base_loc[0])+", Y="+str(base_loc[1]))
	with col2:
		y = st.text_input("Y-Coordinate", value=str(base_loc[1]))
		try:
			y = float(y)
		except:
			st.error("Please enter appropriate value(/s). Eg: X="+str(base_loc[0])+", Y="+str(base_loc[1]))
	_, center_col, _ = st.columns([1.55, 1, 1])

	with center_col:
		submit = st.button("Search")

	placeholder_map = st.empty()
	update_map(placeholder_map, x, y)
	if submit:
		update_map(placeholder_map, x, y)		

	street_rating = st.slider("Rate the Street:", min_value=0, max_value=5, step=1)
	review = st.text_area("Comment/Review Street:", height=10)
	phone_no = st.text_input("Enter your phone number:", value="+91 1234567890")
	name = st.text_input("Enter your name:")
	if st.button("Submit Record"):
		phone_no = [i.strip() for i in phone_no.split() if i!='']
		if len(phone_no)==2 and phone_no[0][0]=='+' and len(phone_no[1])==10:
			if review.strip()!='':
				review_df = pd.DataFrame({"comment":[review], "lat":[x], "long": [y]})
				review_df.to_csv("./data/user_data.csv", index=False, mode="a", header=False)
			rating_df = pd.DataFrame({"rating": [street_rating], "lat": [x], "long": [y]})
			rating_df.to_csv("./data/user_ratings.csv", index=False, mode="a", header=False)
			phone_no_df = pd.read_csv('./data/phone_no.csv')
			phone_no_df = phone_no_df.values
			numbers = [i for i in phone_no_df.T[1]]
			phone_no = ''.join(phone_no)
			if phone_no not in numbers:
				phone_no_df = pd.DataFrame({"name":[name], "phone_no": [phone_no], "lat": [x], "long": [y]})
				phone_no_df.to_csv("./data/phone_no.csv", index=False, mode="a", header=False)
			else:
				update_sidebar()
				st.success("Successfully Recorded")
		else:
			st.error("Please enter a valid phone number!")
	if st.button("Send SOS!"):
		phone_no_df = pd.read_csv('./data/phone_no.csv')
		phone_no_df = phone_no_df.values
		phone_no_df.T[1] = [str(i) for i in phone_no_df.T[1]]
		numbers = [i.replace(" ", "").strip() for i in phone_no_df.T[1]]
		if len(numbers)>0:
			client = Client(st.secrets["TWILIO_ACCOUNT_SID"], st.secrets["TWILIO_AUTH_TOKEN"])
			for number in numbers:
				message = client.messages.create(to='+'+str(number), from_="+17652751440", body="A member of SafeInNet community is in trouble and requires your help! SOS message at loc:"+str(x)+","+str(y))
		else:
			st.write("No registerations so far!")








if __name__ == '__main__':
	app()