from rest_framework.viewsets import ViewSet
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Pessoas
import csv
from django.db import transaction


class CSVUploadView(ViewSet):
    parser_classes = [MultiPartParser]

    @transaction.atomic
    def create(self, request, format=None):
        csv_file = request.data['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        for k,row in enumerate(reader):
            if k >0:
                obj, created = Pessoas.objects.get_or_create(
                    nome=row[0],
                    idade=row[1],
                    raiva=row[2],
                )
                if not created:
                    print('objeto já existe, não precisa fazer nada')
                    pass
                else:
                    print(' objeto criado com sucesso')
                    pass
        return Response({'status': 'OK'})
