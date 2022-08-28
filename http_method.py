import requests
import sys
import json
substring = sys.argv[1]

class movie():
     
    # init method or constructor
    def __init__(self, substring):
        self.substring = substring

    # Function to sort movie titles 
    def getMovieTitles(self):
        url = "https://jsonmock.hackerrank.com/api/movies/search/?Title={}".format(self.substring) # Using String Interpolation for formating url 
        response = requests.get(url)
        value = response.json()
        title = []

        #looping based on the total number pages to pagination 
        for page in range(value.get('total_pages')):
            title_data = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}".format(self.substring,page)).json()
            for per_page in range(value.get('per_page')):
                title.append(title_data['data'][per_page]['Title'])
        
        #print("Unsorted Titles:", title )
        return sorted(title)

if __name__ == '__main__':
    titles = movie(substring)
    sorted_titles = titles.getMovieTitles()
    print("Sorted Titles",sorted_titles)
