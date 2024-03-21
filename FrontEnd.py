import streamlit as st
import pandas as pd
from datetime import date

# Set the title
st.title("Orderbook Frontend")

# Read the Excel file
df = pd.read_excel('W:/58430/04 Individual Folders/Marouan Mrait/Projects/Order book/OrderBook FrontEnd/Orderbook_T00.xlsx')

# Create a dropdown menu for selecting the planner
selected_planner = st.selectbox('Planner', df['RCName'].unique())

# Filter the dataframe based on the selected planner
planner_filtered_df = df[df['RCName'] == selected_planner]

# Button to save the filtered dataframe as an Excel file
if st.button('Send to all Suppliers'):
    # Generate the file name
    current_date = date.today().strftime('%d%m%Y')
    file_name = f"PACCAR Parts Europe Orderbook - {selected_planner} - {current_date}.xlsx"

    # Save the filtered dataframe as an Excel file
    output_path = 'W:/58430/04 Individual Folders/Marouan Mrait/Projects/Order book/OrderBook FrontEnd/Output/'
    file_path = output_path + file_name
    planner_filtered_df.to_excel(file_path, index=False)
    
    # Display success message
    st.write(f"File saved successfully: {file_name}")

# Display the filtered dataframe for Planner and the number of records
st.write(planner_filtered_df)
st.write(f"Number of records is: {len(planner_filtered_df)}")

# Create an entry field for the BVK code
entered_bvk = st.text_input('Enter BevoCode')

# Filter the dataframe based on the entered BVK code
bvk_filtered_df = df[df['BVK'] == entered_bvk]

# Display the filtered dataframe for BVK and the number of records
st.write(bvk_filtered_df)
st.write(f"Number of records is: {len(bvk_filtered_df)}")
