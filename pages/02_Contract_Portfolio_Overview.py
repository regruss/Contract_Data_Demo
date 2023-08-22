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
st.set_page_config(page_title="Contract Portfolio Overview",layout="wide",page_icon=":bar_chart:")
# Insert into DF
contract_df = pd.read_csv(r'C:\Users\regru\Desktop\PDF_OCR\NegotiationAI_Example_Data\Sample_Data_Generation\Contract_Portfolio_DF.csv')
# Title
st.title(":bar_chart: Contract Language Portfolio Overview")

# Sidebar filtering
st.sidebar.header("Filters:")
fn = st.sidebar.multiselect("Search by File Name",options=contract_df['File_Name'].unique(),default=contract_df['File_Name'].iloc[0])
df_selection = contract_df.query("File_Name == @fn")
st.dataframe(df_selection)

# Sort DF
col = st.sidebar.multiselect("Select a Column",options=['Indemnity_Favorability','Patent_Favorability','Subject_Injury_Favorability'],default='Indemnity_Favorability')
val = st.sidebar.multiselect("Select Language Type(s)",options=['standard','sponsor','institution'],default='standard')
search_df = contract_df[contract_df[col[0]].isin(val[:])]
st.dataframe(search_df)

##################### Statistics ############################################
########## Indemnity
# Standard %
indem1 = len(contract_df[contract_df['Indemnity_Favorability'] == 'standard'].values)/len(contract_df)
# Institution %
indem2 = len(contract_df[contract_df['Indemnity_Favorability'] == 'institution'].values)/len(contract_df)
# Sponsor %
indem3 = len(contract_df[contract_df['Indemnity_Favorability'] == 'sponsor'].values)/len(contract_df)
########## Patents
# Standard %
pat1 = len(contract_df[contract_df['Patent_Favorability'] == 'standard'].values)/len(contract_df)
# Institution %
pat2 = len(contract_df[contract_df['Patent_Favorability'] == 'institution'].values)/len(contract_df)
# Sponsor %
pat3 = len(contract_df[contract_df['Patent_Favorability'] == 'sponsor'].values)/len(contract_df)
########## Subject Injury
# Standard %
sub1 = len(contract_df[contract_df['Subject_Injury_Favorability'] == 'standard'].values)/len(contract_df)
# Institution %
sub2 = len(contract_df[contract_df['Subject_Injury_Favorability'] == 'institution'].values)/len(contract_df)
# Sponsor %
sub3 = len(contract_df[contract_df['Subject_Injury_Favorability'] == 'sponsor'].values)/len(contract_df)

st.header('Language Overview')
# Plot
fig1 = px.pie(values=[indem1,indem2,indem3],names=['Standard Language','Institution Friendly','Sponsor Friendly'],title='<b>Indemnity</b>',color_discrete_sequence=["red", "green", "blue"],hole=0.3)
fig2 = px.pie(values=[pat1,pat2,pat3],names=['Standard Language','Institution Friendly','Sponsor Friendly'],title='<b>Patents</b>',color_discrete_sequence=["green", "blue", "red"],hole=0.3)
fig3 = px.pie(values=[sub1,sub2,sub3],names=['Standard Language','Institution Friendly','Sponsor Friendly'],title='<b>Subject Injury</b>',color_discrete_sequence=["green", "red", "blue"],hole=0.3)
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)