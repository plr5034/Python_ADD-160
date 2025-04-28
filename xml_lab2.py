'''
XML lab 2
Name: Paul Ring 
github link: https://github.com/plr5034/Python_ADD-160/blob/main/xml_lab2.py

Build an XML document containing information about the three vegan products available in the store:

<?xml version="1.0"?>
<shop>
    <category name="Vegan Products">
        <product name="Good Morning Sunshine">
            <type>cereals</type>
            <producer>OpenEDG Testing Service</producer>
            <price>9.90</price>
            <currency>USD</currency>
        </product>
        <product name="Spaghetti Veganietto">
            <type>pasta</type>
            <producer>Programmers Eat Pasta</producer>
            <price>15.49</price>
            <currency>EUR</currency>
        </product>
        <product name="Fantastic Almond Milk">
            <type>beverages</type>
            <producer>Drinks4Coders Inc.</producer>
            <price>19.75</price>
            <currency>USD</currency>
        </product>
    </category>
</shop>

Save the document to the shop.xml file. Use UTF-8 character encoding and don't
forget to add the prolog to the beginning of the file. 

Use the Element class and the SubElement function.

'''
import xml.etree.ElementTree as ET

# Create the root element
shop = ET.Element("shop")
# Create the category element with an attribute
category = ET.SubElement(shop, "category")
category.set("name", "Vegan Products")
# Create the product elements with their sub-elements
product1 = ET.SubElement(category, "product")
product1.set("name", "Good Morning Sunshine")
type1 = ET.SubElement(product1, "type")
type1.text = "cereals"
producer1 = ET.SubElement(product1, "producer")
producer1.text = "OpenEDG Testing Service"
price1 = ET.SubElement(product1, "price")
price1.text = "9.90"
currency1 = ET.SubElement(product1, "currency")
currency1.text = "USD"
product2 = ET.SubElement(category, "product")
product2.set("name", "Spaghetti Veganietto")
type2 = ET.SubElement(product2, "type")
type2.text = "pasta"
producer2 = ET.SubElement(product2, "producer")
producer2.text = "Programmers Eat Pasta"
price2 = ET.SubElement(product2, "price")
price2.text = "15.49"
currency2 = ET.SubElement(product2, "currency")
currency2.text = "EUR"
product3 = ET.SubElement(category, "product")
product3.set("name", "Fantastic Almond Milk")
type3 = ET.SubElement(product3, "type")
type3.text = "beverages"
producer3 = ET.SubElement(product3, "producer")
producer3.text = "Drinks4Coders Inc."
price3 = ET.SubElement(product3, "price")
price3.text = "19.75"
currency3 = ET.SubElement(product3, "currency")
currency3.text = "USD"
# Create the tree and write it to a file
tree = ET.ElementTree(shop)
# Add the XML declaration
tree.write("shop.xml", encoding="utf-8", xml_declaration=True)
# Read and print the XML file to verify its contents
with open("shop.xml", "r", encoding="utf-8") as file:
    xml_content = file.read()
    print(xml_content)
