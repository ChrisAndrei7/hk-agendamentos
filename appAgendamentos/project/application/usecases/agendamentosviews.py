#from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.agendamentos.agendamentosmodels import Agendamento
from infrastructure.presenters.agendamentosserializers import AgendamentoSerializer

@api_view(['GET'])
def getData(request):
    agendamentos = Agendamento.objects.all()
    serializer = AgendamentoSerializer(agendamentos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAgendamento(request, pk):
    agendamentos = Agendamento.objects.get(id=pk)
    serializer = AgendamentoSerializer(agendamentos, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getAgendamentodata(request, data):
    agendamentos = Agendamento.objects.get(data=data)
    serializer = AgendamentoSerializer(agendamentos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addAgendamento(request):
    serializer = AgendamentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateAgendamento(request, pk):
    agendamento = Agendamento.objects.get(id=pk)
    serializer = AgendamentoSerializer(instance=agendamento, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteAgendamento(request, pk):
    agendamento = Agendamento.objects.get(id=pk)
    agendamento.delete()
    return Response('Agendamento deletado com sucesso!')

