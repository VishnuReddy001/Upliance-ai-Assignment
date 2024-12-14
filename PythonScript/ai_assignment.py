import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"D:/upliance_ai_assignment/DataSets/Assignment.xlsx"
user_details = pd.read_excel(file_path, sheet_name="UserDetails.csv")
cooking_sessions = pd.read_excel(file_path, sheet_name="CookingSessions.csv")
order_details = pd.read_excel(file_path, sheet_name="OrderDetails.csv")

print(user_details.isnull().sum())
print(cooking_sessions.isnull().sum())
print(order_details.isnull().sum())

user_details.fillna("Unknown", inplace=True)

# Remove duplicates
user_details.drop_duplicates(inplace=True)
cooking_sessions.drop_duplicates(inplace=True)
order_details.drop_duplicates(inplace=True)

# Perform inner join on UserID
merged_data = pd.merge(user_details, cooking_sessions, on="User ID", how="inner")
merged_data = pd.merge(merged_data, order_details, on="User ID", how="inner")

print(merged_data.isnull().sum())
print(merged_data.describe())

merged_data['Age Group'] = pd.cut(merged_data['Age'], bins=[0, 18, 30, 40, 50, 100], labels=['<18', '18-30', '30-40', '40-50', '50+'])
print(merged_data['Age Group'].value_counts())

# Count users by Location
print(merged_data['Location'].value_counts())

print(merged_data.columns)
merged_data.columns = merged_data.columns.str.strip()
meal_type_count = merged_data['Meal Type_y'].value_counts()

# #KPI-1
#Distribution of user ages
plt.figure(figsize=(8,6))
sns.histplot(merged_data['Age'], kde=True, bins=20)
plt.title('Age Distribution of Users')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#KPI-2
plt.figure(figsize=(10,6))
meal_type_count.plot(kind='bar')
plt.title('Most Popular Meal Types')
plt.xlabel('Meal Type')
plt.ylabel('Frequency')
plt.show()

merged_data.to_csv("cleaned_merged_data.csv", index=False)
merged_data.to_excel("cleaned_merged_data.xlsx", index=False)

plt.figure(figsize=(10,6))
meal_type_count.plot(kind='bar')
plt.title('Most Popular Meal Types')
plt.xlabel('Meal Type')
plt.ylabel('Frequency')
plt.savefig('meal_type_count_plot.png')  # Save as PNG

plt.savefig('upliance-ai-final.png')

plt.savefig('D:/upliance_ai_assignment/plots/filename.png')
