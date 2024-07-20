import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit_analytics

with streamlit_analytics.track():
         
         st.markdown(
                  f"""
                  <style>
                  .stApp {{
                      background: url("https://img.freepik.com/premium-photo/rainy-night-basketball-closeup-urban-sports-atmosphere_916860-4819.jpg");
                      background-size: cover
                  }}
                  </style>
                  """,
                  unsafe_allow_html=True
              )
         
         #st.set_page_config(layout="wide")
         col = st.columns(10)
         background_image = 'https://fadeawayworld.net/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTgwMTMyNzAxOTQ4MDI4MDI2/top-10-greatest-leaders-in-nba-history.jpg'
         
         # Load the data
         df = pd.read_csv("final.csv")
         with col[0]:
             if st.button("home", use_container_width=True):
                 switch_page("app")
                  # Display Points Leaders
                  st.subheader("Points Leaders")
                  points_df = df[['name', 'career_PTS']]
                  st.dataframe(points_df.sort_values(by=["career_PTS"],ascending = False))
         with col[1]:
                  # Display Rebounds Leaders
                  st.subheader("Rebounds Leaders")
                  rebounds_df = df[['name', 'career_TRB']]
                  st.dataframe(rebounds_df.sort_values(by=["career_TRB"],ascending = False))

         with col[2]:
                  # Display Assists Leaders
                  st.subheader("Assists Leaders")
                  assists_df = df[['name', 'career_AST']]
                  st.dataframe(assists_df.sort_values(by=["career_AST"],ascending = False))
         
         # Display Player Efficiency Rating Leaders
         st.subheader("Player Efficiency Rating (PER) Leaders")
         per_df = df[['name', 'career_PER']]
         st.dataframe(per_df.sort_values(by=["career_PER"],ascending = False))
         
         # Display Field Goal Percentage Leaders
         st.subheader("Field Goal Percentage (FG%) Leaders")
         fg_df = df[['name', 'career_FG%']]
         st.dataframe(fg_df.sort_values(by=["career_FG%"],ascending = False))
         
         # Display Three-Point Field Goal Percentage Leaders
         st.subheader("Three-Point Field Goal Percentage (FG3%) Leaders")
         fg3_df = df[['name', 'career_FG3%']]
         st.dataframe(fg3_df.sort_values(by=["career_FG3%"],ascending = False))
         
         # Display Free Throw Percentage Leaders
         st.subheader("Free Throw Percentage (FT%) Leaders")
         ft_df = df[['name', 'career_FT%']]
         st.dataframe(ft_df.sort_values(by=["career_FT%"],ascending = False))
         
         # Display Win Shares Leaders
         st.subheader("Win Shares (WS) Leaders")
         ws_df = df[['name', 'career_WS']]
         st.dataframe(ws_df.sort_values(by=["career_WS"],ascending = False))
         
         
          
