# Computational Geometry

## Software

- [Computational Geometry Algorithm Library (CGAL)](https://github.com/CGAL/cgal)
- [Open CASCADE Technology (OCCT)](https://github.com/Open-Cascade-SAS/OCCT)
  - [PythonOCC](https://github.com/tpaviot/pythonocc-core)
- [ezdxf](https://github.com/mozman/ezdxf)
- [Open3D](https://github.com/isl-org/Open3D)
- (Not maintained) [PyMesh](https://github.com/PyMesh/PyMesh)
- [OpenVDB](https://github.com/AcademySoftwareFoundation/openvdb)

## CGAL Notes

- Tetrahedral mesh representations: https://doc.cgal.org/latest/Triangulation_3/index.html#title0
- https://doc.cgal.org/latest/TDS_3/index.html#chapterTDS3
- Infinite vertices are conceptually representative of all space not specified by finite interior cells. For each face on the user defined boundary, there is an exterior cell that has one corner as the infinite vertex. This means that all space is actually tessellated. There are no faces with a cell on only 1 side.
- Polyhedrons are surfaces, not volumes.

### Incremental construction and data access of a tetrahedral mesh

https://doc.cgal.org/latest/TDS_3/index.html#title6
https://doc.cgal.org/latest/SMDS_3/index.html#TetSoupExample
https://github.com/CGAL/cgal/blob/25d28c0e2f3acff6f029df7f13fd9e4032cf33a7/SMDS_3/include/CGAL/tetrahedron_soup_to_triangulation_3.h#L176

