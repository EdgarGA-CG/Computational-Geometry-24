from pathlib import Path
from matplotlib import pyplot as plt
#import sys, os

#mod_path = os.path.join(os.path.dirname(__file__),"pyutils25","Library","Frameworks","Python.framework","Versions","3.12","lib","python3.12","site-packages")
#sys.path.insert(0,mod_path)

from cgshop2025_pyutils import(
    DelaunayBasedSolver,
    InstanceDatabase,
    ZipSolutionIterator,
    ZipWriter,
    verify,
)

# Locate the instances
idb = InstanceDatabase("example_instances/")

# If the solution zip file already exists, delete it
if Path("example_solutions.zip").exists():
    Path("example_solutions.zip").unlink()

fig, axs = plt.subplots(2)
# Compute solutions for all instances using the provided (naive) solver
solutions = []
for instance in idb:
    solver = DelaunayBasedSolver(instance) # Call class/function to get the solution
    solution = solver.solve()
    solutions.append(solution)
    #visualization.plot_instance(axs[0],instance)

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

