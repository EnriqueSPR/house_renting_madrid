from bs4 import BeautifulSoup
import requests
import csv

# Some websites automatically block any kind of scraping, and that’s why
# I’ll define a header to pass along the get command, which will basically
# make our queries to the website look like they are coming from an actual browser.

headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

# Then we define the base url to be used when querying the website
idealista = "https://www.pisos.com/alquiler/pisos-madrid_capital_zona_urbana/16"
source = requests.get(idealista, headers=headers).text

# And now we can test if we can communicate with the website. You can get several codes from this command,
# but if you get “200” it’s usually a sign that you’re good to go. You can see a list of these codes here:
# "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes".

# We can print the response and the first 1000 characters of the text.

# print(response)
#
# print(response.text[:1000])

# Alright, we’re all set to start exploring whatever we get from the website.
# We need to define the Beautiful Soup object that will help us read this html.
# That’s what BS does: it picks the text from the response and parses the information
# in a way that makes it easier for you to navigate in its structure and get its contents.

html_soup = BeautifulSoup(source, 'lxml')

# A big part of building a web scraping tool is navigating through the source code of the web pages we’re scraping from.
#  The chunk of text above is just a part of the whole page. You can check it out in your browser,
#  if you right click the page and select View Source Code or inspect to open the code on the right side to inspect the items of the website

# Before extracting the price, we want to be able to identify each result in the page

house_containers = html_soup.find_all('div', class_="information")

# We now have an object that can be iterated while we scrape the results in each search page.

#  Let’s try and get the price we saw before. I’ll define the variable first which will be the structure of our first house (picked up from the house_containers variable).

# last_house = house_containers[27] # We can access each block by passing the index (30 adds per page -> 0-29)

# print("======================")
#
# for i in range(len(last_house)):
#     print (("This is the item number : {}").format(i), (last_house.find_all('div')[i].text.strip()))

# So we can see that the info of each house property is in different indexes within the div block for each house
# print("======================")


# # 1) Price: index = 1
# print(last_house.find_all('div')[1].text.strip())
#
# # 2) Location index = 4
# print(last_house.find_all('div')[4].text.strip())
#
# # 3) Description index = 5
# print(last_house.find_all('div')[5].text.strip())
#
# # 4) Area index = 7
# print(last_house.find_all('div')[7].text.strip())
#
# # 5) Bedrooms index = 8
# print(last_house.find_all('div')[8].text.strip())
#
# # 6) Bathrooms index = 9
# print(last_house.find_all('div')[9].text.strip())


print("Prices======================")

prices = html_soup.find_all('div', class_="price")  # We can get the list of all 30 accomodation prices
location = html_soup.find_all('div', class_="location")
characteristics = html_soup.find_all('div', class_="characteristics")

prices_list = []
location_list = []
sq_mt_list = []
bedroom_list = []
bathroom_list = []

csv_file = open("rent_scrapper4.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["rent_price", "location", "sq_mt", "bedroom_n", "bathroom_n"])  # Naming the columns

for i in range(len(house_containers)):
    prices_list.append(prices[i].text.strip())
    location_list.append(location[i].text.strip())
    sq_mt_list.append(characteristics[i].div.text.strip())
    bedroom_list.append(characteristics[i].div.find_next('div').text.strip())
    bathroom_list.append(characteristics[i].div.find_next('div').find_next('div').text.strip())
    # Lets save it to a csv file(each iteration one row is added)
    csv_writer.writerow([prices[i].text.strip(), location[i].text.strip(), characteristics[i].div.text.strip(),
                         characteristics[i].div.find_next('div').text.strip(),
                         characteristics[i].div.find_next('div').find_next('div').text.strip()])

csv_file.close()
#
# print(prices_list)
# print(location_list)
# print(sq_mt_list)
# print(bedroom_list)
# print(bathroom_list)
#
house_features = (list(zip(prices_list, location_list, sq_mt_list, bedroom_list, bathroom_list)))

# we can use zip to create a df:

# pd.DataFrame(house_features, columns =["rent_price", "location", "sq_mt", "bedroom_n", "bathroom_n"])

# print("======================")
#
# print("======================")
#
#
#
# for i in range(len(characteristics)): # We can use find_next() to get the info from the next item
#     print(("AREA {})").format(i), (characteristics[i].div.text.strip()))
#     print(("BEDROOM {})").format(i), (characteristics[i].div.find_next('div').text.strip()))
#     print(("BATHROOM {})").format(i), (characteristics[i].div.find_next('div').find_next('div').text.strip()))
#     print(("ITEM NUMBER {})").format(i), (characteristics[i].div.find_next('div').find_next('div').find_next('div').text.strip()))
#     print(("ITEM NUMBER {})").format(i), (characteristics[i].div.find_next('div').find_next('div').find_next('div').find_next('div').text.strip()))
#
# # we could include each of these elements into individual lists
#
#
# print("xxx======================")
#
# bedrooms = html_soup.find_all(attrs={"data-rooms": "true"}) # We can search for specific html attributes by passing a dict.
# # The problem is that not all the houses have this element. the approach above works better. We will at least get area, bedroom and bathroom.
# #  We dont need the last elements (floor and price/m2) and the adds with out one of the 3 first elements we can discard it
#
# for i in range(len(bedrooms)):
#
#     print(("{})").format(i), (bedrooms[i].text.strip()))
#
# also we can use a lambda func to specify a class containing specific info: tag = html.find(lambda tag: tag.name == 'div' and tag['class'] == ['value', 'price', ''])

# Clicking on the "next page" button
#
# try:
#     driver.find_element_by_xpath('.//li[@class="next"]//a').click()
#     # element = driver.find_element_by_class_name('main flex loggedOut lang-es es-ES hollywood wide hasTwoPanes _initOk serpControl')
#     # driver.execute_script("arguments[0].click();", element)
# except NoSuchElementException:
#     print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs,
#                                                                                                  len(jobs)))
#     break
#
# return pd.DataFrame(jobs)  # This line converts the dictionary object into a pandas DataFrame.