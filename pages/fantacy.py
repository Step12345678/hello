import streamlit as st
import pandas as pd
import random
import streamlit_analytics

with streamlit_analytics.track():
    
    @st.cache_data
    def load_data():
        df = pd.read_csv('fantasy.csv')
        return df
    
    def calc_team_score(team, df1):
        totalteampoints = 0
        totalteamassists = 0
        totalteamturnovers = 0
        for player in team:
            playerdf = df1.loc[df1["Player"] == player]
            if not playerdf.empty:
                totalteampoints += playerdf["Total Points"].values[0]
                totalteamassists += playerdf["AST"].values[0]
                totalteamturnovers += playerdf["TOV"].values[0]
        if totalteamturnovers == 0:
            return totalteampoints  # Avoid division by zero
        teamratio = totalteamassists / totalteamturnovers
        totalteampoints = totalteampoints * teamratio
        return totalteampoints
    
    st.title('Welcome to the Fantasy Basketball')
    st.write('Select your team and play against the computer to see who wins.')
    st.write('''From the selector below, select 6 players to get a team score and then the computer generates its own team. 
    For the both generated teams, we compare the score and declare the winner.''')
    
    df2 = load_data()
    names = df2['Player'].tolist()
    
    if 'team2' not in st.session_state:
        st.session_state.team2 = random.sample(names, 6)
    
    col1 = st.columns(2)
    with st.form('my form'):
        with col1[0]:
            team1 = st.multiselect('Select your team', names, max_selections=6)
            st.write(team1)
        with col1[1]:
            if st.checkbox('Opposition Team'):
                select = st.empty()
                t2 = select.multiselect('Opposition Team', st.session_state.team2, default=st.session_state.team2)
                st.write(t2)
        submit = st.form_submit_button('Calculate Score')
        if submit:
            st.subheader('Each Team Description')
            col2 = st.columns(2)
            with col2[0]:
                pl1 = df2.loc[df2["Player"].isin(team1)]
                st.dataframe(pl1,hide_index=True)
            with col2[1]:
                pl2 = df2.loc[df2["Player"].isin(st.session_state.team2)]
                st.dataframe(pl2,hide_index=True)
            sc = calc_team_score(team1, df2)
            st.session_state.score1 = sc
            st.write(f'Your team score is: {st.session_state.score1}')
            sc2 = calc_team_score(t2, df2)
            st.session_state.score2 = sc2
            st.write(f'Opposition Team Score is: {st.session_state.score2}')
            if sc>sc2:
                st.balloons()
            if sc2>sc:
                st.snow()
    
    
    
