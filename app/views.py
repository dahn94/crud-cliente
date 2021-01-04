from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Cliente


class IndexView(ListView):
    models = Cliente
    template_name = 'index.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


class CreateClienteView(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = ['nome', 'endereco', 'telefone', 'data_nascimento']
    success_url = reverse_lazy('index')


class UpdateClienteView(UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = ['nome', 'endereco', 'telefone', 'data_nascimento']
    success_url = reverse_lazy('index')


class DeleteClienteView(DeleteView):
    model = Cliente
    template_name = 'cliente_del.html'
    success_url = reverse_lazy('index')