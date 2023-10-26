import xml.etree.ElementTree as ET

root = ET.fromstring('''
<data>
  <country name="Italy">
    <rank>42</rank>
    <year>1861</year>
  </country>
</data>
''')

print(root)
print(root[0])
print(root[0][1])
print(root[0][1].text)

ET.dump(root)
print(ET.tostring(root))
print(ET.tostring(root).decode())

tree = ET.parse('countries.xml')
print(tree)
root = tree.getroot()
print(root)

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

for element in root.findall('./country[@name="Liechtenstein"]/neighbor'):
    print(element.attrib['name'])

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'true')

print(root[0][0].text)
print(root[0][0].attrib['updated'])

tree.write('updated_countries.xml')

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)
