"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Lubomír Smola
email: L.smola@seznam.cz
"""
# Library imports
import requests
from bs4 import BeautifulSoup
import argparse
import csv

# Election path (update if the source site changes election year or path)
ELECTION_PATH = "ps2017nss"

# Functions for project
def check_arg(url, output_file):
    """Checks the validity of the provided arguments."""
    if url is not None and output_file is not None:
        if output_file.endswith(".csv"):
            return True
        else:
            print("Špatný formát souboru! Použijte koncovku .csv")
            return False
    else:
        print("Musíte zadat URL i jméno výstupního souboru.")
        return False
    
def fetch_url_content(url):
   """Fetches the content of the given URL."""
   response = requests.get(url)
   response.raise_for_status()
   response.encoding = "utf-8"
   return response.text

def scrape_villages(url):
    """Scrapes list of villages."""
    villages = []
    html = fetch_url_content(url)
    soup = BeautifulSoup(html, "html.parser")
    output_rows = soup.find_all("tr")[2:]

    for row in output_rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            code = cols[0].text.strip()
            location = cols[1].text.strip()
            a_tag = cols[0].find("a")
            link = a_tag.get("href") if a_tag else None
            if link:
                full_link = f"https://www.volby.cz/pls/{ELECTION_PATH}/{link}"
                villages.append((code, location, full_link))
    return villages
    
def scrape_voting_data(village):
    """Scrapes voting data for a given village and returns a dictionary."""
    code, location, link = village
    html = fetch_url_content(link)
    soup = BeautifulSoup(html, 'html.parser')
    party_names = []
    party_votes = []
    
    try:
        tables = soup.find_all('table')

        # Get basic voter data
        main_data = tables[0].find_all('td', class_='cislo')
        registered = main_data[3].text.strip().replace('\xa0', '')  # Fourth cell
        envelopes = main_data[4].text.strip().replace('\xa0', '')  # Fifth cell
        valid = main_data[7].text.strip().replace('\xa0', '')      # Eighth cell

        # Get data about political parties (from both tables)
        for table in tables[1:3]:  # Scraping from two tables
            names = [name.text.strip() for name in table.find_all('td', class_='overflow_name')]
            votes = [votes.text.strip().replace('\xa0', '') for votes in table.find_all('td', class_='cislo')[1::3]]
            party_names.extend(names)
            party_votes.extend(votes)

        party_votes_dict = dict(zip(party_names, party_votes))
        entry = {
            "code": code,
            "location": location,
            "registered": registered,
            "envelopes": envelopes,
            "valid_votes": valid,
            "party_votes": party_votes_dict
        }
        return entry
    except (IndexError, AttributeError) as e:
        print(f"Chyba při parsování dat pro {location}: {e}")
        entry = {
            "code": code,
            "location": location,
            "registered": '',
            "envelopes": '',
            "valid_votes": '',
            "party_votes": {}
        }
        return entry

def save_to_csv(data, output_file):
    """
    Saves the scraped data to a CSV file.

    Args:
        data (list): List of dictionaries, each containing keys:
            - "code": str
            - "location": str
            - "registered": str
            - "envelopes": str
            - "valid_votes": str
            - "party_votes": dict (party name as key, votes as value)
        output_file (str): Path to the output CSV file.
    """
    if not data:
        print("Žádná data k uložení.")
        return
    all_parties = set()
    for entry in data:
        all_parties.update(entry["party_votes"].keys())
    all_parties = sorted(all_parties)

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        header = ["Code", "Location", "Registered", "Envelopes", "Valid Votes"] + all_parties
        writer.writerow(header)
        for entry in data:
            row = [
                entry["code"],
                entry["location"],
                entry["registered"],
                entry["envelopes"],
                entry["valid_votes"]
            ] + [entry["party_votes"].get(party, 0) for party in all_parties]
            writer.writerow(row)
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrapování volebních dat do .csv souboru.")
    parser.add_argument("--url", help="URL stránky se seznamem vesnic.")
    parser.add_argument("--output_file", help="Výstupní CSV název souboru (musí končit s .csv)")
    args = parser.parse_args()

    url = args.url
    output_file = args.output_file

    if check_arg(url, output_file):
        villages = scrape_villages(url)
        all_data = []
        for village in villages:
            entry = scrape_voting_data(village)
            all_data.append(entry)

        save_to_csv(all_data, output_file)
        print(f"Data úspěšně uložena do {output_file}")
    else:
        print("Špatné argumenty. Zkontrolujte a zkuste znova. Přečtěte si README.md pro příklad použití")