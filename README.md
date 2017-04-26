# Action Movie Classification through Scene Transition Network Analysis Measures


Semester Project for Winter 2017 Networks Course

Alex Czarnik, Dalton Simancek, Ruihan Wang, Chengyi Xu
 

## INTRODUCTION
### Motivation and Research Question
Movies are commonly classified in terms of their genre: action, adventure, horror, sci-fi, etc. Each genre category lacks finite criteria making it difficult to directly measure and quantify the characteristics of film narrative. Audiences and critics will instead search for a sample of features or events typically associated with a particular genre. Alien characters signal a sci-fi movie. Director Michael Bay signals an action movie. However, as a result of having loose classification criteria, a movie’s final genre designation may be inconsistent among different audiences and critics or the movie would instead be described in terms of multiple genres, sub- genres and hybrid genres.
As artificial language and image generation tasks grow in sophistication, so does the potential for artificially generated stories, movies and more. To teach computers the nuances of narrative, there emerges a need to formalize narrative features and genre conventions in manner that is quantified and, thereby, “translatable” and usable by artificially intelligent agents.
Projects such as MovieGalaxies (http://moviegalaxies.com/) help to formalize inherent structures embedded in narrative content - in this case, character interactions. Each graph provides an objective and measurable pattern that can be observed and studied for its significance generating data and patterns from a narrative.
Inspired by MovieGalaxies approach of generating social graphs of character interactions in movies, our group was inspired to take this methodology into a new dimension. Movie screenplays contain a semi-formal writing structure consisting of “Slug lines”, which indicate a change in scene. These sluglines offer an opportunity to extract data related to the flow of scene transitions in a movie. Our goal is to use network analysis techniques learned in SI608 to derive a set of useful insights and features from the underlying characteristics of a film’s scene transition network.
 
We hypothesize that movies designated with a particular genre (e.g. Action) will have distinct properties in their scene transition network (centrality measures, # nodes, # Edges, etc.) that can be identified and then used as features to create a machine learning model for classifying movies for a specific genre using the inherent properties of its scene transition network.
For this project, we will generate scene transition network metrics for training data in which each data element (a movie) is classified as either an action movie or a non-action movie. We can use the resulting data to train a supervised machine learning model for classifying action movies based on the properties of a movie’s scene-transition network.
## DATA AND METHODS
To extract slugline data from movie screenplays for generating scene-transition networks, we developed text file and html parsers. These parsers tag and extract all of the scene ‘slugs lines.’ Slug lines are all-caps headings in a screenplay that introduce a new scene and usually contain three pieces of information: whether the scene occurs inside or outside (INT/EXT), the location of the scene (TATOOINE) and some temporal information (DAY).
FIgure 1. A sample slug line (IN ALL CAPS) from Star Wars: A New Hope
The resulting output of the parser is a list of slug lines from a movie screenplay. Each slug line effectively serves as network node with edges between adjacent slug lines in the master list. In summary, a list of slug lines can be used to generate a list of node pairs, providing the requisite data for generating a scene transition network.
 

FIgure 2. A directed scene transition network of Star Wars: A New Hope
With scene-transition graphs we generated network metrics that can be used as features in training a supervised machine learning model.
                                    average_degree
avg_cluster_coe
highest in_degree node betweenness
highest in_degree node closeness
highest out_degree node closeness
largest strongly component average path length
   (undirected)
fficient (transitivity)
                             7.2923076923076
92
0.2798816568047 337
0.1538379451212 65
0.4740740740740 74
0.4444444444444 44
3.1353365384615 3
                                   largest strongly component diameter
largest strongly component percent
number of edges
number of nodes
number of components
Action?
                             7
1
237
65
1
1
                 FIgure 3. Scene transition network metrics of Star Wars: A New Hope, Classification Variable
According to our hypothesis, the network metrics will show a distinctiveness for action movies in relation to other genres of movies. Action movies, for example, often contain fast, chase sequences. In such film sequences, there can be rapid, several second shots between multiple locations(e.g. From inside a spacecraft to back at a command center to inside the lair of the
villain, etc.) Action sequences therefore would generate a higher number of nodes (more locations) and a higher number of edges(more rapid transitions) than a film where a scene spans minutes rather than seconds (e.g. A wedding in a romantic comedy). Furthermore, the rapid scene movement in an action sequence may generate greater clustering of scene transitions than a more linear, evenly-paced sequence.
Using our text and html parsers, we extracted slug lines from 50 different movies - 24 action and 26 non-action. Each of slug lines lists from these movies was transformed into a scene- transition network. An analysis script conducted the following metrics for each scene-transition network: average degree, average clustering coefficient, highest in-degree node betweenness, highest in-degree node closeness, highest out-degree node closeness, largest average path length of largest strongly connected component, diameter of largest largely connected component, largest strongly connected component percent, number of edges, number of nodes and number of components.
The final metrics collected for each scene transition network then serve as features in the training of Support Vector Machine model for an action movie classifier. The 50 movies were divided into testing and training data with network metrics used as training features.

## RESULTS
According to the features of action movies with fast cuts, many locations, lower time per scene and parallel events, we are expected to see more nodes, edges and clusters in action movies. At the same time, due to high amount of scene transitions, the average degree of each node should be higher than other genres. Let’s have a look at some movie network visualizations of different genres. In Figure 4, we listed three directed and weighted scene transition network of 3 action movies: Batman, Air Force One and Spiderman. In Figure 5, we listed three other networks of other genres: My Best Friend’s Weddings, Heathers and Halloween.
FIgure 4. Directed and weighted scene transition network of action movies
   

FIgure 5. Directed and weighted scene transition network of non-action movies
From the network visualizations above, in action movies network, the number of nodes and edges are higher than other non-action movies and the cluster in action movie network is easier to be identified. That means we can easily recognize one or more scenes with a fairly high degree in the network. Also, in each action movie, there are usually several edges with high weights than others implying a high frequency of transitions between two specific scenes.
To obtain an overview of our findings in the whole dataset, we drew two bar charts in Figure 6 and 7 to see top 15 movies with highest nodes and edges. The figures show that most movies with large number of nodes and edges are action movies which can be a proof to our intuition mentioned earlier.
    FIgure 6. Top 15 movies with highest number of nodes

 FIgure 7. Top 15 movies with highest number of edges
When applying the model to the training data, we encountered an issue of predicting only “non- action” movies. After applying the SVM model, modifying multiple parameters and applying cross-validation to test different observations in the training data, our model consistently predicted “non-action” results. Due to this, we are faced with inconclusive results that could be attributed to a number of different factors. These factors are discussed further in “Limitations/Challenges”.
## LIMITATIONS/CHALLENGES
Over the course of the semester, our team faced a number of issues when creating our classification model. Below are a few highlighting the major struggles that we encountered.
### Difficulty of designing a screenplay parser
When collecting the screenplay data, we focused on available screenplays in the format of .txt files. We were able to successfully collect and parse eight scripts through our python script, but hit a wall when we could not find more screenplays in that format. Our python script was only programmed to handle the regex and format of .txt files and we had to find another way to get more screenplays. In order to do this, we decided to tackle any screenplays that were available in an html format. Creating a web scraper and parser, we were able to program a parser that extracted the slugline data and create output files similar to output files created by the .txt files.
Alex Czarnik, Dalton Simancek, Ruihan Wang, Chengyi Xu SI 608 Networks
Course Project
18 April 2017
### Working around the inconsistencies of screenplays
Although we overcame the difficulty of parsing files of a different format, there was another issue with the screenplay files we were parsing. Due to the way different studios and writers created their scripts, not all followed the standard slugline format. There were some movie scripts that indented their lines differently, different placement for characters and different wording to describe actor lines. With a persistent tweaking of the program, we were able to parse out almost all of these flaws to create a standard output from different inputs.
### The inconsistencies of using genres as classification labels
In order to produce a classification model, we realized we would need to manually classify each movie. We approached this with our prior knowledge of a movie as well as IMDB’s genre descriptions and believed that would suffice as a solid classifier. However, in a more structured study, we would need multiple avenues of classification to ensure that the training data was appropriately classified. While IMDB is a trusted movie website, there are no guarantees that their classification is accurate. If we had multiple sites classifying a movie as “action” we could say with more certainty that the movie is indeed “action”.
### Novel area of exploratory data analysis
At the beginning of the semester, we imagined this project take on an exploratory analysis methodology. After the mid-point presentations, we realized we exhausted the data of scenes and locations and wondered where to go with the project. As we began finding patterns between screenplays of similar genres, we believed it possible to create a classification model that would take the information we discovered in the exploratory aspect to classify whether a movie was an action movie or not. This challenge opened our eyes to the possibilities of going further in an area of exploratory analysis that we discovered. Unfortunately, our results proved to be inconclusive.
### Insufficient training/test data
Our biggest issue throughout the semester proved too challenging, as we believe that the lack of data ultimately gave us inconclusive results. As data scientists, we know that the more data we have to train a model, the more certain we can be that our sample size is a non-factor in our analysis. Unfortunately, as we described we had to overcome a few different challenges just to reach the size of 50 movies. If we had accumulated more movies, we might have been able to
classify movies correctly, but due to the small sample size of data, this challenge proved to be too much.

## CONCLUSIONS
We believe that beyond the story and actors of a movie, the interactions and relationships among scenes play an important role in how movies are perceived. By building a technology to visualize movies through networks and data processing, our team wants to create a movie genre classification model. Our idea is to tell the story of a movie by visualizing the screenplays. Besides the visual component, we computed social network metrics that make movies comparable in a new formalized way. From our observations, there might be certain success metrics in the network for classifying action and non-action movie genres. Action movies typically have more number of nodes and edges, as well as greater clustering. While we are convinced that the secret of a good movie lies in the social network structure, we do not disclose these insights right now due to the limitations and challenges stated above. However we are aware of the fact that the movie genre is just one of many layers in a movie and that our results still have to be proven with our further work.

## FURTHER WORK
Our experience shows that networks for movies are a good tool to explain scene transitions and narrative complexities so as to automatically classify movie genres. Recognizing those limitations we’ve encountered, our further work will be done in the following areas. We will build a web scraper and parser that could be used to extracte the slug lines and output them into standard .txt files. We will come up with a standard rule for classifying movies by aggregation of information from trusted movie source websites not limited to IMDB. By solving the problems with designing screenplay parser and setting movie classification standard, we will then be able to collect sufficient amount of data used for training and testing, which will yield more accurate prediction of movie classification. The network shows another form of a movie’s hidden beauty. Our project suggest that the social network design of a movie could be a more influential factor than presently known. We are very looking forward to our further work and deeper analysis of movies.
