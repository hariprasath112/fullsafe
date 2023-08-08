def check(gstin):
    import requests
    from bs4 import BeautifulSoup
    global url,inputName,csrfName
    url="https://www.knowyourgst.com/gst-number-search/"
    inputName="gstnum"
    csrfName="csrfmiddlewaretoken"
    client=requests.session()
    global status
    status=""
    client.get(url)
    if(client.get(url).status_code!=200):
        status+="[GET URL Failure]"
    if 'csrftoken' in client.cookies:
        csrftoken = client.cookies['csrftoken']
    else:
        csrftoken = client.cookies['csrf']
    data={inputName:gstin,csrfName:csrftoken}
    r = client.post(url,data=data,headers=dict(Referer=url))
    if (r.content):
        pass
    else:
        status+="[Content retrival failure]"
    try:
        soup=BeautifulSoup(r.text,'html.parser')
        table=soup.find('table',class_="striped highlight questionlist").find_all('tr')
        data=[]
        for tr in table:
            data.append([td.text for td in tr.find_all('td')])
        reqData=[]
        for i in range(len(data)):
                tempList=data[i]
                reqData.append(tempList[1])
        global name,add
        name = str(reqData[0])
        add=str(reqData[6].split(",")[0])
        status="[No Error]"
    except:
        status+="[Parsing Failure]"
def checkstatus():
    global status
    if (status==""):
        status+="[Offline]"
        print(status)
    else:
        print(status)
