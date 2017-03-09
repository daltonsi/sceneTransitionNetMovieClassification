import ast
import networkx as nx
import matplotlib.pyplot as plt

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

def create_network_viz(edge_list, file_name):
    g = nx.Graph()
    for edge in edge_list:
        g.add_edge(edge[0][0],edge[0][1])

    pos1=nx.spring_layout(g)
    nx.draw_spring(g, with_labels=True, node_size=1, font_size=6, font_color='blue')
    plt.savefig(str(file_name) + "_netviz.png")
    plt.clf()
    return 0



if __name__ == "__main__":
    for FILE in FILE_LIST:
        filename = FILE.split('/')[1].split('.')[0]
        networkObjects_list = sluglines_to_networkObjects(FILE)
        node_pairs = networkObjects_to_edges(networkObjects_list)
        create_network_viz(node_pairs, filename)
