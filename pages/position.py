import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

import streamlit_analytics

with streamlit_analytics.track():
		
	st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
	
	def set_bg_hack_url():
	    '''
	    A function to unpack an image from url and set as bg.
	    Returns
	    -------
	    The background.
	    '''
	        
	    st.markdown(
	         f"""
	         <style>
	         .stApp {{
	             background: url("https://cdn.nba.com/manage/2021/03/NBA-All-Star-2021-Court-Design-scaled.jpg");
	             background-size: cover
	         }}
	         </style>
	         """,
	         unsafe_allow_html=True
	     )
	
	@st.cache_data  
	def load_data(pos):
		df = pd.read_csv("final.csv")
		df1 = df[df["position"] == pos]
	    
		return df1
	
	
	set_bg_hack_url()
	col = st.columns(25)
	row1 = st.columns(11)
	row2 = st.columns(11)
	row3 = st.columns(11)
	row4 = st.columns(11)
	row5 = st.columns(11)
	row6 = st.columns(11)
	row7 = st.columns(11)
	row8 = st.columns(11)
	row9 = st.columns(11)
	row10 = st.columns(11)
	row11 = st.columns(11)
	row12 = st.columns(11)
	row13 = st.columns(21)
	row14 = st.columns(11)
	row16 = st.columns(11)
	row17 = st.columns(11)
	row18 = st.columns(11)
	row19 = st.columns(11)
	row20 = st.columns(11)
	row21 = st.columns(11)
	row22 = st.columns(11)
	row23 = st.columns(11)
	row24 = st.columns(11)
	row25 = st.columns(11)
	with col[0]:
		st.markdown(
	       """
	        <style>
	        .stButton > button {
	            position: absolute;
	            top:0px;
	            left:0px;
	        }
	        </style>
	        """,
	        unsafe_allow_html=True
	    )
		if st.button("home", use_container_width=True):
			switch_page("app")###
	
	with row5[2]:
		if st.button("PG"):
			st.dataframe(load_data("Point Guard"))
	with row23[2]:
		if st.button("SG"):
	                st.dataframe(load_data("Shooting Guard"))
	with row5[8]:
		if st.button("SF"):
	                st.dataframe(load_data("Small Forward"))
	with row23[8]:
		if st.button("PF"):
	                st.dataframe(load_data("Power Forward"))
	with row13[10]:
		if st.button("C"):
	                st.dataframe(load_data("Center"))
