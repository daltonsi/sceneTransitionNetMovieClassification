import ast
import networkx as nx
import matplotlib.pyplot as plt
import json

#SLUG LINE FILES
STAR_WARS = "output/star_wars_results.txt"
AUSTIN_POWERS = "output/austinpowers_results.txt"
BATMAN = "output/batman_results.txt"
BLADE_RUNNER = "output/blade_runner_results.txt"
EMPIRE_STRIKES_BACK = "output/empire_strikes_back_results.txt"
JERRY_MCQUIRE = "output/jerry_maguire_results.txt"
BEST_FRIENDS_WEDDING = "output/mybestfriendswedding_results.txt"
TITANIC = "output/titanic_results.txt"
FILE_LIST = [STAR_WARS, AUSTIN_POWERS, BATMAN, BLADE_RUNNER, EMPIRE_STRIKES_BACK, JERRY_MCQUIRE, BEST_FRIENDS_WEDDING, TITANIC]

# CONVERTS each SLUG LINE from processed screenplay to yield a scene node object represented as:
# [SCENE_NUMBER(int), SCENE_LOCATION(str), SCENE_CHARACTERS(list)]
# EXAMPLE:
#   SLUG LINE -
#       1:	INT. REBEL BLOCKADE RUNNER - MAIN PASSAGEWAY:	['THREEPIO', 'THREEPIO', 'THREEPIO', 'THREEPIO']
#   CONVERTED SCENE OBJECT -
#       [1, 'INT. REBEL BLOCKADE RUNNER - MAIN PASSAGEWAY', ['THREEPIO', 'THREEPIO', 'THREEPIO', 'THREEPIO']]
def sluglines_to_networkObjects(textfile):
    file_object = open(textfile,'r')
    scene_objects = []
    for line in file_object.readlines():
        line = line.replace(":","")
        line = line.split('\t')
        line[2] = ast.literal_eval(line[2])
        line[0] = int(line[0])
        if ' -- ' in line[1]:
            line[1] = line[1].split(' -- ')[0]
        if ' - ' in line[1]:
            line[1] = line[1].split(' - ')[0]
        if "." in line[1]:
            try:
                line[1] = line[1].split(". ")[1]
            except:
                pass
        scene_objects.append(line)
    return scene_objects

# Reformats network objects into a list of key value pairs for network preprocessing
# KEY: scene location pair
# VALUE: [Scene_numbers(list), characters(lists)]
def networkObjects_to_edges(networkObjects_list):
    node_pairs = []
    for first, second in zip(networkObjects_list, networkObjects_list[1:]):
        key = [first[1],second[1]]
        scene_numbers = [first[0],second[0]]
        characters = [first[2],second[2]]
        node_object = [key,[scene_numbers,characters]]
        node_pairs.append(node_object)
    return node_pairs
    
# Function to calculate graph parameters
# Results can be found in "graph_info" directory.
def graph_info(g):
    result = {}
    components = list(nx.connected_component_subgraphs(g))
    degrees = nx.degree(g)
    highest_degree_node = sorted(degrees, key = lambda x: degrees[x], reverse = True)[0]
    result['highest degree node'] = highest_degree_node
    result['numnber of components'] = len(components)
    result['number of nodes'] = g.number_of_nodes()
    result['number of edges'] = g.number_of_edges()

    result['degree centrality'] = sorted([(el,nx.degree_centrality(g)[el]) for el in nx.degree_centrality(g)], key = lambda x: x[1], reverse = True)
    result['highest degree node degree centrality'] = nx.degree_centrality(g)[highest_degree_node]

    result['closeness_centrality'] = sorted([(el,nx.closeness_centrality(g)[el]) for el in nx.closeness_centrality(g)], key = lambda x: x[1], reverse = True)
    result['highest degree node closeness'] = nx.closeness_centrality(g)[highest_degree_node]

    result['betweenness centrality'] = sorted([(el,nx.betweenness_centrality(g)[el]) for el in nx.betweenness_centrality(g)], key = lambda x: x[1], reverse = True)
    result['highest degree node betweenness'] = nx.betweenness_centrality(g)[highest_degree_node]

    largest_component = sorted (components, key = lambda x: x.number_of_nodes(), reverse = True)[0]
    result['largest component percent'] = largest_component.number_of_nodes()/float(g.number_of_nodes())
    result['largest component diameter'] = nx.diameter(largest_component)
    result['largest component average path length'] = nx.average_shortest_path_length(largest_component)
    result['average_degree'] = sum(degrees.values())/float(g.number_of_nodes())
    result['avg_cluster_coefficient'] = nx.average_clustering(g)
    return result

def create_network_viz(edge_list, file_name):
    g = nx.Graph()
    for edge in edge_list:
        g.add_edge(edge[0][0],edge[0][1])
    result = graph_info(g)
    f = open('graph_info/'+file_name+'.tsv','w')
    for el in result:
        f.write(el + ':\t' + json.dumps(result[el]) + '\n')
    pos1=nx.spring_layout(g)
    nx.draw_spring(g, with_labels=True, node_size=1, font_size=6, font_color='blue')
    plt.savefig(str(file_name) + "_netviz.png")
    plt.clf()
    f.close()
    return 0


if __name__ == "__main__":
    for FILE in FILE_LIST:
        filename = FILE.split('/')[1].split('.')[0]
        networkObjects_list = sluglines_to_networkObjects(FILE)
        node_pairs = networkObjects_to_edges(networkObjects_list)
        create_network_viz(node_pairs, filename)
