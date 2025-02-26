mport streamlit as st
import pandas as pd

# Sample data
data = {
    "Technology": [
        "Solar Panels",
        "Wind Turbines",
        "Electric Vehicles",
        "Hydroelectric Power",
        "Geothermal Energy"
    ],
    "Carbon Emission Reduction (tons CO2/year)": [
        50,
        100,
        20,
        150,
        75
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Green Technologies and Carbon Emission Reductions")

st.write("""
This app displays a list of green technologies and their estimated carbon emission reductions.
""")

# Display the DataFrame
st.dataframe(df)

# Bar chart
st.bar_chart(df.set_index("Technology"))

# Additional information
st.write("""
### About the Data
- **Solar Panels**: Reduce emissions by generating clean electricity.
- **Wind Turbines**: Harness wind energy to produce electricity with minimal emissions.
- **Electric Vehicles**: Reduce emissions by replacing internal combustion engines.
- **Hydroelectric Power**: Utilize water energy to generate electricity.
- **Geothermal Energy**: Use heat from the Earth to produce clean energy.
""")
