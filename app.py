import streamlit as st
import pandas as pd
import numpy as np

container = st.container(border=True)
st.markdown('<nav data-testid="stSidebarNav"> <ul data-testid="stSidebarNavItems""><li>page1</li><li>page2</li></ul></nav>', unsafe_allow_html = True)
col1, col2 = st.columns(2)
with col1:
    with st.form("my_form"): 
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

with col2:
    st.markdown('<p class="dashboard_title">Crypto<br>Dashboard</p>', unsafe_allow_html = True)


