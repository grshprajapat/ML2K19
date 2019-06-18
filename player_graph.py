#!/usr/bin/python3
import matplotlib.pyplot  as plt
player=["virat","dhoni","pandaya"]
runs=[120,55,60]
plt.xlabel("players")
plt.ylabel("runs")
plt.bar(player,runs)
plt.grid(color="green")
plt.legend()
plt.show()
