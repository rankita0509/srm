import networkx as nx
import matplotlib.pyplot as plt
graph={'dodamarg':['sawantwadi'],
       'sawantwadi':['kudal','vengurla'],
       'kudal':['sawantwadi','vengurla','malvan','kankavli'],
       'vengurla':['sawantwadi','kudal','malvan'],
       'malvan':['vengurla','kudal','kankavli','devgad'],\
       'kankavli':['kudal','vengurla','malvan','devgad','vaibhavwadi'],
       'devgad':['malvan','kankavli'],
       'vaibhavwadi':['kankavli']}
g = nx.Graph(graph)
pos = nx.spring_layout(g)  
nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=500, 
        font_size=10, font_color='darkblue', edge_color='gray')# Add title
plt.title('Graph Visualization Using NetworkX')
plt.show()
visited = []
queue = []
def bfs(node, visited, graph):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end=' ')
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
print("\nBFS traversal starting from node 'a':")
bfs('dodamarg', visited, graph)

