from rest_framework import serializers
from databaseteste import models

class DatabaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.DatabaseTeste
        fields = "__all__"        
    