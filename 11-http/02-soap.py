from zeep import Client
import xml.etree.ElementTree as ET
import requests
from http.client import HTTPSConnection

conn = HTTPSConnection("www.dataaccess.com")

payload = '''\
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
      <ubiNum>1000</ubiNum>
    </NumberToWords>
  </soap:Body>
</soap:Envelope>
'''

headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}
conn.request("POST", "/webservicesserver/NumberConversion.wso",
             payload, headers)
res = conn.getresponse()
print(res.read().decode())


response = requests.post(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso", headers=headers, data=payload)
print(response.text)


root = ET.fromstring(response.text)
print(root.find('.//m:NumberToWordsResult',
      {'m': 'http://www.dataaccess.com/webservicesserver/'}).text)
print(root[0][0][0].text)


client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl")
result = client.service.NumberToWords(1000)
print(result)
