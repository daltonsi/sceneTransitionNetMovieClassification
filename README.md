# screenplay_scene_transition_network_analysis

Project Proposal – Screenplay Scene Transition Network Analysis
Dalton Simancek

Group Members: Alex Czarnik, Ruihan Wang, Chengyi Xu
 
Data: Screenplay(s) from IMSDB (http://www.imsdb.com/)
 
Inspired by Moviegalaxies social graphs depicting character interaction in movies, our project seeks to parse screenplays for scene transitions to generate and analyze scene graphs of movies.
 
The data will be obtained by writing a python script that parses the screenplay by tagging and extracting all of the scene ‘slugs lines’ (e.g. EXT. PARK DAY).  Slug lines are all-caps headings in a screenplay that introduce a new scene and usually contain three pieces of information: whether the scene occurs inside or outside (INT/EXT), the location of the scene (PARK) and some temporal information (DAY).  The resulting list of slug lines can be used to generate a list of node pairs, where each node represents a scene and the presumptive directed edge between them indicates a scene transition.  From there, we can use the node pairs and write a python script to generate and explore the resulting scene transition network.
 
Our goal is to use network analysis techniques learned in SI608 to derive a set of useful insights and features from the underlying characteristics of a film’s scene transition network. There are many potential directions we could explore the through the examination of multiple scene transition networks – 1.  Deriving genre-specific network features ( e.g. clusters of night time scenes in horror movies), 2. clustering patterns of scenes occurring in similar geographic locations and/or concurrent events happening in different locations.
 
We have also discussed the project of using the inside/outside and temporal information within the slug line to encode additional data in the resulting scene transition graphs (e.g. Scenes locations that more commonly occur in the day will be yellow, at night blue). 
 
We intend to begin our project using a small sample of screenplays of our choosing.  However, as the project evolves, we may shift our focus to a specific subset of movies (e.g. most popular science fiction movies). 
