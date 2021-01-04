from django.test import RequestFactory, TestCase


class TestIndexClienteView(TestCase):
    def test_my_method(self):
        request = RequestFactory().get('/')
        view = TestIndexClienteView()
        view(request)

        view()


class TestCreateClienteView(TestCase):
    def test_my_method(self):
        request = RequestFactory().get('add')
        view = TestCreateClienteView()
        view(request)

        view()


class TestUpdateClienteView(TestCase):
    def test_my_method(self):
        request = RequestFactory().get('update')
        view = TestUpdateClienteView()
        view(request)

        view()


class TestDeleteClienteView(TestCase):
    def test_my_method(self):
        request = RequestFactory().get('delete')
        view = TestDeleteClienteView()
        view(request)

        view()
