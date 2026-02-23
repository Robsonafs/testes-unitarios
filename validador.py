import re
from servico_correios import ServicoCorreios


class Validador:
    def __init__(self):
        self.servico_correios = ServicoCorreios()

    def _limpar_entrada(self, valor):
        if not isinstance(valor, str):
            raise ValueError("A entrada deve ser uma string.")
        return re.sub(r'[^0-9]', '', valor)

    def _calcular_digito(self, digitos, pesos):
        soma = sum(d * p for d, p in zip(digitos, pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    def validar_cep(self, cep):
        cep_limpo = self._limpar_entrada(cep)

        if len(cep_limpo) != 8:
            return False

        return self.servico_correios.valida_cep_api(cep_limpo)

    def validar_cpf(self, cpf):
        cpf_limpo = self._limpar_entrada(cpf)

        if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
            return False

        digitos = [int(d) for d in cpf_limpo]

        dv1 = self._calcular_digito(digitos[:9], list(range(10, 1, -1)))
        if dv1 != digitos[9]:
            return False

        dv2 = self._calcular_digito(digitos[:10], list(range(11, 1, -1)))
        if dv2 != digitos[10]:
            return False

        return True

    def validar_cnpj(self, cnpj):
        cnpj_limpo = self._limpar_entrada(cnpj)

        if len(cnpj_limpo) != 14 or cnpj_limpo == cnpj_limpo[0] * 14:
            return False

        digitos = [int(d) for d in cnpj_limpo]

        pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        dv1 = self._calcular_digito(digitos[:12], pesos_1)
        if dv1 != digitos[12]:
            return False

        pesos_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        dv2 = self._calcular_digito(digitos[:13], pesos_2)
        if dv2 != digitos[13]:
            return False

        return True
