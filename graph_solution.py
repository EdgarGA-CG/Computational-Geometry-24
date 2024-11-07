from pathlib import Path
from matplotlib import pyplot as plt
import sys

from cgshop2025_pyutils import(
    InstanceDatabase,
    visualization,
    ZipSolutionIterator
)

if len(sys.argv) == 2:
    uid =sys.argv[1]
else:
    print("Error: Parameters are incorrect")

idb = InstanceDatabase("example_instances/")

axs = plt.axes()

instance_selected = 0
for instance in idb:
    if(instance.instance_uid == uid):
        points_x = instance.points_x
        points_y = instance.points_y
        visualization.plot_instance(axs,instance)

sol_edges = []
# Verify the solutions
for solution in ZipSolutionIterator("example_solutions.zip"):
    if(solution.instance_uid == uid):
        sol_edges =solution.edges 

for edge in sol_edges:
    axs.plot([points_x[edge[0]],points_x[edge[1]]],[points_y[edge[0]],points_y[edge[1]]])

plt.show()

