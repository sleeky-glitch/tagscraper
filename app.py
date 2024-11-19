import streamlit as st
import requests
from bs4 import BeautifulSoup

def fetch_article_links(base_url, search_tag):
  try:
      response = requests.get(base_url)
      response.raise_for_status()
      soup = BeautifulSoup(response.text, 'html.parser')
      # Find all links that contain the search tag
      links = [a['href'] for a in soup.find_all('a', href=True) if search_tag.lower() in a.text.lower()]
      return links
  except requests.RequestException as e:
      st.error(f"Error fetching the URL: {e}")
      return []

def main():
  st.title("News Article Link Scraper")
  st.write("Enter a news website URL and a tag to find all article links containing that tag.")

  base_url = st.text_input("News Website URL", "https://example.com")
  search_tag = st.text_input("Tag to search for in articles", "technology")

  if st.button("Search Articles"):
      if base_url and search_tag:
          with st.spinner("Searching for articles..."):
              links = fetch_article_links(base_url, search_tag)
              if links:
                  st.success(f"Found {len(links)} articles containing the tag '{search_tag}':")
                  for link in links:
                      st.write(link)
              else:
                  st.warning("No articles found with the specified tag.")
      else:
          st.error("Please enter both a URL and a tag.")

if __name__ == "__main__":
  main()
