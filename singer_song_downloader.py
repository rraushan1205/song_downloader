import bs4
import requests
import webbrowser
a = 0
singernameinput = input('Enter the name of singer : ')
res = requests.get('https://pagalfree.com/singer/' + singernameinput + '.html')
res.raise_for_status()
nonStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
aElems = nonStarchSoup.select('a')
Songs_List = []
ans = ''
i = 15
while ans != 'Ok':
    try:
        Songs_Link = aElems[i].get('href')
        Songs_List.append(Songs_Link)
        i = i + 2
    except:
        ans = 'Ok'
        print("Songs link have been fetched")
new_Lists = []
for i, links in enumerate(Songs_List):
    new_Lists.append(links)
    if i == len(Songs_List) - 9:
        break
    else:
        continue
l = 0
m = 0
for i, items in enumerate(new_Lists):
    req = requests.get(items)
    req.raise_for_status()
    nonStarchSoup1 = bs4.BeautifulSoup(req.text, 'html.parser')
    aElems1 = nonStarchSoup1.select('a')
    Download_Link = aElems1[15].get('href')
    aElems2 = nonStarchSoup1.select('div')[16]
    c = aElems2.getText()
    d = c.strip()
    
    Songname = d.strip(' Song')
    Songname = Songname.split('-')[0]
    print('Downloading....   ' + Songname)
    webbrowser.open_new_tab(Download_Link) #Comment out if ypu want result
    m = m + 1
print('Total Downloaded = ' + str(m))
a = a + m
print(a)
