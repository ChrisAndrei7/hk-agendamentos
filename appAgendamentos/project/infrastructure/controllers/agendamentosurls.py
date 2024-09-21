from django.urls import path
from application.usecases import agendamentosviews

urlpatterns = [
    path('', agendamentosviews.getData),
    path ('create', agendamentosviews.addAgendamento),
    path ('read/<str:pk>', agendamentosviews.getAgendamento),
    path ('readdata/<str:data>', agendamentosviews.getAgendamentodata),
    path ('update/<str:pk>', agendamentosviews.updateAgendamento),
    path ('delete/<str:pk>', agendamentosviews.deleteAgendamento),
]
