from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.agendamentos.agendamentosmodels import Agendamento
from infrastructure.presenters.agendamentosserializers import AgendamentoSerializer
from django.core.mail import send_mail  # Import para envio de e-mails

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
    data = request.data
    data_agendamento = data.get('data')
    hora_agendamento = data.get('horario')
    medico_nome = data.get('nomemedico')
    paciente_nome = data.get('nomepaciente')
    email_destinatario = data.get('email')  # Campo de e-mail

    # Verificação se o horário já está ocupado para o mesmo médico (validando pelo nome)
    conflito = Agendamento.objects.filter(data=data_agendamento, horario=hora_agendamento, nomemedico=medico_nome).exists()

    if conflito:
        return Response({"erro": "Já existe um agendamento para esse médico na mesma data e horário."}, status=400)

    serializer = AgendamentoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        # Envio do e-mail após salvar o agendamento
        send_mail(
            'Health&Med - Nova consulta agendada',
            f'Olá, Dr. {medico_nome}!\nVocê tem uma nova consulta marcada!\nPaciente: {paciente_nome}.\nData e horário: {data_agendamento} às {hora_agendamento}.',
            'no-reply@healthmed.com',  # Remetente
            [email_destinatario],  # Destinatário
            fail_silently=False,
        )

    return Response(serializer.data)

@api_view(['PUT'])
def updateAgendamento(request, pk):
    data = request.data  # Aqui estamos corrigindo para pegar os dados do request

    data_agendamento = data.get('data')
    hora_agendamento = data.get('horario')
    medico_nome = data.get('nomemedico')
    paciente_nome = data.get('nomepaciente')
    email_destinatario = data.get('email')  # Campo de e-mail

    # Verificação se o horário já está ocupado para o mesmo médico (validando pelo nome)
    conflito = Agendamento.objects.filter(data=data_agendamento, horario=hora_agendamento, nomemedico=medico_nome).exists()

    if conflito:
        return Response({"erro": "Já existe um agendamento para esse médico na mesma data e horário."}, status=400)

    agendamento = Agendamento.objects.get(id=pk)
    serializer = AgendamentoSerializer(instance=agendamento, data=data)

    if serializer.is_valid():
        serializer.save()

        # Envio do e-mail após atualizar o agendamento
        send_mail(
            'Health&Med - Atualização de consulta',
            f'Olá, Dr. {medico_nome}!\nVocê tem uma atualização de uma consulta marcada!\nPaciente: {paciente_nome}.\nNova data e horário: {data_agendamento} às {hora_agendamento}.',
            'no-reply@healthmed.com',  # Remetente
            [email_destinatario],  # Destinatário
            fail_silently=False,
        )

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteAgendamento(request, pk):
    agendamento = Agendamento.objects.get(id=pk)
    agendamento.delete()
    return Response('Agendamento deletado com sucesso!')
