def find_all_paths(graph, start, end, path=[]):
		path = path + [start]
		if start == end:
			return [path]
		if start not in graph:
			return []
		paths = []
		for node in graph[start]:
			if node not in path:
				newpaths = find_all_paths(graph, node, end, path)
				for newpath in newpaths:
					paths.append(newpath)
		return paths       

def min_path(graph, start, end):
	paths=find_all_paths(graph,start,end)
	
	route_distance = dict()

	for route in paths:
		print(route)

graph = [
    {
      "source": "A", "target": "B", "distance":6
    },
    {
      "source": "A", "target": "E", "distance":4
    },
    {
      "source": "B", "target": "A", "distance":6
    },
    {
      "source": "B", "target": "C", "distance":2
    },
    {
      "source": "B", "target": "D", "distance":4
    },
    {
      "source": "C", "target": "B", "distance":3
    },
    {
      "source": "C", "target": "D", "distance":1
    },
    {
      "source": "C", "target": "E", "distance":7
    },
    {
      "source": "D", "target": "B", "distance":8
    },
    {
      "source": "E",  "target": "B", "distance":5
    },
    {
      "source": "E", "target": "D", "distance":7
    }
  ]

graph3 = dict()

for item in graph:
	graph_source_dict = {}
	for item2 in graph:
		if item['source'] == item2['source']:
			graph_source_dict[item2['target']] = item2['distance']

	graph3[item['source']] = graph_source_dict

print(min_path(graph3, 'A', 'C'))