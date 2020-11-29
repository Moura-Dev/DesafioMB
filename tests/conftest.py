from app import create_app
import unittest

app = create_app()

class FlaskTeste(unittest.TestCase):

    FEIRA_OBJ = {
        "areap": "3550308005145",
        "bairro": "VL NOVA atualizada",
        "coddist": "60",
        "codsubprefe": "21",
        "distrito": "PENHA",
        "id": "4",
        "lat": "-23520880",
        "logradouro": "RUA FRANCISCO DE OLIVEIRA BRAGA",
        "long_": "-46513450",
        "nome_feira": "VILA NOVA",
        "numero": "13.000000",
        "referencia": "RUA OLIVIA DE OLIVEIRA",
        "regiao5": "Leste",
        "regiao8": "Leste 1",
        "registro": "3048-1",
        "setcens": "355030859000173",
        "subprefe": "PENHA"
    }

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    def test_status_code_get_feira(self):
        tester = app.test_client(self)
        response = tester.get('/feira/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, "application/json")


    def test_content_type_Buscar_feira(self):
        tester = app.test_client(self)
        response = tester.get('/feira/')
        self.assertEqual(response.content_type, "application/json")


    def test_Url_que_nao_existe(self):
        tester = app.test_client(self)
        response = tester.get('/URL_QUE_NAO_EXISTE')
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)


    def test_Post_Criar_feira(self):
        tester = app.test_client(self)
        response = tester.post('/feira/',json=FlaskTeste.FEIRA_OBJ)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, "application/json")


    def test_Atualizar_feira(self):
        id = 4
        tester = app.test_client(self)
        response = tester.put('/feira/{}'.format(id),json=FlaskTeste.FEIRA_OBJ)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_buscar_nova_feira(self):
        nomefeira = "Vila"
        tester = app.test_client(self)
        response = tester.get('/feira/{}'.format(nomefeira))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_deletar_feira(self):
        id = 5
        tester = app.test_client(self)
        response = tester.delete('/feira/{}'.format(id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")






if __name__ == "__main__":
    unittest.main()