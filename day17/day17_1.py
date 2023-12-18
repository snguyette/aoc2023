from aocd import get_data
import numpy as np
import queue
import time

class SetQueue(queue.Queue):

    def _init(self, maxsize):
        self.maxsize = maxsize
        self.queue = set()

    def _put(self, item):
        self.queue.add(item)

    def _get(self):
        return self.queue.pop()


class Graph():
    def __init__(self):
        self.nodes = {}
        self.edges = {}
    
    def add_node(self, new_node):
        # if new_node not in self.nodes:
        self.nodes[new_node] = set()

    def add_edge(self, start_node, end_node, weight):
        self.nodes[start_node].add(end_node)
        (x1, y1, d1, s1) = start_node
        (x2, y2, d2, s2) = end_node
        self.edges[((x1, y1), (x2, y2))] = weight

def print_all_dest_nodes(dist, g, grid):
    for k in g.nodes:
        (x, y, d, s) = k
        if x == grid.shape[0]-1 and y == grid.shape[1]-1:
            print(f'{k}: {dist[k]}')

def main():
    my_data = get_data(day=17, year=2023)
    # print(my_data)
    # my_data = "2413432311323\n3215453535623\n3255245654254\n3446585845452\n4546657867536\n1438598798454\n4457876987766\n3637877979653\n4654967986887\n4564679986453\n1224686865563\n2546548887735\n4322674655533"
    lines = my_data.split("\n")
    grid = np.array([list(line) for line in lines]).astype(np.int32)
    node_queue = SetQueue()
    my_graph = Graph()
    x = 0
    y = 0
    direction = 'i'
    steps = 0
    node_queue.put((x, y, 'i', 0))
    processed = []
    while not node_queue.empty():
        # print(node_queue.qsize())
        # print(node_queue.queue)
        # input()
        node = node_queue.get()
        (x, y, direction, steps) = node
        if node not in my_graph.nodes:
            my_graph.add_node(node)
        if direction == 'i':
            new_node = (x+1, y, 'd', 1)
            # if new_node not in my_graph.nodes:
            node_queue.put(new_node)
            my_graph.add_edge(node, new_node, grid[x+1, y])
            new_node = (x, y+1, 'r', 1)
            # if new_node not in my_graph.nodes:
            node_queue.put(new_node)
            my_graph.add_edge(node, new_node, grid[x, y+1])
        else:
            if direction == 'u':
                if steps < 3 and x > 0:
                    new_node = (x-1, y, 'u', steps+1)
                    # if new_node not in processed:
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x-1, y)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x-1, y])
                if y > 0:
                    new_node = (x, y-1, 'l', 1)
                    # if new_node not in processed:
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x, y-1)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x, y-1])
                if y < grid.shape[1]-1:
                    new_node = (x, y+1, 'r', 1)
                    # if new_node not in processed:
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x, y+1)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x, y+1])
            if direction == 'd':
                if steps < 3 and x < grid.shape[0]-1:
                    new_node = (x+1, y, 'd', steps+1)
                    # if new_node not in processed:
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x+1, y)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x+1, y])
                if y > 0:
                    new_node = (x, y-1, 'l', 1)
                    # if new_node not in processed:
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x, y-1)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x, y-1])
                if y < grid.shape[1]-1:
                    new_node = (x, y+1, 'r', 1)
                # if new_node not in processed:
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x, y+1)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x, y+1])
            if direction == 'r':
                if steps < 3 and y < grid.shape[1]-1:
                    new_node = (x, y+1, 'r', steps+1)
                    # if new_node not in processed:
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x, y+1)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x, y+1])
                if x > 0:
                    new_node = (x-1, y, 'u', 1)
                    # if new_node not in processed:
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x-1, y)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x-1, y])
                if x < grid.shape[0]-1:
                    new_node = (x+1, y, 'd', 1)
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x+1, y)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x+1, y])
            if direction == 'l':
                if steps < 3 and y > 0:
                    new_node = (x, y-1, 'l', steps+1)
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x, y-1)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x, y-1])
                if x > 0:
                    new_node = (x-1, y, 'u', 1)
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x-1, y)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x-1, y])
                if x < grid.shape[0]-1:
                    new_node = (x+1, y, 'd', 1)
                    if new_node not in my_graph.nodes:
                        node_queue.put(new_node)
                    # if ((x, y), (x+1, y)) not in my_graph.edges:
                    my_graph.add_edge(node, new_node, grid[x+1, y])
    print('It finished!')
    visited = {}
    unvisited_list = []
    unvisited_dist = []
    t_dist = {}
    print('Initializing structures...')
    for k in my_graph.nodes:
        visited[k] = False
        unvisited_list.append(k)
        t_dist[k] = float('inf')
    unvisited_dist = []
    print(len(unvisited_list))
    t_dist[(0, 0, 'i', 0)] = 0
    curr = (0, 0, 'i', 0)
    print('starting loop...')
    count = 0
    time_now = time.time()
    while curr:
        if count % 100 == 0:
            print(f'{len(unvisited_list)}: {time.time() - time_now}')
            time_now = time.time()
        count += 1
        for node in my_graph.nodes[curr]:
            if not visited[node]:
                cost = t_dist[curr] + my_graph.edges[((curr[0], curr[1]), (node[0], node[1]))]
                if cost < t_dist[node]:
                    if t_dist[node] < float('inf'):
                        unvisited_dist.remove((node, t_dist[node]))
                    t_dist[node] = cost
                    unvisited_dist.append((node, cost))
        unvisited_dist.sort(key=lambda x: x[1])
        unvisited_list.remove(curr)
        visited[curr] = True
        if unvisited_dist and unvisited_dist[0][1] < float('inf'):
            curr = unvisited_dist[0][0]
            unvisited_dist.pop(0)
        else:
            break
    print_all_dest_nodes(t_dist, my_graph, grid)


if __name__ == "__main__":
    main()
