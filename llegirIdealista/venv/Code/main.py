import json
import csv

delimiter = ";"
lineterminator = '\r'
fileName = 'dataOutput.csv'

def getField(objeto, campo):
    if campo in objeto:
        return (str(objeto[campo]).replace('🏖', ''))
    else:
        return ('')

def getFieldNames() -> object:
    fieldnames = [
        'propertyCode', 'thumbnail', 'externalReference', 'numPhotos', 'floor', 'price', 'propertyType', 'operation',
        'size', 'exterior', 'rooms', 'bathrooms', 'address', 'province', 'municipality', 'district', 'country',
        'latitude', 'longitude', 'showAddress', 'url', 'hasVideo', 'status', 'newDevelopment', 'hasLift'
    ]
    return fieldnames

def createFile(fileName):
    with open(fileName, 'w') as csvfile:
        fieldnames = getFieldNames()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter, quotechar=delimiter, quoting=csv.QUOTE_MINIMAL, lineterminator=lineterminator)
        writer.writeheader()
        return writer

writer = createFile(fileName)
with open(fileName, 'a') as csvfile:
    fieldnames = getFieldNames()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                            lineterminator='\r')
    for documento in range(1,73):
        nomFichero = '../../../PAC2/data/' + str(documento)+ '.json'
        with open(nomFichero, encoding='utf-8') as json_file:
            data = json.load(json_file)
            for p in data['elementList']:
                print(p)
                writer.writerow({
                    'propertyCode' : getField(p, 'propertyCode'),
                    'thumbnail' : getField(p, 'thumbnail'),
                    'externalReference' : getField(p, 'externalReference'),
                    'numPhotos' : getField(p, 'numPhotos'),
                    'floor' : getField(p, 'floor'),
                    'price' : getField(p, 'price'),
                    'propertyType' : getField(p, 'propertyType'),
                    'operation' : getField(p, 'operation'),
                    'size' : getField(p, 'size'),
                    'exterior' : getField(p, 'exterior'),
                    'rooms' : getField(p, 'rooms'),
                    'bathrooms' : getField(p, 'bathrooms'),
                    'address' : getField(p, 'address'),
                    'province' : getField(p, 'province'),
                    'municipality' : getField(p, 'municipality'),
                    'district' : getField(p, 'district'),
                    'country' : getField(p, 'country'),
                    'latitude' : getField(p, 'latitude'),
                    'longitude' : getField(p, 'longitude'),
                    'showAddress' : getField(p, 'showAddress'),
                    'url' : getField(p, 'url'),
                    'hasVideo' : getField(p, 'hasVideo'),
                    'status' : getField(p, 'status'),
                    'newDevelopment' : getField(p, 'newDevelopment'),
                    'hasLift' : getField(p, 'hasLift')
                })