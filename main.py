import json
import urllib2

print('Loading function')
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    #searchURL="http://ishank.me/test.html"
    searchURL=event['val1']
    #searchURL=input()
    #print (searchURL)
    page = urllib2.urlopen(searchURL)
    
    soup = BeautifulSoup(page, "html.parser")
    #print(soup)
    table = soup.find("table", { "name" : "grades" })
    #print(table)
    rows = []
    for row in table.find_all("tr"):
        data=[]
        for td in row.find_all("td"):
            if(td):
                entity=td.text
                data.append(entity)
                print (td.text),
        if(data):
            rows.append(data)
        print ("")
    
    #print("value3 = " + event['key3'])
    
    #return event['key1']  # Echo back the first key value
    
    return {
            "body":str(rows),
        # "statusCode": 200,
        # "isBase64Encoded": False
    }
    #raise Exception('Something went wrong')
