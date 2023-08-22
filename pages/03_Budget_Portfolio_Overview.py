# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:26:45 2023

@author: regru
"""
import os
import json
import numpy as np
import pandas as pd
import time
import spacy
import openai
import glob
import re
import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io
from PyPDF2 import PdfReader
from IPython.display import display
import streamlit as st
import plotly.express as px



# https://streamlit.io/gallery
# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Budget Portfolio Overview",layout="wide",page_icon=":bar_chart:")
# Insert into DF
budget_df = pd.read_csv(r'Budget_Portfolio_DF.csv')
# DF Overview Title
st.title(":bar_chart: Budget Portfolio Overview")
st.subheader('Main Data Frame')
# Sidebar filtering
st.sidebar.header("Filters:")
fn = st.sidebar.multiselect("Select Contract to View Data",options=budget_df['Contract_Name'].unique(),default=budget_df['Contract_Name'].iloc[0])
df_selection = budget_df.query("Contract_Name == @fn")
st.dataframe(df_selection)


# Percentiles
st.subheader('Percentiles')
budget_pcts_df = pd.DataFrame(columns=['Patient_Count', 'Overhead_Rate', 'Total_Cost','Per_Site_OH', 'Conditional_OH', 'Startup_OH', 'Expected_Revenue','SG&A', 'Total_Negotiation_Days', 'NPV10'])
for col in budget_pcts_df.columns:
    budget_pcts_df[col] = budget_df[col].rank(pct=True)
budget_pcts_df['Contract_Name'] = budget_df['Contract_Name']
budget_pcts_df = budget_pcts_df[['Contract_Name','Patient_Count', 'Overhead_Rate', 'Total_Cost','Per_Site_OH', 'Conditional_OH', 'Startup_OH', 'Expected_Revenue','SG&A', 'Total_Negotiation_Days', 'NPV10']]
# Percentile DF
df_pct_selection = budget_pcts_df.query("Contract_Name == @fn")
st.dataframe(df_pct_selection)
# Sort DF
col = st.sidebar.multiselect("Select Column to Sort by",options=['Patient_Count', 'Overhead_Rate', 'Total_Cost','Per_Site_OH', 'Conditional_OH', 'Startup_OH', 'Expected_Revenue','SG&A', 'Total_Negotiation_Days', 'NPV10','Proposal_Date','Target_Close_Date'],default='Total_Cost')
if bool(col):
    st.subheader('Sort Data')
    sorted_df = budget_df.sort_values(by=col[:],ascending=False)
    st.dataframe(sorted_df)

####################################
# Distributions Title

# Sidebar filtering
fn = st.sidebar.multiselect("Select Column to View Histogram",options=['Patient_Count', 'Overhead_Rate', 'Total_Cost',
       'Per_Site_OH', 'Conditional_OH', 'Startup_OH', 'Expected_Revenue','SG&A', 'Total_Negotiation_Days', 'NPV10'],default=['Total_Cost'])
if bool(fn):
    st.subheader('Distributions')
    hist_chart = px.histogram(budget_df,x=fn,nbins=int(len(budget_df)/4))
    hist_chart.add_vline(x=np.mean(budget_df[fn].values), line_dash = 'dash', line_color = 'firebrick')
    st.plotly_chart(hist_chart)








