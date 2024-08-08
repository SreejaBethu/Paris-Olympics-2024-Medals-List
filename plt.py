import matplotlib.pyplot as plt
import seaborn as sns

# Load the medal count data from CSV
medal_count_data = pd.read_csv('C:/Users/Sreeja/Downloads/DA/medals_total.csv')

# Visualize the medal count data using a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='Medal Count', data=medal_count_data)
plt.title('Medal Count by Country in Olympics 2024')
plt.xlabel('Country')
plt.ylabel('Medal Count')
plt.show()