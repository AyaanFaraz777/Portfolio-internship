import matplotlib.pyplot as plt

states=["Kerala","Tamil Nadu","Karnataka","Maharashtra"]
population=[10,15,34,52]
plt.plot(states,population,color="red",marker="*",markeredgecolor="black",linestyle="dashed",linewidth=4,markersize=10)
plt.title("Population of different states")
plt.xlabel("States")
plt.ylabel("Population")
plt.show()
          
