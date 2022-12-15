import streamlit as st
from transformers import pipeline
import requests
from bs4 import BeautifulSoup
#"https://en.wikipedia.org/wiki/Andor_(TV_series)"
def text_recovery(url):
    # Make a  request to the URL
    response = requests.get(str(url))
    print("ba")

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    print("ba1")

    # Find the table that contains the episode summary

    table = soup.find('table', {'class': 'wikiepisodetable'})
    text = []
    print("ba2")

    # Iterate over the rows in the table
    for row in table.find_all('tr'):
        # Find the cells in each row
        print("ba3")

        cells = row.find_all('td')
        print("ba4")

        # If the row contains episode data
        if len(cells) == 1:
            # Extract the episode number, title, and summary
            episode_summary = cells[0].text
            print("ba5")

            # Print the episode data
            text.append(episode_summary)
            print("ba5")
    for i in range(len(text)):
        st.write(text[i])
            
    

# Create the main app
def main():
    st.title("Text Summarization with Hugging Face")

    # Get the input text from the user
    url = st.text_area("Enter the link of the wikipedia page")
    result = st.button('Run on url')
    if result:
        text_recovery(url)
    


if __name__ == "__main__":
    main()
