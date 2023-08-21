# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:00:52 2023

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



# https://streamlit.io/gallery
# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
def main():
    st.set_page_config(page_title="CTA Data Extraction",page_icon=":house:")
    st.header("Extract Data From Your Contracts")
    pdf_files = st.file_uploader("Upload Files", accept_multiple_files=True, type="pdf")
    # Extract Data
    if bool(pdf_files):
        st.header('Contract Data Preview')
        # Insert into DF
        contract_df = pd.read_csv(r'C:\Users\regru\Desktop\PDF_OCR\NegotiationAI_Example_Data\Sample_Data_Generation\Contract_Portfolio_DF.csv')
        budget_df = pd.read_csv(r'C:\Users\regru\Desktop\PDF_OCR\NegotiationAI_Example_Data\Sample_Data_Generation\Budget_Portfolio_DF.csv')
        st.write(contract_df.head())
        st.header('Budget Data Preview')
        st.write(budget_df.head())
if __name__== '__main__':
    main()






#############################################################################################################
#############################################################################################################
#############################################################################################################
###################################### Testing ##############################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################





























