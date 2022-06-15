from rest_framework import viewsets, status
from rest_framework.response import Response

from databaseteste.api import serializers
from databaseteste import models

import pandas as pd


class DatabaseViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DatabaseSerializer
    queryset = models.DatabaseTeste.objects.all()
    
    def list(self, request, *args, **kwargs):
        res = super().list(request=request).data
        return Response(res, status=status.HTTP_200_OK)

class DatabaseViewTotalVendas(viewsets.ModelViewSet):
    serializer_class = serializers.DatabaseSerializer
    queryset = models.DatabaseTeste.objects.all()
    
    def list(self, request, *args, **kwargs):
        data = super().list(request=request).data
        df = pd.DataFrame(data)
        df.total_vendas = df.total_vendas.astype(int)
        df = df.groupby('mes_referencia').sum('total_vendas').reset_index().to_dict('records')
        res = {"meses":[], "valores":[]}
        for d in df:
            res['meses'].append(d['mes_referencia'])
            res['valores'].append(d['total_vendas'])
        return Response(res, status=status.HTTP_200_OK)

class DatabaseViewIndicadores(viewsets.ModelViewSet):
    serializer_class = serializers.DatabaseSerializer
    queryset = models.DatabaseTeste.objects.all()
    
    def list(self, request, *args, **kwargs):
        data = super().list(request=request).data
        df = pd.DataFrame(data).reset_index().to_dict('records')
        # df.total_vendas = df.total_vendas.astype(int)
        # df = df.groupby('mes_referencia').sum('total_vendas').reset_index().to_dict('records')
        res = {"Total Vendas":[], "Total de Clientes":[], "Ticket médio por cliente": []}
        for d in df:
            tv = int(d['total_vendas'])
            cc = int(d['contagem_clientes_mes'])
            res['Total Vendas'].append(tv)
            res['Total de Clientes'].append(cc)
            res['Ticket médio por cliente'].append(int(tv/cc))
        return Response(res, status=status.HTTP_200_OK)

class DatabaseViewCategorias(viewsets.ModelViewSet):
    serializer_class = serializers.DatabaseSerializer
    queryset = models.DatabaseTeste.objects.all()
    
    def list(self, request, *args, **kwargs):
        data = super().list(request=request).data
        df = pd.DataFrame(data)
        df1 = df
        df = df.loc[df['tipo_compra']=='Online']
        df.total_vendas = df.total_vendas.astype(int)
        df = df.groupby('mes_referencia').sum('total_vendas').reset_index().to_dict('records')
        res = {"meses":[], "valores":[], "categoria":[]}
        for d in df:
            s1 = 'Online'
            res['meses'].append(d['mes_referencia'])
            res['valores'].append(d['total_vendas'])
            res['categoria'].append(s1)
        df = df1.loc[df1['tipo_compra']=='presencial']
        df.total_vendas = df.total_vendas.astype(int)
        df = df.groupby('mes_referencia').sum('total_vendas').reset_index().to_dict('records')
     
        for d in df:
            s1 = 'presencial'
            res['meses'].append(d['mes_referencia'])
            res['valores'].append(d['total_vendas'])
            res['categoria'].append(s1)

        return Response(res, status=status.HTTP_200_OK)

