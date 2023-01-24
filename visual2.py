import pandas as pd
import streamlit as st

final = pd.read_csv("stringency_final.csv")
opt = list(final["State_Code"].unique())
series = st.selectbox("Select State",options=opt)
data = final[final["State_Code"]==series]
st.line_chart(data=data,x="Date",y=["StringencyIndex"])
