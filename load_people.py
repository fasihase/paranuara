import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paranuara.settings')
import django
django.setup()

from api import serializers
from rest_framework.parsers import JSONParser
import shutil, json

filename = 'people.json'
currentDir = os.path.dirname(os.path.abspath(__file__))
orgFile = os.path.join(os.path.join(currentDir, 'resources'), filename)
fileToProcess = os.path.join(currentDir, 'tmp.json')
shutil.copyfile(orgFile, fileToProcess)

with open(fileToProcess, 'r') as jsonRead:
    data = json.load(jsonRead)

for row in data:
    temp = row['registered']
    row['registered'] = ''.join(temp.split(' '))

with open(fileToProcess, 'w') as jsonWrite:
    json.dump(data, jsonWrite)

try:
    with open(fileToProcess, 'rb') as people_file:
        data = JSONParser().parse(people_file)
        serializer = serializers.PeopleImportSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            print("Successfully loaded %s" % filename)
        else:
            # print("File format is invalid: %s" % filename)
            print(serializer.errors)
except OSError:
    raise OSError('Cannot open file %s' % filename)

if os.path.isfile(fileToProcess):
    os.remove(fileToProcess)
