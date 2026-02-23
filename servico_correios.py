import requests

class ServicoCorreios:
    def valida_cep_api(self, cep):
        """
        Realiza a chamada a uma API externa de CEP.
        """
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
        return "erro" not in dados