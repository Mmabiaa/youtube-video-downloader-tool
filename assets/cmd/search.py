import requests
from bs4 import BeautifulSoup

def search_videos(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    videos = []
    for item in soup.find_all('h3', class_='title-and-badge'):
        title = item.find('a').text
        link = "https://www.youtube.com" + item.find('a')['href']
        videos.append((title, link))
    
    return videos

def main():
    query = input("Enter search query: ")
    results = search_videos(query)

    print("\nSearch Results:")
    for title, link in results:
        print(f"{title}: {link}")

if __name__ == "__main__":
    main()
