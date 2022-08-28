# http_get_python
HTTP GET method to retrieve information from a films DB Given a string substr, the function getMovieTitles() must perform the following tasks:
1. Query https://jsonmock.hackerrank.com/api/movies/search/?Title=substr (replace substr, You can check (https://jsonmock.hackerrank.com/api/movies/search/?Title=Superman)).
2. Initialize the titles array to store total string elements. Store the Title from each record returned in the data field to the titles array.
3. Sort titles in ascending order and return it as the answer.
The query response from the website is a JSON response with the following five fields:
- page : The current page
- per_page : The maximum number of results per page
- total : The total number of records in the search result
- total_pages : The total number of pages which must be queried to get all the results
- data : Data: An array of JSON objects containing movie information where the Title field denotes the title of the movie. In order to get all results, you may have to make multiple page requests. To request a page by number, your query should
read https://jsonmock.hackerrank.com/api/movies/search/?Title=substr&page=p ageNumber, replacing substr and pageNumber
