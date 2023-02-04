import streamlit as st

import fastf1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd
 
#Sidebar
st.sidebar.title("Instructions:")
st.sidebar.markdown("1. ")
st.sidebar.markdown("2. ")
st.sidebar.markdown("3. ")
st.sidebar.markdown("4. ")

#Main Page
st.title("Formula One Studio")
tabs = st.tabs(["Note","Main Page"])

tab_note = tabs[0]

with tab_note:
    telemetry_data = fastf1.load_data(2022, round_number)
    st.write(telemetry_data)
    st.line_chart(telemetry_data)
