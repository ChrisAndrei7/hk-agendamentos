from rest_framework import serializers
from entities.agendamentos.agendamentosmodels import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'