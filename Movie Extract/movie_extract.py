import regex as re
from collections import OrderedDict

movies = ['austinpowers',
          'batman',
          'blade_runner',
          'empire_strikes_back',
          'jerry_maguire',
          'mybestfriendswedding',
          'star_wars',
          'titanic']
for movie in movies:
    file = open('./input/' + movie + '.txt', 'r')

    scenes = []
    characters = OrderedDict()
    bool = False
    first_scene = True
    scene_count = 1
    with open('./output/' + movie + '_results.txt', 'w') as f:
        final = []
        for line in file:
            result = re.search(r'((?:EXT|INT).+)', line)
            if result:
                if first_scene:
                    first_scene = False
                else:
                    if characters[scene]:
                        final.append(str(scene_count) + ':\t' + str(scene) + ':\t' + str(characters[scene]))
                        scene_count += 1
                    else:
                        final.append(str(scene_count) + ':\t' + str(scene) + ':\t' + 'None')
                        scene_count += 1
                bool = True
                scene = re.sub(r'\s+\d+', '', result.group(1))
                scenes.append(scene)
                characters[scene] = []

            elif bool:
                result2 = re.search('^\s+([A-Z]{2}.+)(?<![a-z]+)', line)
                if result2:
                    if '!' not in result2.group(1) and ',' not in result2.group(1) and ' ...' not in result2.group(1) \
                            and ' - ' not in result2.group(1) and ':' not in result2.group(1)\
                            and len(result2.group(1)) < 35:
                        character = re.sub(r'^\s+', '', result2.group(1))
                        characters[scene].append(character)
        if characters[scene]:
            final.append(str(scene_count) + ':\t' + str(scene) + ':\t' + str(characters[scene]))
            scene_count += 1
        else:
            final.append(str(scene_count) + ':\t' + str(scene) + ':\t' + 'None')
            scene_count += 1
        for line in final:
            f.write(line + '\n')