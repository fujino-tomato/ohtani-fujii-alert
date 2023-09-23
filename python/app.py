import streamlit as st
from scrayping import fujii_scrayping

df = fujii_scrayping()
st.title("藤井聡太 戦績")
st.table(df)
