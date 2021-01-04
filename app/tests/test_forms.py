from django.test import TestCase
from ..forms import ClienteModelForm


class ClienteFormTestCase(TestCase):

    def test_cliente_form_valido(self):
        form = ClienteModelForm(data={
            'nome': "Francisco André",
            'endereco': "R. Equador, 686 - Paulista, PE, 5342-760",
            'telefone': "+5581987903112",
            'data_nascimento': "1994-10-13",
        })
        self.assertTrue(form.is_valid())

    def test_cliente_form_invalido(self):
        form = ClienteModelForm(data={})
        self.assertFalse(form.is_valid())

