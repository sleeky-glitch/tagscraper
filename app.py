import streamlit as st
import requests
from bs4 import BeautifulSoup

def fetch_links(url, tag):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True) if tag in a['href']]
        return links
    except requests.RequestException as e:
        st.error(f"Error fetching the URL: {e}")
        return []

def main():
    st.title("News Website Link Scraper")
    st.write("Enter a news website URL and a tag to find all links containing that tag.")

    url = st.text_input("News Website URL", "https://example.com")
    tag = st.text_input("Tag to search for in links", "news")

    if st.button("Scrape Links"):
        if url and tag:
            with st.spinner("Scraping links..."):
                links = fetch_links(url, tag)
                if links:
                    st.success(f"Found {len(links)} links containing the tag '{tag}':")
                    for link in links:
                        st.write(link)
                else:
                    st.warning("No links found with the specified tag.")
        else:
            st.error("Please enter both a URL and a tag.")

if __name__ == "__main__":
    main()
