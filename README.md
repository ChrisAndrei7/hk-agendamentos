<h1 align="center"> H&MSystem - Sistema para agendamentos de consultas </h1>
Bem-vindo ao Sistema para agendamento de consultas da Health&Med! Este projeto está em desenvolvimento como atividade do hackaton para a FIAP, curso Software Architecture.	
<br/>
<b>Neste repositório, temos o microsserviço de cadastro dos agendamentos</b>
<br/>
:construction: Projeto em construção :construction:
<br/>

# :computer: Endpoint base da aplicação
http://localhost:8003/
<br/>
<br/>

# :hammer: Subida da aplicação
### Subida completa da aplicação via docker:

#### - Subida no docker:
1. Entre no diretório do projeto: `cd appPacientes`
2. Efetue a criação/subida do banco de dados: `docker compose up -d dbPacientes`
3. Efetue a criação da aplicação: `docker compose build`                                                                                                                                                                                                                                                     
      <b>Nota Importante:
      Ao realizar a primeira inicialização, ocasionalmente pode ocorrer o erro "No installed app with label 'pacientes'". Como solução temporária, sugerimos a seguinte abordagem: caso o erro mencionado ocorra na primeira subida, modifique o arquivo "django.sh" na linha       3, substituindo "pacientes" por "application" e efetue novamente o passo 3 antes de seguir para o passo 4.</b>
4. Efetue a subida da aplicação: `docker compose up`
<br/>
  
# :arrow_forward: Uso 
Abaixo, fluxos principais com processo e endpoint desse microsserviço. Para maior detalhe dos campos, temos no projeto(Na pasta appPacientes/Documentos) o arquivo do Postman com a collection estruturando todos as APIs com descrição e valores a serem informados no json.

1 - Criar o cadastro de um paciente: http://localhost:8003/pacientes/create

2 - Consultar pacientes cadastrados: http://localhost:8003/pacientes/

3 - Atualizar cadastro de um paciente: http://localhost:8003/pacientes/update/{id_do_paciente}

4 - Deletar o cadastro de um paciente: http://localhost:8003/pacientes/delete/{id_do_paciente}

# :page_with_curl: Collection
Disponibilizamos uma collection do postman para ajudar na utilização, contendo todas as APIs deste microserviço e com os campos necessários para preenchimento, <b>localizado na pasta appPacientes/Documentos com nome "hk-pacientes.postman_collection".</b>

# :dancer: Padrão Saga - Coreografia
:construction: Em construção :construction:

# :lock: Relatório RIPD
Relatório RIPD gerado se encontra junto com todos os outros documentos do projeto dentro do projeto, na pasta pasta **appPacientes/Documentos**, com nome **H&MSystem - RIPD**.

# :test_tube: Testes
Para executar os testes, localizados dentro da pasta "feature", deve ser processado o comando behave abaixo após aplicação estar no ar.
<br/>
OBS: BDD está dentro do arquivo "pacientes.feature"

#### behave appPacientes/project/features/pacientes.feature

# Evidência dos testes:

![image](https://github.com/user-attachments/assets/533decb2-745e-4e86-a379-a79a9392fad5)
