import streamlit as st

st.title('REGISTRATION FORM')
name = st.text_input("ENTER YOUR NAME")
mname = st.text_input("ENTER YOUR MIDDLE NAME")
lname = st.text_input("ENTER YOUR LAST NAME")

adr = st.text_area("ENTER ADDRESS:" )
classdata = st.selectbox("ENTER YOUR CLASS:" ,(1,2,3,4,5,6,7,8,9))

button = st.button("DONE")
if button :
    st.markdown("FORM SUCCESSFUL CREATED")