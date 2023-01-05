import requests
from lxml import html

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
URL_MAILRU = 'https://news.mail.ru/politics/'

headers = {
    'User-Agent': user_agent,
}

params = {
    'sso_failed': '',
}


def get_content_dom_from_html_text(url, headers=None, params=None):
    response = requests.get(url, headers=headers, params=params)
    content_dom = html.fromstring(response.text)

    print(response.url)

    return content_dom
    
def parser_mailru(content_dom):
    news_container = content_dom.xpath('//div[contains(@class, "cols__column cols__column_small_23 cols__column_small_23_5 cols__column_medium_32 cols__column_large_39")]')
    mailru_news = []
    for new_container in news_container:
        new_source = new_container.xpath(".//span[@class='newsitem__param']/text()")
        new_text = new_container.xpath(".//span[@class='newsitem__text']/text()")
        new_link = new_container.xpath(".//div/span/a/@href")
        new_date = new_container.xpath(".//div/span/@data-ago_content")
        news_dict = {
            'new_source': new_source,
            'new_text': new_text,
            'new_link': new_link,
            'new_date': new_date,
        }
        mailru_news.append(news_dict)

    return mailru_news

dom = get_content_dom_from_html_text(URL_MAILRU, headers=headers, params=params)
result = parser_mailru(dom)
print(result)
