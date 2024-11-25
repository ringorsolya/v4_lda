import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    # Replace with your file path
    file_path = "ripost_lda_results_term.xlsx"

    
    # Load the Excel file
    terms_df = pd.read_excel(file_path, header=None)
    
    # Extract topic names from the first row
    topic_names = terms_df.iloc[0, :].tolist()  # First row contains topic names
    
    # Remove the first row and reset the dataframe
    terms_split = terms_df.iloc[1:, :]  # Remaining rows contain the terms
    terms_split.columns = topic_names  # Assign topic names as column headers
    
    return terms_split, topic_names

# Load data and topic names
terms_split, topic_names = load_data()

# Sidebar for Topic Selection
st.sidebar.title("Options")
topic_name = st.sidebar.selectbox("Select Topic", topic_names)  # Let user select a topic name

# Add a custom title with the corpus name
st.title(f"Word Cloud for {ripost.hu}")

# Word Cloud Visualization
st.header(f"Word Cloud for {topic_name}")
topic_terms = terms_split[topic_name].dropna().astype(str)  # Extract terms for the selected topic

# Combine terms into a single string for the word cloud
combined_terms = " ".join(topic_terms)

# Generate Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_terms)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

# Additional Notes
#st.write("Extend the dashboard by adding document-topic distributions or interactive visualizations.")
