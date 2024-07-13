import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import streamlit_analytics

with streamlit_analytics.track():
         
         st.markdown(
                  f"""
                  <style>
                  .stApp {{
                      background: url("https://fadeawayworld.net/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTgwMTMyNzAxOTQ4MDI4MDI2/top-10-greatest-leaders-in-nba-history.jpg");
                      background-size: cover
                  }}
                  </style>
                  """,
                  unsafe_allow_html=True
              )
         
         #st.set_page_config(layout="wide")
         col = st.columns(10)
         with col[0]:
             if st.button("home", use_container_width=True):
                 switch_page("app")
         background_image = 'https://fadeawayworld.net/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTgwMTMyNzAxOTQ4MDI4MDI2/top-10-greatest-leaders-in-nba-history.jpg'
         
         # Load the data
         df = pd.read_csv("final.csv")
         
         # Display Points Leaders
         st.subheader("Points Leaders")
         points_df = df[['name', 'career_PTS']]
         st.dataframe(points_df.sort_values(by=["career_PTS"],ascending = False))
         
         # Display Rebounds Leaders
         st.subheader("Rebounds Leaders")
         rebounds_df = df[['name', 'career_TRB']]
         st.dataframe(rebounds_df)
         
         # Display Assists Leaders
         st.subheader("Assists Leaders")
         assists_df = df[['name', 'career_AST']]
         st.dataframe(assists_df)
         
         # Display Player Efficiency Rating Leaders
         st.subheader("Player Efficiency Rating (PER) Leaders")
         per_df = df[['name', 'career_PER']]
         st.dataframe(per_df)
         
         # Display Field Goal Percentage Leaders
         st.subheader("Field Goal Percentage (FG%) Leaders")
         fg_df = df[['name', 'career_FG%']]
         st.dataframe(fg_df)
         
         # Display Three-Point Field Goal Percentage Leaders
         st.subheader("Three-Point Field Goal Percentage (FG3%) Leaders")
         fg3_df = df[['name', 'career_FG3%']]
         st.dataframe(fg3_df)
         
         # Display Free Throw Percentage Leaders
         st.subheader("Free Throw Percentage (FT%) Leaders")
         ft_df = df[['name', 'career_FT%']]
         st.dataframe(ft_df)
         
         # Display Win Shares Leaders
         st.subheader("Win Shares (WS) Leaders")
         ws_df = df[['name', 'career_WS']]
         st.dataframe(ws_df)
         
         
          
