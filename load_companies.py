import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paranuara.settings')
import django
django.setup()

from api import serializers
from rest_framework.parsers import JSONParser

file = 'companies.json'
currentDir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(os.path.join(currentDir, 'resources'), file)

try:
    with open(filename, 'rb') as companies_file:
        data = JSONParser().parse(companies_file)
        serializer = serializers.CompaniesSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            print("Successfully loaded %s" % filename)
        else:
            print(serializer.errors)
except OSError:
    raise OSError('Cannot open file %s' % filename)
