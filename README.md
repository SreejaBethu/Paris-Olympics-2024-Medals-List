# Paris Olympics 2024 Medal Count Visualization**

## Overview
This project visualizes the medal counts for countries participating in the Paris Olympics 2024 using Streamlit, Seaborn, Matplotlib, and Plotly.

## Features
- **Total Medals by Country**: Bar plot showcasing the total medals won by each country.
- **Medal Distribution by Country**: Stacked bar plot of gold, silver, and bronze medals.
- **Interactive Medal Visualization**: Dynamic Plotly chart for exploring medal distribution.

## Technologies
- **Python**
- **Pandas**
- **Seaborn**
- **Matplotlib**
- **Plotly Express**
- **Streamlit**

## Data
The data is stored in a CSV file (`Olympics_data.csv`) with columns for medal date, type, athlete's name, gender, country, nationality, discipline, event, and event type.

## Running the Application
cd paris-olympics-2024-medal-visualization
pip install -r requirements.txt
streamlit run app.py

**Project Structure**

    app.py: Main script for the application.
    Olympics_data.csv: Dataset with the Olympics medal information.
    requirements.txt: Dependencies list.

**Future Enhancements**

    Add country and date filters.
    Include athlete details.
