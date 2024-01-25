import streamlit as st

print("st.session_state")
print(st.session_state)
if not st.session_state:
    st.switch_page("app.py")

def logout():
    del st.session_state["password_correct"] 
    del st.session_state["email"]

st.write("Here goes your normal Streamlit app...")
st.button("log out", on_click=logout())