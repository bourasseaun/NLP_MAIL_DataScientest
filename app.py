import streamlit as st
PAGE_CONFIG = {"page_title":"NLP_Mail.io","page_icon":":smiley:","layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)
def main():
	st.title("NLP Online formail")
	st.subheader("DifferentNLP for Datascientest")
	menu = ["Home","IA1","IA2","IA3"]
	choice = st.sidebar.selectbox('Menu',menu)
	if choice == 'Home':
		st.subheader("NLP for Datascientest")	
if __name__ == '__main__':
	main()
