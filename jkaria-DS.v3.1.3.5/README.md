# Spotify Top 50 Tracks - 2020: A Pandas Learning Project

## Overview

This project is designed as a hands-on learning experience to practice working with the Pandas library in Python. By exploring the **Top 50 Spotify Tracks of 2020** dataset from Kaggle, you will hone your skills in data manipulation, cleaning, and analysis.

- **Dataset**: [Top 50 Spotify Tracks - 2020](https://www.kaggle.com/datasets/atillacolak/top-50-spotify-tracks-2020)
- **Objective**: Gain practical experience in performing exploratory data analysis (EDA) with Pandas.

## Objectives

1. **Work with Kaggle Data**: Download and work with a dataset from Kaggle.
2. **Perform Exploratory Data Analysis (EDA)**: Gain insights by analyzing the dataset.
3. **Practice Data Handling**: Use Pandas to clean, query, and filter the data.

## Project Requirements

### Dataset Overview
- Download the **Spotify Top 50 Tracks of 2020** dataset from Kaggle.
- Load the data into a Pandas DataFrame.

### Data Cleaning
- Handle **missing values**.
- Remove **duplicate samples and features**.
- Address **outliers** in the data.

### Exploratory Data Analysis (EDA)
Use Pandas to explore and answer the following questions:

#### General Insights
- How many observations are there in the dataset?
- How many features does the dataset contain?
- Which features are **categorical** and which are **numeric**?

#### Artists & Albums Analysis
- Are there any artists with more than one track in the top 50? If yes, which artists and how many tracks do they have?
- Who was the most popular artist in 2020?
- How many unique artists have songs in the top 50?
- Are there any albums with more than one track in the top 50? If yes, which albums and how many tracks do they have?
- How many unique albums are represented in the top 50?

#### Track Analysis
- Which tracks have a **danceability score** above 0.7? Below 0.4?
- Which tracks have **loudness** above -5 dB? Below -8 dB?
- Which track is the **longest**? Which is the **shortest**?

#### Genre Insights
- Which genre is the most popular in the top 50?
- Which genres have only one song in the top 50?
- How many genres are represented in the top 50?

#### Feature Correlation
- Which features have a **strong positive correlation**?
- Which features have a **strong negative correlation**?
- Which features show **no correlation**?

#### Comparative Genre Analysis
- How do the following features compare between **Pop**, **Hip-Hop/Rap**, **Dance/Electronic**, and **Alternative/Indie** genres?
  - **Danceability**
  - **Loudness**
  - **Acousticness**

## Notebook Guidelines

In your Jupyter notebook, provide clear explanations throughout your analysis. Each section should inform the reader of:
- **The goal**: What are you trying to achieve?
- **The results**: What did you find?
- **The interpretation**: What do these results mean?

Additionally, include suggestions on how your analysis could be improved or extended in the future.

## Evaluation Criteria

Your project will be evaluated based on the following:

1. **Adherence to Requirements**  
   - Did you meet the project objectives and answer the analysis questions?
   
2. **Code Quality**  
   - Is your code well-structured and organized?
   - Have you removed unused or commented-out code?
   - Have you followed Python's **PEP8** style guide?

3. **Code Performance**  
   - Have you used efficient algorithms and data structures?
   - Is your code optimized for performance?
