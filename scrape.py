from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

def imdb_movies_scraper():

    def extract_text_in_parentheses(text):
        """
        Extracts and returns the text inside parentheses from the given string.
        
        Parameters:
        - text (str): The input string containing parentheses.
        
        Returns:
        - str: The text inside the first set of parentheses, or None if no parentheses are found.
        """
        match = re.search(r'\((.*?)\)', text)
        if match:
            return match.group(1).strip()
        return None

    def parse_duration(duration_text):
        """
        Parses the duration string and converts it to minutes.
        
        Parameters:
        - duration_text (str): Duration text in the format "Xh Ym".
        
        Returns:
        - int: Duration in minutes.
        """
        if 'h' in duration_text and 'm' in duration_text:
            parts = duration_text.split(' ')
            hours = int(parts[0].replace('h', ''))
            minutes = int(parts[1].replace('m', ''))
            return hours * 60 + minutes
        return 0

    def parse_voting(voting_text):
        """
        Parses the voting text and converts it to a numeric value.
        
        Parameters:
        - voting_text (str): Voting text in the format "(X.YM)" or "(X.YK)".
        
        Returns:
        - float: Voting count in numeric form.
        """
        voting_info = extract_text_in_parentheses(voting_text)
        if voting_info:
            if voting_info.endswith("M"):
                return float(voting_info.split('M')[0]) * 1_000_000
            elif voting_info.endswith("K"):
                return float(voting_info.split('K')[0]) * 1_000
            else:
                return float(voting_info)
        return 'N/A'

    chrome_options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    driver.get(url)
    
    time.sleep(5)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    
    movies = soup.find_all("li", class_="ipc-metadata-list-summary-item")
    
    movie_list = []
    for index, movie in enumerate(movies):
        link_tag = movie.find("a", class_="ipc-title-link-wrapper")
        title_tag = link_tag.find("h3", class_="ipc-title__text")
        rating_tag = movie.find("span", class_="ipc-rating-star--rating")
        voting_tag = movie.find("span", class_="ipc-rating-star--voteCount")
        metadata_div = movie.find("div", class_="sc-b189961a-7")
        
        if not (link_tag and title_tag and metadata_div):
            continue
        
        voting_text = voting_tag.text.strip() if voting_tag else "N/A"
        voting_info = parse_voting(voting_text)
        
        title = title_tag.text.strip()
        title = re.sub(r'^\d+\.\s*', '', title).strip()  # Remove leading numbers and dots
        
        link = "https://www.imdb.com" + link_tag['href']
        metadata_info = metadata_div.find_all("span")
        year = int(metadata_info[0].text.strip()) if len(metadata_info) > 0 else 'N/A'
        rating = float(rating_tag.text.strip()) if rating_tag else 'N/A'
        
        duration = metadata_info[1].text.strip() if len(metadata_info) > 1 else 'N/A'
        duration_minutes = parse_duration(duration)
        
        movie_list.append({
            "title": title,
            "year": year,
            "rating": rating,
            "voting": voting_info,
            "duration": duration_minutes,
            "link": link
        })
        
        print(f"Scraped movie {index + 1}: {title}, Year: {year}, Rating: {rating}, Vote: {voting_info}, Duration: {duration_minutes}, Link: {link}")
        
        time.sleep(1.5)
    
    return pd.DataFrame(movie_list)


# Run the scraper and save the results to a CSV file
movies_df = imdb_movies_scraper()
if not movies_df.empty:
    movies_df.to_csv("imdb.csv", index=False)
else:
    print("No movies were found.")
