# Big Data Assignment 1


This Dockerfile sets up an environment for performing big data processing tasks using Python and associated libraries.


## Environment Setup


- **Base Image**: Ubuntu latest
- **Python Version**: 3
- **PIP Timeout**: 2000 milliseconds


## Installed Packages


The following Python packages are installed using pip:


- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn


## Directory Structure


The Docker container is configured with the following directory structure:


- `/home/doc-bd-a1/`: Main working directory within the container.
  - `load.py`: Python script for loading datasets.
  - `model.py`: Python script for implementing machine learning models.
  - `dpre.py`: Python script for data preprocessing.
  - `eda.py`: Python script for exploratory data analysis.
  - `vis.py`: Python script for generating visualizations.
  - `Titanic-Dataset.csv`: Sample dataset for testing purposes.


Build Docker Image:
docker build -t bd-a1-image .


Run Docker Container:
docker run -it  bd-a1-image


Execute load and run other Files:
Python3 load.py “Titanic-Dataset.csv”


Execute Final Script and Copy Output Files:
./final.sh 


final.sh contain:
#!/bin/bash
mkdir -p bd-a1/service-result (Make a directory in bd-a1 called service-result )


Ever one of these take container id and file to download and put it in service-result:
docker cp cc192d1c389a:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/
docker cp cc192d1c389a:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
docker cp cc192d1c389a:/home/doc-bd-a1/eda-in-2.txt bd-a1/service-result/
docker cp cc192d1c389a:/home/doc-bd-a1/eda-in-3.txt bd-a1/service-result/
docker cp cc192d1c389a:/home/doc-bd-a1/vis.png bd-a1/service-result/
docker cp cc192d1c389a:/home/doc-bd-a1/k.txt bd-a1/service-result/


docker stop cc192d1c389a(stop container with id)
