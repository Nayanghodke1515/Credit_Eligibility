import streamlit as st
import sys
import os

# Allow imports from src folder
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

st.set_page_config(page_title="Credit Eligibility App")

st.title("Credit Eligibility Application")
st.write("ML Code Deployment – Streamlit Cloud")

# Import main logic
import main

if hasattr(main, "main"):
    main.main()
else:
    st.error("main() function not found in main.py")
