import pandas as pd
import matplotlib.pyplot as plt


# Note: I used my own dummy data, and this code loads it
df = pd.read_csv("Houses_dataset.csv", encoding="latin-1")
print(df.columns)


# Scatter plot: Fire intensity by location
plt.figure(figsize=(10, 6))
sc = plt.scatter(df['Longitude'], df['Latitude'], 
                 c=df['Fire Intensity Level'], cmap='hot', s=120, edgecolors='black')
plt.colorbar(sc, label="Fire Intensity Level")
plt.title("Visualization of Houses at Risk of Fire by Intensity")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
