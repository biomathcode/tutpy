import bs4, requests

def GetAmazonprice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#buyNewSection > a > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
    return elems[0].text.strip()        





price = GetAmazonprice('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')

print('The price is ' + price)
