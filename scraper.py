from urllib.request import urlopen
from bs4 import BeautifulSoup


class Scraper:

    def search(self, athlete_name):
        name_components = athlete_name.split(' ', 1)
        url = "http://ufcstats.com/statistics/fighters/search?query=" + name_components[0]
        request = urlopen(url)
        request_in_html = request.read()
        request.close()
        html_parsed = BeautifulSoup(request_in_html, 'html.parser')
        testing = html_parsed.find_all('a', class_='b-link b-link_style_black')

        for x in range(len(testing)):
            if testing[x].text == name_components[0] and testing[x + 1].text == name_components[1]:
                return testing[x]['href']
        return None

    def text_scrape(self, url):
        request = urlopen(url)
        request_in_html = request.read()
        request.close()

        html_parsed = BeautifulSoup(request_in_html, 'html.parser')
        record = html_parsed.find('span', class_='b-content__title-record').get_text().replace('\n', '').replace(' ', '').replace('Record:', '')
        info = html_parsed.find_all('li', class_='b-list__box-list-item b-list__box-list-item_type_block')

        stats = []

        for statistic in info:
            stats.append(statistic.get_text().replace('\n', '').replace(' ', '').split(':'))
        stats.append(record)

        return stats

    def image_scrape(self, athlete_name):
        athlete_name = athlete_name.replace(' ', '-')
        url = "https://www.ufc.com/athlete/" + athlete_name
        request = urlopen(url)
        request_in_html = request.read()
        request.close()

        html_parsed = BeautifulSoup(request_in_html, 'html.parser')
        image = html_parsed.find('div', class_="c-bio__image").find('img')

        return image['src']
