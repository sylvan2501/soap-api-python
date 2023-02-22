import requests
import xml.etree.ElementTree as ET

fahrenheit = '71'

url = 'https://www.w3schools.com/xml/tempconvert.asmx'
soap_envelop = f'''
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
      <Fahrenheit>{fahrenheit}</Fahrenheit>
    </FahrenheitToCelsius>
  </soap:Body>
</soap:Envelope>

'''
res = ''
options = {"Content-Type": "text/xml; charset=utf-8"}
response = requests.post(url, data=soap_envelop, headers=options)
root = ET.fromstring(response.text)
for i, element in enumerate(root.iter('*')):
    if i == 3:
        res = element.text

print('Celcius: ', res)
