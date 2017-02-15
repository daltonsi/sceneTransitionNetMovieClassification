import regex as re

file = open('empire_strikes_back_screenplay.txt', 'r')

scenes = []
for line in file:
    result = re.search(r'((?:EXT|INT) .+)\s+', line)
    if result:
        scene = re.sub(r'\s+\d+', '', result.group(1))
        scenes.append(scene)

# TODO: GRAB CHARACTERS WITHIN A SCENE
# \s+(\D+)\s
file = open('empire_results.txt', 'w')
for item in scenes:
  file.write("%s\n" % item)
