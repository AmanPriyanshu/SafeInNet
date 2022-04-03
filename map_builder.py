import folium
import streamlit as st

@st.cache(hash_funcs={folium.folium.Map: lambda _: None}, allow_output_mutation=True)
def make_map(x=40.3430942, y=-74.6572626, display_all=True):
	if display_all:
		main_map = folium.Map(location=(x, y), zoom_start=16)
	return main_map