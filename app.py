
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit_analytics


with streamlit_analytics.track():
	st.markdown('''
    	<style>
    	.st-emotion-cache-1jzia57.e1nzilvr2 #danger-zone
    	{
        display: none;
    	}
    	.st-emotion-cache-p5msec.eqpbllx1
    	{
        display: none;
    	}
    	</style>
    	''',unsafe_allow_html=True)
	st.title("PER vs Salary")
	st.image("palm-tree-sunset-basketball-hoop-hwnjg9y6ee0i1ppj.jpg")
	st.markdown("""
	This site was created using HTML, python and streamlit to show idetify the correlation between Salary and PER (player efficiency rating).It is claimed that great players have a high PER and get paid more. Let's find out if this is true... 
	
	""")
	col = st.columns(4)
	with col[0]:
		if st.button("Yearly stats"):
			switch_page("yearly")
	with col[1]:
		if st.button("Stats leaderboard"):
			switch_page("leaderboard")
	with col[2]:
		if st.button("Position Stats"):
			switch_page("position")
	with col[3]:
		if st.button("Fantasy"):
			switch_page("fantc")
	st.write("---")
	st.header("About me!")
	
	st.image("IMG_1390.jpg")
	st.markdown("""
	I am a basketball player of many years, my love for maths and sports specifically basketball has lead me to create this website to express a new cool i$
	""")
	st.header("Get in touch with me!")
	
	
	contact_form = """
	<form action="https://formsubmit.co/raitanay@gmail.com" method="POST">
	     <input type="hidden" name="_captcha" value="false">
	     <input type="text" name="name" placeholder = "Your name" required>
	     <input type="email" name="email" placeholder = "Your email" required>
	     <textarea name="message" placeholder="Your message here"></textarea>
	     <input type="submit" value"Send">
	</form>
	"""
	st.markdown(contact_form,unsafe_allow_html=True)
	
	with open("style.css") as f:
		st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
	
	
