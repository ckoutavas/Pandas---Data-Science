# parse xml files

# import objectify
from lxml import objectify

# read xml file
xml = objectify.parse('Document1.xml')

# get root
root = xml.getroot()

# get the chilren of root
data=[]
for i in range(len(root.getchildren())):
    data.append([child.text for child in root.getchildren()[i].getchildren()])

# transpose dataframe
df = pd.DataFrame(data).T
df.columns = ['bathrooms', 'price', 'property_id']
df

# sample data

s = '''<?xml version="1.0" encoding="UTF-8" ?>
<root>
	<bathrooms type="dict">
		<n35237 type="number">1.0</n35237>
		<n32238 type="number">3.0</n32238>
		<n44699 type="number">nan</n44699>
	</bathrooms>
	<price type="dict">
		<n35237 type="number">7020000.0</n35237>
		<n32238 type="number">10000000.0</n32238>
		<n44699 type="number">4128000.0</n44699>
	</price>
	<property_id type="dict">
		<n35237 type="number">35237.0</n35237>
		<n32238 type="number">32238.0</n32238>
		<n44699 type="number">44699.0</n44699>
	</property_id>
</root>'''

# if you dont want all the columns you can use list comprehension:

from lxml import objectify
xml = objectify.parse('Document1.xml')
root = xml.getroot()

bathrooms = [child.text for child in root['bathrooms'].getchildren()]
price = [child.text for child in root['price'].getchildren()]
property_id = [child.text for child in root['property_id'].getchildren()]

data = [bathrooms, price, property_id]
df = pd.DataFrame(data).T
df.columns = ['bathrooms', 'price', 'property_id']
df

