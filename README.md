# CS4 Task: Fire Risk Visualization


This repository contains a Python script for visualizing fire risk data for various houses. The script reads house locations and fire risk metrics from a CSV file and generates a scatter plot to represent fire intensity geographically.

## Project Structure

*   **`visualization.py`**: The main Python script that uses `pandas` and `matplotlib` to read the data and create the visualization.
*   **`houses_fire_risk.csv`**: A CSV file containing the dataset with information about different houses, their locations, and their associated fire risk levels.
*   **`package.json`**: A dependency file indicating the use of `@pyscript/core`, suggesting potential for web-based execution.

## Getting Started

### Prerequisites

To run the visualization script locally, you will need Python installed, along with the following libraries:
*   pandas
*   matplotlib

### Execution

To generate the visualization, run the script from your terminal:

```bash
python visualization.py
```

This will process the `houses_fire_risk.csv` file and display a scatter plot titled "Visualization of Houses at Risk of Fire by Intensity".

## Visualization Output

The script generates a scatter plot where each point represents a house.
*   **X-axis**: Longitude
*   **Y-axis**: Latitude
*   **Color**: The color of each point corresponds to the `Fire_Intensity (%)`, using a "hot" colormap. Yellow points indicate lower intensity, while red and black points indicate higher intensity.

## Data Schema (`houses_fire_risk.csv`)

The dataset contains the following columns:

| Column Name                  | Type    | Description                                                 |
| ---------------------------- | ------- | ----------------------------------------------------------- |
| **House_ID**                 | String  | A unique identifier for each house.                         |
| **Owner_Name**               | String  | The name of the house owner.                                |
| **Location**                 | String  | The general location or neighborhood of the house.          |
| **Latitude**                 | Float   | The geographical latitude of the house.                     |
| **Longitude**                | Float   | The geographical longitude of the house.                    |
| **House_Type**               | String  | The type of house (e.g., Apartment, Bungalow).              |
| **Fire_Risk_Level**          | String  | A categorical risk level (e.g., High, Medium, Low).         |
| **Fire_Intensity (%)**       | Integer | The estimated fire intensity as a percentage.               |
| **Last_Inspection**          | Date    | The date of the last fire safety inspection.                |
| **Distance_to_Water_Source (m)** | Integer | The distance in meters to the nearest water source.         |
