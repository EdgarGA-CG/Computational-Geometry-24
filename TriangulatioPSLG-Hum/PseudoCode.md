# Nonobtuse Triangulation of PSLGs

## Pseudocode for Nonobtuse Triangulation of a PSLG

**Input:** A PSLG $\Gamma$ with $n$ vertices.  
**Output:** A nonobtuse triangulation of $\Gamma$.

---

1. Initialize vertex set $V$ from the vertices of $\Gamma$.  
2. Initialize empty set $T$ for storing triangles.  
3. Initialize empty list $R$ for Steiner points.  

### Step 1: Initial Triangulation
4. Apply a standard triangulation algorithm to create an initial set of triangles $T$.

### Step 2: Ensure Gabriel Property
5. For each triangle $t \in T$:  
   5.1. If an edge is not a Gabriel edge:  
   - Compute the incenter of $t$.  
   - Adjust vertices and edges to satisfy the Gabriel condition.  
   - Temporarily store new Steiner points in $R$.

### Step 3: Update Triangulation
6. For each triangle $t \in T$:  
   - Refine $T$ by adding Steiner points from $R$.  
   - Recalculate affected regions to ensure nonobtuse angles.

### Step 4: Final Refinement
7. For each remaining region in $T$:  
   - Apply local triangulation rules for three- and four-sided regions.  
   - Ensure all triangles have nonobtuse angles.

---

**Output:** Return the set of triangles $T$.

## Remarks

- To triangulate and make a triangle Gabriel, use the perpendicular bisector to add at least one poi
