"""
Maps Route Planner -> main.py

Program to find the shortest path from point A to point B on a map network using A* search algorithm.
main.py:
    1. class Node- Object to store a node point on the map i.e. an intersection point.
    2. class A_star_planner- Object implementing A* search algorithm on the map network
    3. def shortest_path- Function called by Jupyter notebook
"""

from queue import PriorityQueue


# 1. Node
class Node:
    def __init__(self, node, map=None):
        self.node = node
        self.score = float('inf')
        self.neighbours = map.roads[node]
        self.pose = map.intersections[node]


class A_star_planner:

    def __init__(self, start, goal, M):
        self.start = Node(start, M)
        self.goal = Node(goal, M)
        self.Nodes = {self.start.node: self.start,
                      self.goal.node: self.goal}  # Dict for storing node and fast access through hashing
        self.M = M
        self.poses = M.intersections
        self.connections = M.roads
        self.frontier = PriorityQueue()  # Priority queue to access lowest f_score
        self.explored = set()
        self.cameFrom = [[None, float("inf")] for _ in range(len(self.connections))]
        # List of pairs containing parent node and g_score for a child (index is child)

    def shortest_path(self):
        """
        Function to be called for finding the shortest path
        :return: path (list)
        """
        print("Attempting to find shortest path from point A:{} to point B:{}".format(self.start.node, self.goal.node))

        current = self.Nodes[self.start.node]
        current.score = self.f_score(current)

        self.frontier.put((current.score, current.node))  # Adding start node to the frontier

        bestGoalReached = False

        while not self.frontier.empty():

            current_node = self.frontier.get()  # Picking the node with the lowest f-score
            current = self.Nodes[current_node[1]]  # Using index 1 since f_score is stored at index 0

            for neighbour in current.neighbours:  # Loop through all connecting nodes and add them to frontier

                if neighbour not in self.explored:
                    self.Nodes[neighbour] = Node(neighbour, self.M)
                    neighbour = self.Nodes[neighbour]
                    neighbour.score = self.f_score(neighbour, current)

                    self.frontier.put((neighbour.score, neighbour.node))

            # Break condition
            if current.node == self.goal.node:
                bestone = self.frontier.get()
                if bestone[0] >= current.score:
                    bestGoalReached = True
                    break
                self.frontier.put(bestone)

            self.explored.add(current.node)

        if bestGoalReached:
            print("Shortest path found!")
            path = self.retrace_path(self.goal.node)
        else:
            print("No path found!")
            path = None

        return path

    def f_score(self, node, parent=None):
        g = self.g_score(node, parent)  # Return g_score and update self.cameFrom
        h = self.heuristic(node)
        return h+g

    def heuristic(self, node):
        """
        Calculates the h_score for a particular node
        """
        dist = self.distance(node, self.goal)
        return dist

    def g_score(self, child, parent=None):
        """
        :param child, parent: Takes in any node on the network with its parent node and calculates g_score
        :return: the new g_score for that node
        """
        if parent:  # Condition to check if we're at the start node
            local_dist = self.distance(child, parent)
            parent_score = self.cameFrom[parent.node][1]  # Cumulative path cost until parent node
            new_score = local_dist + parent_score
            if new_score <= self.cameFrom[child.node][1]:  # Making sure we're not replacing a better path
                self.cameFrom[child.node] = [parent.node, new_score]
                return new_score
            else:
                return self.cameFrom[child.node][1] # There is already a better path so return that
        else:  # if we're at the start node then just set the score to zero
            new_score = 0
            self.cameFrom[child.node] = [None, new_score]
            return new_score

    @staticmethod
    def distance(node1, node2):
        x1, y1 = node1.pose
        x2, y2 = node2.pose

        dist = ( (x2-x1)**2 + (y2-y1)**2 )**0.5
        return dist

    def retrace_path(self, goal_node):
        """
        :param goal_node: Once goal has been reached successfully, retrace the path back to point A
        :return: path: List with the route
        """
        path = []
        current = goal_node
        path.append(current)
        previous = self.cameFrom[current][0]
        while previous is not None:
            path.append(previous)
            previous = self.cameFrom[previous][0]
        path.reverse()
        return path



def shortest_path(M,start,goal):
    route_search = A_star_planner(start, goal, M)
    return route_search.shortest_path()
