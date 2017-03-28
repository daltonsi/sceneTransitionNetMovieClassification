#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
import time
from bs4 import BeautifulSoup
import regex as re
from collections import OrderedDict

def get_soup(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

def write_script(script, movie):
    script = script.split('\n')
    scenes = []
    characters = OrderedDict()
    bool = False
    first_scene = True
    scene_count = 1
    with open('./output/' + movie + '_results.txt', 'w') as f:
        final = []
        for line in script:
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
                scene = re.sub(r'\r', '', scene)
                scenes.append(scene)
                characters[scene] = []

            elif bool:
                result2 = re.search('^\s+([A-Z]{2}.+)(?<![a-z]+)', line)
                if result2:
                    if '!' not in result2.group(1) and ',' not in result2.group(1) and ' ...' not in result2.group(1) \
                            and ' - ' not in result2.group(1) and ':' not in result2.group(1) and len(result2.group(1)) < 25 \
                            and 'FADE' not in result2.group(1) and 'THE END' not in result2.group(1):
                        character = re.sub(r'^\s+', '', result2.group(1))
                        character = re.sub(r'\r', '', character)
                        characters[scene].append(character)
        if characters[scene]:
            final.append(str(scene_count) + ':\t' + str(scene) + ':\t' + str(characters[scene]))
            scene_count += 1
        else:
            final.append(str(scene_count) + ':\t' + str(scene) + ':\t' + 'None')
            scene_count += 1
        for line in final:
            f.write(line + '\n')


def extract_text(soup):
    #Find all instances of text block in the code
    text = soup.find("pre")
    #Case by case for each difference in text blocks
    #Get text and split, remove Author and heading information (i.e. anything with HealthDay)
    if text:
        return text.text

#Call the extract methods and write the results to an output file
def movie_extract(url):
    split_url = url.split('.htm')[0].split('/')
    movie = split_url[-1]
    # Extract Soup Object
    soup = get_soup(url)
    # Extract Script Text
    result = extract_text(soup)
    write_script(result, movie)

def main():
    #Get urls and timestamps
    filename = "./input/link.txt"
    input = open(filename, "r")
    for i in input:
        movie_extract(i.split('\n')[0])
        time.sleep(5)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()