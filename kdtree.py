# Balanced + Unbalanced KD Tree
# def build_kdtree(points, depth=0):
#     if not points:
#         return None
#     k = len(points[0])
#     axis = depth % k
#     sorted_points = sorted(points, key=lambda point: point[axis])
#     midpoint = len(points) // 2
#     return {
#         'point': sorted_points[midpoint],
#         'left': build_kdtree(sorted_points[:midpoint], depth+1),
#         'right': build_kdtree(sorted_points[midpoint+1:], depth+1)
#     }


def build_kdtree_unbalanced(points, depth=0):
    if not points:
        return None
    k = len(points[0])
    axis = depth % k
    return {
        'point': points[0],
        'left': build_kdtree_unbalanced([p for p in points[1:] if p[axis] <= points[0][axis]], depth+1),
        'right': build_kdtree_unbalanced([p for p in points[1:] if p[axis] > points[0][axis]], depth+1)
    }




# def print_kdtree(node, depth=0, ch='A'):
#     if node is None:
#         return
#     print("  " * depth, ch, ':', node['point'])
#     print_kdtree(node['left'], depth+1, ch + 'L')
#     print_kdtree(node['right'], depth+1, ch + 'R')


# # points = [[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 3], [1, 5], [9, 5]]
# points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
# # points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]

# print("Balanced KD Tree")
# kdtree = build_kdtree(points)
# print_kdtree(kdtree)

# print("\nUnbalanced KD Tree")
# kdtree = build_kdtree_unbalanced(points)
# print_kdtree(kdtree)

def build_balanced_kdtree(points, depth=0):
    if not points:
        return None
    k = len(points[0])
    axis = depth % k
    sorted_points = sorted(points, key=lambda point: point[axis])
    median = len(points) // 2
    return{
        'point' : sorted_points[median],
        'left' : build_balanced_kdtree(sorted_points[:median],depth+1),
        'right' : build_balanced_kdtree(sorted_points[median+1:],depth+1)
    }

def build_unbalanced_kdtree(points,depth=0):
    if not points:
        return None
    k = len(points[0])
    axis = depth % k
    return{
        'point' : points[0],
        'left' : build_unbalanced_kdtree([p for p in points[1:] if p[axis] <= points[0][axis]], depth+1),
        'right' : build_unbalanced_kdtree([p for p in points[1:] if p[axis] > points[0][axis]], depth+1)
    }


def print_kdtree(node,depth=0,ch='A'):
    if node is None:
        return
    print("  "*depth,ch,':',node['point'])
    print_kdtree(node['left'],depth+1,ch+'L')
    print_kdtree(node['right'],depth+1,ch+'R')






points = [[2,4],[1,5],[2,9],[8,2],[7,3]]
print("Balanced KD tree:-")
kdtree = build_balanced_kdtree(points)
print_kdtree(kdtree)

print("Unbalanced KD tree:-")
kdtree = build_unbalanced_kdtree(points)
print_kdtree(kdtree)