# SHAPE (Python) – selected geometry and form utilities

This folder provides a lightweight Python port of key utilities from the SHAPE MATLAB toolbox for 3D particle geometry and form analysis. It focuses on portable, dependency-light functions with clear NumPy interfaces and runnable examples.

Acknowledgement: This work ports selected functions from the original SHAPE MATLAB code in this repository. The Python code mirrors naming and formulas (Wadell 1932, Krumbein 1941, Zingg 1935, Potticary et al. 2015, Kong and Fonseca 2018; orientation tensor by Bagi & Orosz 2020) where applicable.

## What’s included

- Geometry
	- `surface_area(nodes, faces)` – area of triangle surface mesh
	- `volume_centroid_inertia_tensor(nodes, elements, calculate_inertia=True)` – volume, centroid, inertia for tetra meshes
- Form and sphericity
	- `convexity(volume, volume_convex_hull)`
	- `sphericity_wadell(volume, surface_area)`
	- `sphericity_krumbein(S, I, L)`
	- `surface_orientation_tensor(nodes, faces)` → C, F, R, eigenvalues, eigenvectors
	- Form parameters and wrappers:
		- `form_parameters_kong_and_fonseca(S, I, L)`
		- `form_parameters_potticary_et_al(S, I, L)`
		- `form_parameters_zingg(S, I, L)`
		- `form_functions_1(surface_area, volume, volume_convex_hull)`
		- `form_functions_2(S, I, L)`
- I/O
	- `load_stl(path)` – load STL to `(nodes, faces)`

Source files
- `pyshape/geometry.py` – geometry
- `pyshape/form.py` – sphericities, form parameters, orientation tensor
- `pyshape/io.py` – STL loading (uses `trimesh` if installed, else built-in fallback)
- `pyshape/__init__.py` – package exports
- `python/examples/*` – runnable demos and a small STL asset for standalone runs
- `tests/*` – unit tests

## Requirements and install

- Python 3.9+
- NumPy, PyTest; `trimesh` is recommended for robust STL parsing (fallback exists)

From the repository root:

```bash
python -m pip install -r python/requirements.txt
```

## Quick start

Compute area, volume, inertia, and form metrics:

```python
import numpy as np
from pyshape import surface_area, surface_orientation_tensor

# Triangle mesh (square split into two triangles)
nodes = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0]], dtype=float)
faces = np.array([[0,1,2],[0,2,3]], dtype=int)
print(surface_area(nodes, faces))  # -> 1.0

from pyshape import volume_centroid_inertia_tensor
nodes_t = np.array([[0,0,0],[1,0,0],[0,1,0],[0,0,1]], dtype=float)
elements = np.array([[0,1,2,3]], dtype=int)
vol, cen, Icur, Idiag, axes = volume_centroid_inertia_tensor(nodes_t, elements)
print(vol, cen)

from pyshape import (
	convexity, sphericity_wadell, sphericity_krumbein, surface_orientation_tensor,
	form_functions_1, form_functions_2
)
print(convexity(2.0, 2.5))
print(sphericity_wadell(4/3*np.pi, 4*np.pi))
C, F, R, vals, vecs = surface_orientation_tensor(nodes, faces)
con, spW = form_functions_1(surface_area=1.0, volume=0.5, volume_convex_hull=0.6)
spK, flP, elP, flK, elK, SIZ, ILZ = form_functions_2(S=1.0, I=2.0, L=4.0)

from pyshape import load_stl
stl_nodes, stl_faces = load_stl("python/examples/assets/Tetrahedron_ascii.stl")
print(surface_area(stl_nodes, stl_faces))
```

Indexing notes
- `faces` are 0-based (M,3). If they appear to be 1-based (typical in MATLAB), auto-conversion will apply.
- `elements` are 0-based (M,4) for tetrahedral meshes; 1-based will be auto-converted.

## Examples

Ready-made demos (run from repository root):

```bash
python python/examples/stl_area_and_orientation.py
python python/examples/tetra_volume_inertia.py
python python/examples/form_metrics_demo.py
python python/examples/shapes_gallery.py
```

The examples use a bundled ASCII STL asset so the Python folder works standalone.

## Testing

Run the unit tests from the repository root:

```bash
python -m pytest -q python/tests
```

## Roadmap and parity with MATLAB

Ported from MATLAB SHAPE so far:
- Geometry: surface area for triangle meshes; volume/centroid/inertia for tetra meshes
- Form: Wadell and Krumbein sphericities; Zingg ratios; Potticary and Kong-Fonseca flatness/elongation; orientation tensor (Bagi & Orosz)
- Convenience wrappers matching MATLAB entry points (Form_functions_1/2)

Potential next steps:
- Volume from closed triangle surfaces (no tetra required)
- Convex hull volume helper to compute `Volume_CH` from point clouds/meshes
- Visualization helpers (Matplotlib) analogous to MATLAB plots

## License

This Python code lives within the same repository and follows its LICENSE.

## References

- Wadell, 1932; Krumbein, 1941; Zingg, 1935
- Potticary et al., 2015; Kong and Fonseca, 2018
- Bagi & Orosz, 2020 (surface orientation tensor)

## Examples

Run ready-made demos from `python/examples/` (they use bundled assets for standalone runs):

- `python/examples/stl_area_and_orientation.py` — load an STL, print surface area and (C,F,R)
- `python/examples/tetra_volume_inertia.py` — build a tetrahedral mesh and print volume, centroid, inertia
- `python/examples/form_metrics_demo.py` — sphericities, form parameters, and wrappers

Run them:

```bash
python python/examples/stl_area_and_orientation.py
python python/examples/tetra_volume_inertia.py
python python/examples/form_metrics_demo.py
```
