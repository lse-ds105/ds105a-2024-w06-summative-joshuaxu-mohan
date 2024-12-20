[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/16Ytx_fz)

# What you will find here
In this repository, you will find Jupyter Notebook(s), csv files, visualised data and more to answer the question: 

***"Is London really as rainy as the movies make it out to be?"***

![image](./TitleImage.png)

*Source: [GencraftAI](https://gencraft.com/generate)*

# How I will be approaching this question
In order to answer this question, it is clear that I have to compare the weather of London with other cities in the world, using OpenMeteo's free API.

**To answer <ins>yes</ins> would require London to be a clear outlier in terms of 'raininess' when compared with other cities.** 

To do this, the parameters of the comparison is as follows:
- **Time Period** - 2023-01-01 to 2024-01-01
- **Other Cities** - 10 other cities will be chosen using a random capital city generator which I will create.
- **'Raininess'** - A composite measurement of frequency of rainy days, Precipitation Sum, Rain Sum, Shower Sum and Precipitation Hours
- **OpenMeteo Variables** - Daily Weather Variables: Weather Code, Precipitation Sum, Rain Sum, Showers Sum, Precipitation Hours.

# How to run the codes
To simply follow along my exploratory process to answer the question, it will be sufficient to simply follow the Jupyter Notebooks in the following order:
1. [Jupyter Notebook of Randomiser](../ds105a-2024-w06-summative-joshuaxu-mohan/Sampling/Randomiser.ipynb)
2. [Jupyter Notebook of Data Collection](../ds105a-2024-w06-summative-joshuaxu-mohan/DataCollection/DataCollection.ipynb)
3. [Jupyter Notebook of Data Analysis](../ds105a-2024-w06-summative-joshuaxu-mohan/DataAnalysis/DataAnalysis.ipynb)
4. [Jupyter Notebook of Data Visualisation](./DataAnalysis/DataVisualisation.ipynb)


Using VSCode/Nuvolos, you can run the code cells under the approrpiate Python environment (3.10+).

Enjoy!
