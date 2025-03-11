import requests
import csv
import sys

def fetch_research_papers(query, output_file):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&fields=title,authors,year,abstract"
    response = requests.get(url)
    papers = response.json()['data']

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Title', 'Authors', 'Year', 'Abstract'])

        for paper in papers:
            # Handle missing authors by assigning "Unknown"
            authors = ", ".join([author['name'] for author in paper.get('authors', [])]) if 'authors' in paper else "Unknown"
            year = paper.get('year', 'Unknown')
            abstract = paper.get('abstract', 'No abstract available')
            title = paper.get('title', 'Untitled')

            csvwriter.writerow([title, authors, year, abstract])
    
    print(f"Research papers fetched successfully and saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[2] != '-f':
        print("Usage: python fetch_research_papers.py <query> -f <output_file>")
    else:
        query = sys.argv[1]
        output_file = sys.argv[3]
        fetch_research_papers(query, output_file)
