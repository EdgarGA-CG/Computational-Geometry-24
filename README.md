# Computational-Geometry-24
An interactive space to implemente computational geometry concepts. 

# Dependencies
Before use the utilites of this repo, ensure resolve next dependencies (make sure that you have the latest python version, 3.13):

```bash
#Install python libraries

pip install cgshop2025_pyutils
pip install ipywidgets
```


# How to use python scripts

Execute next scripts in proposed order.

1. `solve_instances.py`: When file it is executed it will resolve the instances located in example_instances folder

```bash
python solve_instances.py
```
2. `graph_solution.py`: This file needs an input parameter to generate a graph with the points of the instance and the solution edges previosly calculated by solve_instances.py

```bash
python graph_solution.py <uid>

#Example:
python graph_solution.py cgshop2025_examples_ortho_10_ff68423e
```
