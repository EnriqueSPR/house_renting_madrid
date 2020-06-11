from bs4 import BeautifulSoup
import requests
import csv

headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
csv_file = open("rent_scrapper.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["rent_price", "location", "sq_mt", "bedroom_n", "bathroom_n"])

for i in range(1,6): # After page 6 at the website there is a change in the html code
    idealista = "https://www.pisos.com/alquiler/pisos-madrid_capital_zona_urbana/{}".format(i)

    source = requests.get(idealista, headers=headers).text

    html_soup = BeautifulSoup(source, 'lxml')

    house_containers = html_soup.find_all('div', class_="information exclusivo")

    prices = html_soup.find_all('div', class_="price")  # We can get the list of all 30 accommodation prices
    location = html_soup.find_all('div', class_="location")
    characteristics = html_soup.find_all('div', class_="characteristics")

    for j in range(len(house_containers)):
        # Lets save it to a csv file(each iteration one row is added)
        csv_writer.writerow([prices[j].text.strip(), location[j].text.strip(), characteristics[j].div.text.strip(),
                             characteristics[j].div.find_next('div').text.strip(),
                             characteristics[j].div.find_next('div').find_next('div').text.strip()])


for i in range(7,101):
    idealista = "https://www.pisos.com/alquiler/pisos-madrid_capital_zona_urbana/{}".format(i)

    source = requests.get(idealista, headers=headers).text

    html_soup = BeautifulSoup(source, 'lxml')

    house_containers = html_soup.find_all('div', class_="information")

    prices = html_soup.find_all('div', class_="price")  # We can get the list of all 30 accomodation prices
    location = html_soup.find_all('div', class_="location")
    characteristics = html_soup.find_all('div', class_="characteristics")

    for j in range(len(house_containers)):
        # Lets save it to a csv file(each iteration one row is added)
        csv_writer.writerow([prices[j].text.strip(), location[j].text.strip(), characteristics[j].div.text.strip(),
                             characteristics[j].div.find_next('div').text.strip(),
                             characteristics[j].div.find_next('div').find_next('div').text.strip()])

csv_file.close()
