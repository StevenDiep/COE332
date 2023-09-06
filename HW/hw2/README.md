# Homework 2 guide

In this readme, I'm going to explain a general description of tools, how to run the scripts directly, how to build the image, how to run the scripts inside the container, and how to run the unittests.

##General description of the tools

We first start off with generate_animals.py and read_animals.py. generate_animals.py will generate the 20 animals needed for the data our project needs to work with. The data generated will be in the form of a json file, which you will later name yourself.

For my feature that I added, I implemented a summary statistics function. This function will read in the data from the json file and give summary statistics. This includes the number of heads for each type of animal, the average number of arms, average number of legs, and the average number of tails.

read_animals.py will then read in a json file and provide the summary statstics I explained above.

Also included are Dockerfile and docker-compose.yml which will be used to run your containters.

##Installation and running scripts

On your command line, cd to the place you want to keep the diretory you are about to pull. Once there, run the following command:

'''bash
git clone https://github.com/StevenDiep/COE332
'''

Once you have the repo installed, go ahead and

'''bash
cd /HW/hw2
'''

Once there, run 

'''bash
generate_animals.py animals.json
'''
