from pathlib import Path
from matplotlib import pyplot as plt
import sys

from cgshop2025_pyutils import(
    InstanceDatabase,
    visualization,
    ZipSolutionIterator
)

# Get 1st argument from command line
if len(sys.argv) == 2:
    uid =sys.argv[1]
else:
    print("Error: Wrong size of parameters received, ensure you are sending just one parameter")
    exit()

# Get instances, necesary to obtain x,y points 
idb = InstanceDatabase("example_instances/")

# Create axe to graph instance points and solution edges
axs = plt.axes()

#  Find instance with uid
instance_selected = 0
uid_found = False
for instance in idb:
    if(instance.instance_uid == uid):
        uid_found = True
        points_x = instance.points_x
        points_y = instance.points_y
        # Plot instance points
        visualization.plot_instance(axs,instance) 
        break

if uid_found == False : 
    print("uid not found")
    exit()

# Find solution with iud
uid_found = False
sol_edges = []
for solution in ZipSolutionIterator("example_solutions.zip"):
    if(solution.instance_uid == uid):
        uid_found = True
        sol_edges =solution.edges

if uid_found == False : 
    print("uid not found")
    exit()

# Plot solution edges
for edge in sol_edges:
    axs.plot([points_x[edge[0]],points_x[edge[1]]],[points_y[edge[0]],points_y[edge[1]]])

# Show plot
plt.show()

