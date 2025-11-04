import matplotlib.pyplot as plt
import pandas as pd

# Sample demographic data for Japan (2025 estimate, approximate values)
age_groups = [
    "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39",
    "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80+"
]
male_population = [
    -2.4, -2.3, -2.2, -2.1, -2.3, -2.4, -2.5, -2.6,
    -3.0, -3.2, -3.0, -2.8, -2.5, -2.4, -2.0, -1.8, -1.5
]
female_population = [
    2.3, 2.2, 2.1, 2.0, 2.2, 2.3, 2.5, 2.6,
    3.0, 3.3, 3.1, 3.0, 2.8, 2.9, 2.7, 2.5, 2.3
]

df = pd.DataFrame({
    "Age Group": age_groups,
    "Male": male_population,
    "Female": female_population
})

# Create population pyramid
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(df["Age Group"], df["Male"], color="steelblue", label="Male")
ax.barh(df["Age Group"], df["Female"], color="lightcoral", label="Female")

ax.set_xlabel("Population (%)")
ax.set_ylabel("Age Group")
ax.set_title("Japan Population Pyramid (2025 Estimate)")
ax.legend(loc="upper right")
ax.set_xlim(-4, 4)
ax.grid(axis="x", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()

