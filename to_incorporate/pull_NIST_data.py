from lxml import html
import requests
import csv

website = 'https://physics.nist.gov/PhysRefData/Handbook/Tables/*table3.htm'
elements = ['hydrogen','helium','lithium','beryllium','boron','carbon','nitrogen','oxygen','fluorine','neon','sodium','magnesium','aluminum','silicon','phosphorus','sulfur','chlorine','argon','potassium','calcium','scandium','titanium','vanadium','chromium','manganese','iron','cobalt','nickel','copper','zinc','gallium','germanium','arsenic','selenium','bromine','krypton','rubidium','strontium','zirconium','niobium','molybdenum','technetium','ruthenium','rhodium','palladium','silver','cadmium','indium','tin','antimony','tellurium','iodine','xenon','cesium','barium','lanthanum','cerium','praseodymium','neodymium','promethium','samarium','europium','gadolinium','terbium','dysprosium','holmium','erbium','thulium','ytterbium','lutetium','hafnium','tantalum','tungsten','rhenium','osmium','iridium','platinum','gold','mercury','thallium','lead','bismuth','polonium','astatine','radon','francium','radium','actinium','thorium','protactinium','uranium','neptunium','plutonium','americium','curium','berkelium','californium','einsteinium','fermium','mendelevium','nobelium','lawrencium','rutherfordium','dubnium','seaborgium','bohrium','hassium','meitnerium','darmstadtium','roentgenium','copernicium','nihonium','flerovium','moscovium','livermorium','tennessine','oganesson']
website.split('*')

wavelength = {}
intensity  = {}
for element in elements:
    wavelength[element] = []
    intensity[element] = []
    page = requests.get(website.split('*')[0]+element+website.split('*')[1])
    for i in page.text.split('table'):
        if '<a name=' in i:
            try: 
                wavelength[element].append(float(i.split('name=')[1].split('"')[1]))
            except:
                pass
            try:
                intensity[element].append(float(i.split('name=')[1].split('</td>')[0].split('&nbsp;')[-1]))
            except:
                pass

make_csv = False

if make_csv:
    with open('./persistent_lines.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for i in intensity:
            for j,k in zip(intensity[i],wavelength[i]):
                writer.writerow([i,j,k])
