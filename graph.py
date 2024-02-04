import networkx as nx
import matplotlib.pyplot as plt


subway = nx.Graph()
subway.add_edges_from(
    [   ("Heroiv Dnipra", "Minska", {"weight": 3}),
        ("Minska", "Obolon", {"weight": 3}),
        ("Obolon", "Pochaina", {"weight": 3}),
        ("Pochaina", "Ploshcha Tarasa Shevchenka", {"weight": 3}),
        ("Ploshcha Tarasa Shevchenka", "Kontraktova Ploshcha", {"weight": 3}),
        ("Kontraktova Ploshcha", "Poshtova Ploshcha", {"weight": 3}),
        ("Poshtova Ploshcha", "Maidan Nezalezhnosti", {"weight": 3}),
        ("Maidan Nezalezhnosti", "Ploshcha Ukrainskykh Heroiv", {"weight": 3}),
        ("Ploshcha Ukrainskykh Heroiv", "Olimpiyska", {"weight": 3}),
        ("Olimpiyska", "Palats Ukraina", {"weight": 3}),
        ("Palats Ukraina", "Lybidska", {"weight": 3}),
        ("Lybidska", "Demiivska", {"weight": 3}),
        ("Demiivska", "Holosiivska", {"weight": 3}),
        ("Holosiivska", "Vasylkivska", {"weight": 3}),
        ("Vasylkivska", "Vystavkovyi Tsentr", {"weight": 3}),
        ("Vystavkovyi Tsentr", "Ipodrom", {"weight": 3}),
        ("Ipodrom", "Teremky", {"weight": 3}),

        ("Lisova", "Chernihivska", {"weight": 3}),
        ("Chernihivska", "Darnytsia", {"weight": 3}),
        ("Darnytsia", "Livoberezhna", {"weight": 3}),
        ("Livoberezhna", "Hydropark", {"weight": 3}),
        ("Hydropark", "Dnipro", {"weight": 3}),
        ("Dnipro", "Arsenalna", {"weight": 3}),
        ("Arsenalna", "Khreshchatyk", {"weight": 4}),
        ("Khreshchatyk", "Teatralna", {"weight": 3}),
        ("Teatralna", "Universytet", {"weight": 3}),
        ("Universytet", "Vokzalna", {"weight": 3}),
        ("Vokzalna", "Politekhnichnyi Instytut", {"weight": 3}),
        ("Politekhnichnyi Instytut", "Shuliavska", {"weight": 3}),
        ("Shuliavska", "Beresteiska", {"weight": 3}),
        ("Beresteiska", "Nyvky", {"weight": 3}),
        ("Nyvky", "Sviatoshyn", {"weight": 3}),
        ("Sviatoshyn", "Zhytomyrska", {"weight": 3}),
        ("Zhytomyrska", "Akademmistechko", {"weight": 3}),

        ("Syrets", "Dorohozhychi", {"weight": 3}),
        ("Dorohozhychi", "Lukianivska", {"weight": 3}),
        ("Lukianivska", "Zoloti Vorota", {"weight": 4}),
        ("Zoloti Vorota", "Palats Sportu", {"weight": 3}),
        ("Palats Sportu", "Klovska", {"weight": 3}),
        ("Klovska", "Pecherska", {"weight": 3}),
        ("Pecherska", "Zvirynetska", {"weight": 3}),
        ("Zvirynetska", "Vydubychi", {"weight": 3}),
        ("Vydubychi", "Slavutych", {"weight": 4}),
        ("Slavutych", "Osokorky", {"weight": 3}),
        ("Osokorky", "Pozniaky", {"weight": 3}),
        ("Pozniaky", "Kharkivska", {"weight": 3}),
        ("Kharkivska", "Vyrlytsia", {"weight": 3}),
        ("Vyrlytsia", "Boryspilska", {"weight": 3}),
        ("Boryspilska", "Chervonyi Khutir", {"weight": 3}),

        ("Maidan Nezalezhnosti", "Khreshchatyk", {"weight": 5}),
        ("Teatralna", "Zoloti Vorota", {"weight": 5}),
        ("Palats Sportu", "Ploshcha Ukrainskykh Heroiv", {"weight": 5}),
    ]
)

def show_graph(graph, title="Graph"):
    pos = nx.circular_layout(graph)
    nx.draw(
        graph,
        pos,
        with_labels=True,
        font_size=7,
        node_size=300,
        node_color="skyblue",
        font_color="black",
        font_weight="bold",
        arrowsize=10,
    )
    plt.title(title)
    plt.show()

show_graph(subway, "Kyiv metro")

num_nodes = subway.number_of_nodes()
num_edges = subway.number_of_edges()

print(f"Nodes: {num_nodes}")
print(f"Edges: {num_edges}")

degree_dict = dict(subway.degree())
print("\nDegrees:")
for station, degree in degree_dict.items():
    print(f"{station}: {degree}")