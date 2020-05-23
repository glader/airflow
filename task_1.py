import requests
from collections import Counter
from zipfile import ZipFile
from io import BytesIO
import csv

streets = Counter()

urls = (
    'https://op.mos.ru/EHDWSREST/catalog/export/get?id=781683',
    'https://op.mos.ru/EHDWSREST/catalog/export/get?id=781635',
    'https://op.mos.ru/EHDWSREST/catalog/export/get?id=781643',
    'https://op.mos.ru/EHDWSREST/catalog/export/get?id=781691',
)

for url in urls:
    response = requests.get("https://op.mos.ru/EHDWSREST/catalog/export/get?id=781683")
    input_zip=ZipFile(BytesIO(response.content))
    
    for name in input_zip.namelist():
        data = input_zip.read(name).decode('cp1251')
        reader = csv.reader(data.split('\n'), delimiter=";")
        
        next(reader)
        for line in reader:
            if not line:
                continue

            address = line[4]
            street = '-'
            for n, piece in enumerate(address.split(',')):
                if 'дом' in piece:
                    street = address.split(',')[n-1].strip()

            streets.update([street])
    
print(streets.most_common(6))

# [('-', 32), ('Дмитровское шоссе', 16), ('Чертановская улица', 12), ('шоссе Энтузиастов', 12), ('Волгоградский проспект', 12), ('Кастанаевская улица', 8)]
