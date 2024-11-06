from pathlib import Path
from matplotlib import pyplot as plt
import os

from cgshop2025_pyutils import (
    DelaunayBasedSolver,
    InstanceDatabase,
    ZipSolutionIterator,
    ZipWriter,
    verify,
    visualization
)

# Locate the instances
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
idb = InstanceDatabase(file_path)

# If the solution zip file already exists, delete it
if Path("example_solutions.zip").exists():
    Path("example_solutions.zip").unlink()

fig, axs = plt.subplots(2)
# Compute solutions for all instances using the provided (naive) solver
solutions = []
for instance in idb:
    uid = instance.instance_uid
    points_x = instance.points_x
    points_y = instance.points_y
    num_points = instance.num_points
    print(uid)
    print(points_x)
    print(points_y)
    print(num_points)
    solver = DelaunayBasedSolver(instance) # Call class/function to get the solution
    solution = solver.solve()
    solutions.append(solution)
    visualization.plot_instance(axs[0],instance)

sol_edges = solutions[0].edges # Index zero to get solution for 
for edge in sol_edges:
    axs[0].plot([points_x[edge[0]],points_x[edge[1]]],[points_y[edge[0]],points_y[edge[1]]])



plt.show()

# Write the solutions to a new zip file
with ZipWriter("example_solutions.zip") as zw:
    for solution in solutions:
        zw.add_solution(solution)

# Verify the solutions
for solution in ZipSolutionIterator("example_solutions.zip"):
    instance = idb[solution.instance_uid]
    result = verify(instance, solution)
    print(f"{solution.instance_uid}: {result}")
    assert not result.errors, "Expect no errors."

