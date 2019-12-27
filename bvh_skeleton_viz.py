#!/usr/bin/env python3
"""
generate tree of bones in BVH files
"""
skeletons = []
with open("Example1.bvh") as infile:
    skeleton = None
    parents = ['none']  # track the (path of) parents)
    level = 0
    for line in infile:
        if '{' in line:
            level += 1
            parents.append('none')  # make sure we have a value
        if '}' in line:
            level -= 1
        if "ROOT" in line:
            # check if there was already a skeletin defined
            if skeleton:
                skeletons.append(skeleton)
            # create new skeleton dict and root node
            skeleton = dict()
            name = line.strip()[4:].strip()
            skeleton[str(level)] = {'name': name,
                                    'parent': "none"}
            parents[0] = name
        if "JOINT" in line:
            # get data of joint
            name = line.strip()[5:].strip()
            if str(level) not in skeleton.keys():
                skeleton[str(level)] = []
            skeleton[str(level)].append(
                {'name': name,
                 'parent': parents[level-1]}
                )
            parents[level] = name
    skeletons.append(skeleton)  # save last processed skeleton

scounter = 1
for skeleton in skeletons:
    fname = "skeleton_tree_{}.gv".format(scounter)
    with open(fname, 'w') as outfile:
        outfile.write("# BVH skelleton visualisation\n")
        outfile.write("# render via: dot -Tpng -o skeleton_tree.png skeleton_tree.gv\n")
        outfile.write("digraph skeleton {\n")
        for level in skeleton:
            for k in skeleton[level]:
                if k in ['name', 'parent']:
                    continue
                edge = "{0} -> {1};".format(k['parent'], k['name'])
                outfile.write("\t" + edge + "\n")
        outfile.write("}")
    scounter += 1
