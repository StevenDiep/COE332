# Homework 2 guide

In this readme, I'm going to explain a general description of tools, how to run the scripts directly, how to build the image, how to run the scripts inside the container, and how to run the unittests.

## General description of the tools

We first start off with generate_animals.py and read_animals.py. generate_animals.py will generate the 20 animals needed for the data our project needs to work with. The data generated will be in the form of a json file, which you will later name yourself.

For my feature that I added, I implemented a summary statistics function. This function will read in the data from the json file and give summary statistics. This includes the number of heads for each type of animal, the average number of arms, average number of legs, and the average number of tails.

read_animals.py will then read in a json file and provide the summary statstics I explained above.

Also included are Dockerfile and docker-compose.yml which will be used to run your containters.

## Installation and running scripts

On your command line, cd to the place you want to keep the diretory you are about to pull. Once there, run the following command:

```bash
git clone https://github.com/StevenDiep/COE332
```

Once you have the repo installed, go ahead and

```bash
cd /HW/hw2
```

Once there, run 

```bash
python3 generate_animals.py animals.json
```

This will generate a json file that holds data on the 20 animals you just created. To check that the program ran smoothly, type:

```bash
cat animals.json
```

You should see the first couple of lines as:

{
  "animals": [
    {
      "head": "bull",
      "body": "snake-sponge",
      "arms": 10,
      "legs": 3,
      "tail": 13
    },

Next, you can run

```bash
python3 read_animals.py animals.json
```

To see the summary statistics for our data, the output should read:

{'head_count': {'snake': 3, 'bull': 3, 'lion': 6, 'raven': 5, 'bunny': 3}, 'avg_arms': 6.4, 'avg_legs': 7.35, 'avg_tails': 13.75}
    
## Building a docker image with the given dockerfile

First thing you should make sure before running the commands is that your Docker is open and running

then run the following command:

```bash
docker build -t stevendiep/hw2:1.0 .
```

This will build our docker image, once you build the image, you can run it and type the interactive commands needed to run the code in our container

## Running our code in the interactive container

```bash
docker run --rm -it stevendiep/hw2:1.0 /bin/bash
```

Once in the interactive state, run:

```bash
generate_animals.py animals.json
```

```bash
read_animals.py animals.json
```

This will generate the 20 animals and read the summary statstics in that order within the interactive prompt


## How to run unit tests

Navigate to the test folder of hw2

Once you are in the folder, you can run

```bash 
python3 test_read_animals.py
```

To check if our unit tests have passed






