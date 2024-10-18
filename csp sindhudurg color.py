import networkx as nx
import matplotlib.pyplot as plt
import constraint
regions = ["dodamarg", "sawantwadi", "kudal", "vengurla", "kankavli", "vaibhavwadi", "malvan", "devgad"]
color = ["red", "orange", "green", "cyan", "blue", "yellow", "gray"]
problem = constraint.Problem()
for region in regions:
    problem.addVariable(region, color)
neighbours = {
    'dodamarg': ['sawantwadi'],
    'sawantwadi': ['kudal', 'vengurla'],
    'kudal': ['sawantwadi', 'vengurla', 'malvan', 'kankavli'],
    'vengurla': ['sawantwadi', 'kudal', 'malvan'],
    'malvan': ['vengurla', 'kudal', 'kankavli', 'devgad'],
    'kankavli': ['kudal', 'vengurla', 'malvan', 'devgad', 'vaibhavwadi'],
    'devgad': ['malvan', 'kankavli', 'vaibhavwadi'],
    'vaibhavwadi': ['kankavli']
}
for region, adjacent in neighbours.items():
    for neighbour in adjacent:
        problem.addConstraint(constraint.AllDifferentConstraint(), (region, neighbour))
solution = problem.getSolution()
print(solution)
G = nx.Graph()
G.add_nodes_from(regions)
for region, adjacent in neighbours.items():
    for neighbour in adjacent:
        G.add_edge(region, neighbour)
node_colors = [solution[region] for region in G.nodes()]
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=10, font_color='black', font_weight='bold', edge_color='gray', width=2)
plt.show()import constraint
import matplotlib.pyplot as plt
import networkx as nx

#Create a new problem instance
problem = constraint.Problem()

# Define the regions and their respective domains (colors)
regions = ['Kudal', 'Sawantwadi', 'Kankavli', 'Devgad', 'Malvan', 'Vengurla', 'Dodamarg','Vaibhavwadi']
colors = ['Red', 'Green', 'Blue','Pink','Black','Grey','Purple']
# Add variables to the problem
for region in regions:
    problem.addVariable(region, colors)
#Define the constraints
neighbors = {"Kudal":["Sawantwadi","Kankavli","Vengurla","Malvan"],
         "Sawantwadi":["Vengurla","Dodamarg","Kudal"],
         "Kankavli":["Malvan","Devgad","Kudal","Vaibhavwadi"],------
         "Devgad":["Kankavli","Malvan","Vaibhavwadi"],
         "Malvan":["Kankavli","Kudal","Devgad","Vengurla"],
         "Vengurla":["Sawantwadi","Kudal","Malvan"],
         "Dodamarg":["Sawantwadi"],
         "Vaibhavwadi":["Kankavli"] 
    }

for region, adjacent in neighbors.items():
    for neighbor in adjacent:
        problem.addConstraint(lambda region, neighbor: region != neighbor,(region,neighbor))
solution=problem.getSolution()
print(solution)

grp=nx.Graph(neighbors)
nx.draw(grp,with_labels=True,node_color="white",font_color="black")
plt.show()