# Paris Olympics 2024 Medal Count Visualization
This project visualizes the medal counts for countries participating in the Paris Olympics 2024 using Streamlit, Seaborn, Matplotlib, and Plotly.

## Overview

-[Features](#features)

-[Technologies](#technologies)

-[Data](#data)

-[Project structure](#project-structure)

-[Running the application](#running-the-application)

-[Visualization](#visualization)

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

## Project Structure

    app.py: Main script for the application.
    Olympics_data.csv: Dataset with the Olympics medal information.
    requirements.txt: Dependencies list.

## Running the Application

cd paris-olympics-2024-medal-visualization
pip install -r requirements.txt
streamlit run app.py

## Visualization
![Screenshot (15)](https://github.com/user-attachments/assets/e4a0ffde-a6bf-463d-b419-d385d91e74eb)

![Screenshot (16)](https://github.com/user-attachments/assets/d830118a-40fe-448d-ba6b-1526488d5aef)

![Screenshot (17)](https://github.com/user-attachments/assets/d45356ea-a182-47a9-9378-af47a8b66597)





**Future Enhancements**

    Add country and date filters.
    Include athlete details.
