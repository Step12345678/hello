import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
import streamlit_analytics

with streamlit_analytics.track():
	st.markdown(
	         f"""
	         <style>
	         .stApp {{
	             
	             background-size: cover
	         }}
	         </style>
	         """,
	         unsafe_allow_html=True
	     )
	
	
	col = st.columns(10)
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
	        switch_page("app")
	
	st.title("Yearly stats")
	
	col = st.columns(10)
	row1 = st.columns(10)
	row2 = st.columns(10)
	row3 = st.columns(10)
	row4 = st.columns(10)
	row5 = st.columns(10)
	row6 = st.columns(10)
	row7 = st.columns(10)
	row8 = st.columns(10)
	row9 = st.columns(10)
	row10 = st.columns(10)
	row11 = st.columns(10)
	row12 = st.columns(10)
	row13 = st.columns(10)
	row14 = st.columns(10)
	row15 = st.columns(10)
	row16 = st.columns(10)
	row17 = st.columns(10)
	row18 = st.columns(10)
	row19 = st.columns(10)
	row20 = st.columns(10)
	
	@st.cache_data
	def data():
		df = pd.read_csv("yeardata.csv")
		return df
	
	with row1[1]:	
		if st.button("1985"):
			df1 = data()
			st.dataframe(df1[df1["draft_year"] == "1985"])	
	with row1[2]:
	        if st.button("1986"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1986"])
		
	with row1[3]:
	        if st.button("1987"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1987"])
	with row1[4]:
	        if st.button("1988"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1988"])
	with row1[5]:
	        if st.button("1989"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1989"])
	with row1[6]:
	        if st.button("1990"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1990"])
	with row1[7]:
	        if st.button("1991"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1991"])
	with row1[8]:
	        if st.button("1992"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1992"])
	with row1[9]:
	        if st.button("1993"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1993"])
	with row5[1]:
	        if st.button("1994"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1994"])
	with row5[2]:
	        if st.button("1995"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1995"])
	with row5[3]:
	        if st.button("1996"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1996"])
	with row5[4]:
	        if st.button("1997"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1997"])
	with row5[5]:
	        if st.button("1998"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1998"])
	with row5[6]:
	        if st.button("1999"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "1999"])
	with row5[7]:
	        if st.button("2000"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2000"])
	with row5[8]:
	        if st.button("2001"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2001"])
	with row5[9]:
	        if st.button("2002"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2002"])
	with row9[1]:
	        if st.button("2003"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2003"])
	with row9[2]:
	        if st.button("2004"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2004"])
	with row9[3]:
	        if st.button("2005"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2005"])
	with row9[4]:
	        if st.button("2006"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2006"])
	with row9[5]:
	        if st.button("2007"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2007"])
	with row9[6]:
	        if st.button("2008"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2008"])
	with row9[7]:
	        if st.button("2009"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2009"])
	with row9[8]:
	        if st.button("2010"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2010"])
	with row9[9]:
	        if st.button("2011"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2011"])
	with row13[9]:
	        if st.button("2012"):
	                df1 = data()
	                st.dataframe(df1[df1["draft_year"] == "2012"])
	
	
	
	
	
	
	
	
	
	
