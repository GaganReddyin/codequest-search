# CodeQuest-SearchEngine
forgot the question name of a particular website. No worries, go to our website and search for your questions by putting relevant keywords and hit search; you can also set the platform you wanna stick to.


# Search Engine
 
A search engine that allows users to search for questions based on their query. The search engine consists of three main stages: web scraping, TF-IDF algorithm, and a Node.js and React web application.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Web scraping: The search engine scrapes question data from websites such as LeetCode, Codeforces, and CodeChef using Beautiful Soup and Selenium.
- TF-IDF algorithm: It implements the TF-IDF algorithm to find potential documents (questions) related to the user's query.
- Web application: The search engine is integrated into a web application built with Node.js and React, allowing users to search for questions and view the results.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/GaganReddyin/CodeQuest-SearchEngine.git

2. Install dependencies:

- Make sure you have beautiful soup and selenium installed in your workspace

  ```shell
  pip install bsoup
  ```
  ```shell
  pip install selenium

- if getting error after installing the libraries

  ```shell
  pip install -user bsoup selenium
  ```
for intalling it globally

- For hosting the backend locally go to Website/Backend

  ```shell
  npm install
  ```

  ```shell
  node server.js
  ```
- For hosting the frontend locally go to Website/Frontend/my_app/

  ```shell
  npm install
  ```
  ```shell
  npm start
  ```
- Now you are good to go, now the website will be hosted on http://localhost:3000

## Usage

1. Perform a search:

- Enter a query in the search box.
-  Select the website you want to search
- The search engine will process the query using the TF-IDF algorithm and display relevant questions as results.

