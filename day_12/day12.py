from typing import Counter
# part 2 is inefficient, it takes about 2 mins

class Graph:
    def __init__(self, edges: list[(str, str)]) -> None:
        self.edges = edges
    def get_neighbours(self, edge_to_find: str):
        return [edge[1] for edge in self.edges if edge[0] == edge_to_find] \
        + [edge[0] for edge in self.edges if edge[1] == edge_to_find]

class Path:
    def __init__(self, graph, values:list[str] = None) -> None:
        self.values = values if values != None else []
        self.graph = graph
    def __contains_two(self) -> bool:
        return 2 in Counter([value for value in self.values if value.islower()]).values()
    def contains(self, node: str) -> bool:
        # return node in self.values and node.islower() # for part 1
        if node in ['start', 'end']:
            return node in self.values
        elif self.__contains_two():
            return node in self.values and node.islower()
        else:
            return False
    def add(self, node:str):
        self.values.append(node)
    def is_valid(self) -> bool:
        return self.values[-1] == 'end'
    def is_complete(self):
        return all(self.contains(neighbour) for neighbour in self.graph.get_neighbours(self.values[-1])) or self.is_valid()
    def get_end(self) -> str:
        return self.values[-1]
    def __add__(self, other: str):
        return Path(self.graph, self.values + [other])
    def __repr__(self) -> str:
        return str(self.values)
    def __str__(self) -> str:
        return str(self.values)

if __name__ == '__main__':
    graph = Graph([tuple(line[:-1].split('-')) for line in open('input.in')])
    paths: list[Path] = [Path(graph, ['start'])]
    complete_paths: list[Path] = []
    while len(paths) != 0:
        path = paths.pop(0)
        if path.is_complete():
            complete_paths.append(path)
            continue
        neighbours = graph.get_neighbours(path.get_end())
        for neighbour in neighbours:
            if not path.contains(neighbour):
                paths.append(path + neighbour)
    print(len([path for path in complete_paths if path.is_valid()]))
