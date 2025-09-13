import pandas as pd
import matplotlib.pyplot as plt


# Note: I used my own dummy data, and this code loads it
df = pd.read_csv("houses_fire_risk.csv", encoding="latin-1")

# Scatter plot: Fire intensity by location
plt.figure(figsize=(10, 6))
sc = plt.scatter(df['Longitude'], df['Latitude'], 
                 c=df['Fire_Intensity (%)'], cmap='hot', s=120, edgecolors='black')
plt.colorbar(sc, label="Fire Intensity (%)")
plt.title("Visualization of Houses at Risk of Fire by Intensity")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
