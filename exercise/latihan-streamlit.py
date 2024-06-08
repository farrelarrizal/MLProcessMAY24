import streamlit as st

st.title('Halo Semuanya!?')
st.header('This is the welcome page')

st.image('https://disk.mediaindonesia.com/files/news/2022/12/30/WhatsApp%20Image%202022-12-22%20at%2017.03.14.jpg', caption='Awesome sunrise', width = 200)

with st.form(key="my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")
   name = st.text_input('Input your name', help='maximum 20 chars')

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)
       st.write(f'Hi, {name} happy saturday!')

st.write("Outside the form")