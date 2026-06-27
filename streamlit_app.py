import streamlit as st
import subprocess

st.title("Zapia Persistent Terminal")

if "history" not in st.session_state:
    st.session_state.history = ""

command = st.text_input("Enter command:")

if st.button("Run"):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = f"$ {command}\n{result.stdout}\n{result.stderr}"
        st.session_state.history += "\n" + output
    except Exception as e:
        st.error(f"Error: {e}")

st.text_area("Terminal Output", value=st.session_state.history, height=400)
