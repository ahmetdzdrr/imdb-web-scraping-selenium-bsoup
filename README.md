# IMDb Top 250 Movies Scraper

![image](https://github.com/user-attachments/assets/79fffa26-a33c-4f44-a79c-4fc41f33ba75)

This project provides a Python-based solution to scrape IMDb's Top 250 movies list using Selenium and BeautifulSoup. The script extracts detailed movie information including title, year, rating, votes, and duration, and saves it in a CSV file for further analysis.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Setup](#setup)
   - [Installing Dependencies](#installing-dependencies)
   - [Running the Scraper](#running-the-scraper)
4. [Output](#output)
5. [Example Output](#example-output)
6. [Notes](#notes)
7. [License](#license)

## Features

- Scrapes IMDb's Top 250 movies list
- Extracts and cleans up movie titles, release years, IMDb ratings, vote counts, and durations
- Handles dynamic content loading with Selenium
- Parses and formats data using BeautifulSoup and regular expressions
- Outputs results to a CSV file for easy access and analysis

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup
- `webdriver-manager`
- pandas

## Setup

### Installing Dependencies

1. Clone the Repository:

        git clone https://github.com/yourusername/imdb-web-scraping-selenium-bsoup.git
        cd imdb-web-scraping-selenium-bsoup

2. Install Python Dependencies:

Ensure you have Python 3.x installed and then install the necessary libraries:

    pip install -r requirements.txt

## Running The Scraper

1. Run the Scraper:

Execute the Python script to start the scraping process:

    python scrape.py

2. Check the Output:
After execution, you will find the scraped data saved in `imdb.csv`.

## Output

The script generates a CSV file named imdb.csv with the following columns:

- **title**: Movie title
- **year**: Release year
- **rating**: IMDb rating
- **voting**: Number of votes (numeric value)
- **duration**: Duration in minutes
- **link**: IMDb movie URL

## Example Output

    Scraped movie 1: The Shawshank Redemption, Year: 1994, Rating: 9.3, Vote: 2,366,758, Duration: 142, Link: https://www.imdb.com/title/tt0111161/?ref_=chttp_t_1

## Notes

- Ensure that you have a stable internet connection as the script fetches data from the web.
- The scraping delay (time.sleep(1.5)) is added to avoid overloading IMDb's servers and to simulate human-like browsing behavior.
- This script uses Selenium for handling dynamic content loaded via JavaScript.

## License

This project is licensed under the MIT License. See the LICENSE file for details.



