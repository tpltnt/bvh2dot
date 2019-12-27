# bvh2dot
visualize BVH file skeletons using graphviz

generate dot/graphviz file: `./bvh_skeleton_viz.py [-h] [--outfile OUTFILE] bvhfile`
generate graph image: `dot -Tpng -o skeleton_tree.png skeleton_tree.gv`

# references
* [Biovision BVH file format explanation](https://research.cs.wisc.edu/graphics/Courses/cs-838-1999/Jeff/BVH.html)
* [wikipedia: BVH file](https://en.wikipedia.org/wiki/Biovision_Hierarchy)
* [graphviz](http://graphviz.org/) - open source graph visualization software
