import matplotlib.pyplot as plt
import numpy as np


age_groups = [
    "0–4", "5–9", "10–14", "15–19", "20–24", "25–29", "30–34",
    "35–39", "40–44", "45–49", "50–54", "55–59", "60–64", "65–69", "70–74", "75+"
]
male = np.array([4.3, 4.5, 4.7, 4.6, 4.8, 4.6, 4.3, 3.9, 3.3, 2.9, 2.5, 2.1, 1.8, 1.3, 0.9, 0.8])
female = np.array([4.0, 4.3, 4.5, 4.4, 4.6, 4.4, 4.1, 3.8, 3.2, 2.8, 2.5, 2.1, 1.9, 1.4, 1.0, 1.0])


y = np.arange(len(age_groups))
plt.figure(figsize=(10, 8))
plt.barh(y, -male, color='steelblue', label='Male')
plt.barh(y, female, color='lightcoral', label='Female')


plt.yticks(y, age_groups)
plt.xlabel("Population (%)")
plt.title("India Population Pyramid, 2025 (Estimated)")
plt.legend(loc='lower right')
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
