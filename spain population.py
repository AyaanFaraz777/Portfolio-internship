import matplotlib.pyplot as plt
import numpy as np

age_groups = [
    "0–4", "5–9", "10–14", "15–19", "20–24", "25–29", "30–34",
    "35–39", "40–44", "45–49", "50–54", "55–59", "60–64", "65–69", "70–74", "75+"
]
male = np.array([1.83, 2.20, 2.52, 2.71, 2.63, 2.59, 2.82, 3.05, 3.62, 4.19, 4.01, 3.77, 3.33, 2.74,2.19, 1.83])
female = np.array([1.73, 2.08, 2.37, 2.56, 2.47, 2.49, 2.75, 3.04, 3.57,4.07, 3.94, 3.84, 3.53, 3.01, 2.53, 2.30])

y= np.arange(len(age_groups))
plt.figure(figsize=(10,8))
plt.barh(y,-male,color="steelblue",label="Male")
plt.barh(y,female,color="pink",label="Female")
plt.yticks(y,age_groups)
plt.xlabel("Population(%)")
plt.title("Population primid")
plt.legend(loc="lower right")
plt.axvline(0,color="blue",linewidth=0.5)
plt.grid(axis='x',linestyle="--",alpha=0.5)
plt.tight_layout()
plt.show()
