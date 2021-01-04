from django.test import TestCase
from ..models import Cliente


class ClienteTestCase(TestCase):
    def setUp(self):
        Cliente.objects.create(
            nome="Daniel Arruda de Santana",
            endereco="R. Equador, 686 - Paulista, PE, 53425760",
            telefone="+5581987903112",
            data_nascimento="1994-10-13",
            data_cadastro="2021-01-03 17:12"
        )

    def test_return_srt(self):
        p1 = Cliente.objects.get(nome="Daniel Arruda de Santana")
        self.assertEqual(p1.__str__(), "Daniel Arruda de Santana")

