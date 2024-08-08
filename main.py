import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Streamlit app
st.markdown("<h1 style='text-align: center; color: #00698f;'>Paris Olympics 2024 Medal Count Visualization</h1>", unsafe_allow_html=True)

df = pd.read_csv(r"C:\Users\Sreeja\Downloads\DA\Olympics_data.csv")

# Check for the necessary columns
required_columns = ['medal_date', 'medal_type', 'name', 'gender', 'country', 'country_code', 'nationality', 'discipline', 'event', 'event_type']
if all(column in df.columns for column in required_columns):

    # Convert necessary columns to strings if they are not already
    df['medal_type'] = df['medal_type'].astype(str)
    df['country'] = df['country'].astype(str)

    # Group the medals by country and type
    medal_counts = df.groupby(['country', 'medal_type']).size().unstack(fill_value=0).reset_index()

    # Calculate the total number of medals for each country
    medal_counts['Total'] = medal_counts.iloc[:, 1:].sum(axis=1)

    # Bar Plot of Medal Counts
    st.header('Total Medals by Country')
    fig1, ax1 = plt.subplots(figsize=(12, 8))
    sns.barplot(x='country', y='Total', data=medal_counts, palette='viridis', ax=ax1)
    ax1.set_title('Total Medals by Country - Olympics 2024')
    ax1.set_xlabel('Country')
    ax1.set_ylabel('Total Medals')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90, fontsize=10)
    st.pyplot(fig1)

    # Stacked Bar Plot of Medal Types
    df_melted = medal_counts.melt(id_vars='country', value_vars=medal_counts.columns.drop(['country', 'Total']), var_name='Medal', value_name='Count')
    st.header('Medal Distribution by Country')
    fig2, ax2 = plt.subplots(figsize=(14, 10))
    sns.barplot(x='country', y='Count', hue='Medal', data=df_melted, palette=['#FFD700', '#C0C0C0', '#CD7F32'], ax=ax2)
    ax2.set_title('Medal Distribution by Country - Olympics 2024')
    ax2.set_xlabel('Country')
    ax2.set_ylabel('Medal Count')
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90, fontsize=10)
    st.pyplot(fig2)

    # Interactive Plot with Plotly
    st.header('Interactive Medal Distribution')
    fig3 = px.bar(df_melted, x='country', y='Count', color='Medal', title='Medal Distribution by Country - Olympics 2024',
                  labels={'Count': 'Medal Count', 'country': 'Country', 'Medal': 'Medal Type'},
                  color_discrete_map={'Gold': '#FFD700', 'Silver': '#C0C0C0', 'Bronze': '#CD7F32'})
    st.plotly_chart(fig3)
else:
    st.error(f"The CSV file must contain the following columns: {', '.join(required_columns)}")