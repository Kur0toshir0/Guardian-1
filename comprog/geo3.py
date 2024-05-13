import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
# Disable a specific warning
warnings.filterwarnings("ignore", category=UserWarning)
st.set_option('deprecation.showPyplotGlobalUse', False)

def generate_sample_soil_strength_data(num_samples, sustainability_percentage):
    # Generate sample soil strength data based on sustainability percentage
    np.random.seed(0)
    depth = np.linspace(0, 10, num_samples)
    # Calculate strength based on sustainability percentage
    strength = (np.random.randint(40, 100, size=num_samples) * sustainability_percentage) / 100
    df = pd.DataFrame({"Depth (m)": depth, "Strength (kN/m^2)": strength})
    return df

def visualize_soil_strength_data(df):
    st.header("Sample Soil Strength Data Visualization")

    # Plot soil strength data
    plt.figure(figsize=(10, 6))
    plt.plot(df["Depth (m)"], df["Strength (kN/m^2)"], marker='o', linestyle='-')
    plt.title("Sample Soil Strength vs. Depth")
    plt.xlabel("Depth (m)")
    plt.ylabel("Strength (kN/m^2)")
    st.pyplot()

def main():
    st.title("Sample Soil Strength Data Generator")

    num_samples = st.slider("Number of Samples", min_value=10, max_value=100, value=50, step=1)
    sustainability_percentage = st.slider("Soil Sustainability Percentage", min_value=0, max_value=100, value=70, step=1)

    df = generate_sample_soil_strength_data(num_samples, sustainability_percentage)
    visualize_soil_strength_data(df)

if __name__ == "__main__":
    main()


    # Generate non-random hazard map data
    
def generate_hazard_map(size=10, success_percentage=70):
    # Initialize hazard map array
    hazard_map = np.zeros((size, size))
    
    # Generate hazard levels based on success percentage
    for i in range(size):
        for j in range(size):
            if np.random.randint(1, 101) <= success_percentage:
                hazard_map[i, j] = np.random.rand()  # Assign a random hazard level
            else:
                hazard_map[i, j] = 0  # No hazard
    
    return hazard_map

def plot_hazard_map(hazard_map):
    # Plot hazard map
    plt.figure(figsize=(8, 6))
    plt.imshow(hazard_map, cmap='hot', origin='lower')
    plt.colorbar(label='Hazard Level')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Hazard Map Visualization')
    st.pyplot()

def main():
    st.title('Hazard Map Visualization')
    
    # Define success percentage
    success_percentage = st.slider("Select Success Percentage", 0, 100, 70)

    hazard_map = generate_hazard_map(size=10, success_percentage=success_percentage)
    
    plot_hazard_map(hazard_map)

# Run the app
if __name__ == "__main__":
    main()
