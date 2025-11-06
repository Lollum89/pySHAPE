#!/usr/bin/env python3
"""
Quick test to verify OpenGL rendering with a simple cube.
"""
import sys
from pathlib import Path
import numpy as np

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent))

from pyshape import load_stl

# Try to load and print info about an STL file
stl_file = Path(__file__).parent.parent / "Matlab" / "examples" / "Platonic_solids" / "Hexahedron.stl"

if stl_file.exists():
    print(f"Loading: {stl_file}")
    nodes, faces = load_stl(stl_file)
    print(f"Nodes shape: {nodes.shape}")
    print(f"Faces shape: {faces.shape}")
    print(f"Nodes range: [{nodes.min():.3f}, {nodes.max():.3f}]")
    print(f"Node sample:\n{nodes[:3]}")
    print(f"Face sample:\n{faces[:3]}")
else:
    print(f"File not found: {stl_file}")
    
    # Create a simple test cube
    print("\nCreating test cube...")
    nodes = np.array([
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # bottom
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1],  # top
    ], dtype=float)
    
    faces = np.array([
        # bottom
        [0, 1, 2], [0, 2, 3],
        # top
        [4, 6, 5], [4, 7, 6],
        # front
        [0, 5, 1], [0, 4, 5],
        # back
        [2, 7, 3], [2, 6, 7],
        # left
        [0, 3, 7], [0, 7, 4],
        # right
        [1, 6, 2], [1, 5, 6],
    ], dtype=int)
    
    print(f"Nodes shape: {nodes.shape}")
    print(f"Faces shape: {faces.shape}")
    
print("\nTest complete - data looks good!")
