Feature: Gerenciamento de agendamentos

  Scenario: Adicionar um novo Agendamento
    Given que eu tenho os detalhes do Agendamento
    When eu faço o cadastro de um Agendamento
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Agendamento
    When eu faço a consulta dos agendamentos cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um Agendamento existente
    Given que eu tenho os detalhes atualizados do Agendamento
    When eu faço uma atualização de um Agendamento
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Agendamento por data
    When eu faço a consulta de um Agendamento por data
    Then eu devo receber uma resposta com o código de status 200