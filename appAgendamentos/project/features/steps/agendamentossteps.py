from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8002'

@given('que eu tenho os detalhes do Agendamento')
def step_impl(context):
    context.Agendamento_data = {
        'nomemedico': 'Jose Silverino',
        'nomepaciente': 'Joao da Silva',
        'data': '01-01-2025',
        'horario': '13:00',
    }

@given('que eu tenho os detalhes atualizados do Agendamento')
def step_impl(context):
    context.updated_Agendamento_data = {
        'nomemedico': 'Jose Silverino',
        'nomepaciente': 'Joao da Silva',
        'data': '02-01-2025',
        'horario': '14:00',
    }

@when('eu faço o cadastro de um Agendamento')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/agendamentos/create", json=context.Agendamento_data)

@when('eu faço uma atualização de um Agendamento')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/agendamentos/update/1", json=context.updated_Agendamento_data)

@when('eu faço a consulta dos Agendamentos cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/agendamentos")

@when('eu faço a consulta de um Agendamento por data')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/agendamentos/readdata/02-01-2025")

@when('eu faço a exclusão de um Agendamento')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/agendamentos/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
