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
    components = list(nx.strongly_connected_component_subgraphs(g))
    in_degrees = g.in_degree()
    out_degrees = g.out_degree()
    highest_in_degree_node = sorted(in_degrees, key = lambda x: in_degrees[x], reverse = True)[0]
    highest_out_degree_node = sorted(out_degrees, key = lambda x: out_degrees[x], reverse = True)[0]

    result['highest in_degree node'] = highest_in_degree_node
    result['highest out_degree_node'] = highest_out_degree_node

    result['numnber of components'] = len(components)
    result['number of nodes'] = g.number_of_nodes()
    result['number of edges'] = g.number_of_edges()
#Degree centrality
    in_degree_centrality = nx.in_degree_centrality(g)
    out_degree_centrality = nx.out_degree_centrality(g)
    result['sorted in_degree centrality'] = sorted([(el,in_degree_centrality[el]) for el in g.nodes()], key = lambda x: x[1], reverse = True)
    result['sorted out_degree centrality'] = sorted([(el,out_degree_centrality[el]) for el in g.nodes()], key = lambda x: x[1], reverse = True)
    
    result['closeness_centrality'] = sorted([(el,nx.closeness_centrality(g)[el]) for el in nx.closeness_centrality(g)], key = lambda x: x[1], reverse = True)
    result['highest in_degree node closeness'] = nx.closeness_centrality(g)[highest_in_degree_node]
    result['highest out_degree node closeness'] = nx.closeness_centrality(g)[highest_out_degree_node]


    result['betweenness centrality'] = sorted([(el,nx.betweenness_centrality(g)[el]) for el in nx.betweenness_centrality(g)], key = lambda x: x[1], reverse = True)
    result['highest in_degree node betweenness'] = nx.betweenness_centrality(g)[highest_in_degree_node]
    result['highest in_degree node betweenness'] = nx.betweenness_centrality(g)[highest_out_degree_node]


    largest_component = sorted (components, key = lambda x: x.number_of_nodes(), reverse = True)[0]

    result['largest strongly component percent'] = largest_component.number_of_nodes()/float(g.number_of_nodes())
    result['largest strongly component diameter'] = nx.diameter(largest_component)
    result['largest strongly component average path length'] = nx.average_shortest_path_length(largest_component)
    result['average_degree (undireceted)'] = sum(g.degree().values())/float(g.number_of_nodes())
    result['avg_cluster_coefficient (transitivity)'] = nx.transitivity(g)
    return result

def create_network_viz(edge_list, file_name):
    g = nx.DiGraph()
    for edge in edge_list:
        g.add_edges_from([(edge[0][0],edge[0][1])])
    pos1=nx.spring_layout(g)
    nx.draw_spring(g, with_labels=True, node_size=1, font_size=6, font_color='blue')
    plt.savefig(str(file_name) + "_netviz.png")
    plt.clf()
    return g
def write_file(f, fname, title, result):
    f.write(fname+'\t')
    for attr in title:
        f.write(json.dumps(result[attr])+'\t')
    f.write('\n')

if __name__ == "__main__":
    init_flag = True
    for FILE in FILE_LIST:
        filename = FILE.split('/')[1].split('.')[0]
        networkObjects_list = sluglines_to_networkObjects(FILE)
        node_pairs = networkObjects_to_edges(networkObjects_list)
        g = create_network_viz(node_pairs, filename)
        result = graph_info(g)
        if init_flag == True:
            title = sorted(result.keys())
            f = open("graph_info_all.tsv","w")
            f.write("Movie Name\t")
            for attr in title:
                f.write(attr + "\t")
            f.write("\n")
            init_flag = False
        write_file(f,filename,title,result)


      



