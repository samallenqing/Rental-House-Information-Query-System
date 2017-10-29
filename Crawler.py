from bs4 import BeautifulSoup
from urllib2 import urlopen

adId = 0
fhandle = open('RawData.txt','r')
gethandle = open('LosAngeles.txt','a')
for line in fhandle:
    zipCode = line[:5]
    location = line[6:-1]
    url = "https://losangeles.craigslist.org/search/apa?query="+zipCode+"&availabilityMode=0"
    content = urlopen(url)
    data = content.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    totalInfo = soup.find_all('li',{'class':'result-row'})
    for listItem in totalInfo:
        houseURL = listItem.a.get('href')
        description = listItem.p.a.string
        spans = listItem.find_all('span',{'class':'result-meta'})
        for i in spans:
            try:
                arr = i.find('span',{'class':'housing'}).text.split();
                model = arr[0]+arr[2]
                tag = i.find('span',{'class':'result-price'}).text
                price = tag[1:]
            except Exception as e:
                continue
        adId += 1
        adContent = urlopen(houseURL)
        adData = adContent.read().decode('utf-8')
        soup = BeautifulSoup(adData, 'html.parser')
        adInfo = soup.find('div',{'id':'map'})
        if not adInfo:
            continue
        lat = adInfo.get('data-latitude')
        lon = adInfo.get('data-longitude')
        gps = lat + ',' + lon
        s = str(adId)+'?'+zipCode+'?'+location+'?'+price+'?'+model+'?'+houseURL+'?'+description+'?'+gps
        s = s.encode('utf-8')
        gethandle.write(s+'\n')
        print(lat)
        print(lon)
        print(houseURL)
        print(description)
        print(model)
        print(price)
        print(zipCode)

fhandle.close()
gethandle.close()
