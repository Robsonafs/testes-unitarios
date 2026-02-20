import re

class Validador:
    def validar_cep(self, cep):
        if not isinstance(cep, str):
            raise ValueError("O valor fornecido deve ser do tipo texto (str).")

        # Valida o formato exato com máscara (XXXXX-XXX) ou sem máscara (XXXXXXXX)
        if not re.match(r'^\d{5}-?\d{3}$', cep):
            return False

        return True

    def validar_cpf(self, cpf):
        if not isinstance(cpf, str):
            raise ValueError("O valor fornecido deve ser do tipo texto (str).")

        # Valida o formato exato: com máscara (XXX.XXX.XXX-XX) ou sem máscara (11 dígitos)
        if not re.match(r'(^\d{3}\.\d{3}\.\d{3}-\d{2}$)|(^\d{11}$)', cpf):
            return False

        # Remove a máscara para calcular os dígitos
        numeros = re.sub(r'[^0-9]', '', cpf)

        # Rejeita CPFs conhecidos por terem todos os números iguais (ex: 111.111.111-11)
        if len(set(numeros)) == 1:
            return False

        # Cálculo do primeiro dígito verificador
        soma_d1 = sum(int(numeros[i]) * (10 - i) for i in range(9))
        d1 = 11 - (soma_d1 % 11)
        d1 = 0 if d1 >= 10 else d1
        if int(numeros[9]) != d1:
            return False

        # Cálculo do segundo dígito verificador
        soma_d2 = sum(int(numeros[i]) * (11 - i) for i in range(10))
        d2 = 11 - (soma_d2 % 11)
        d2 = 0 if d2 >= 10 else d2
        if int(numeros[10]) != d2:
            return False

        return True

    def validar_cnpj(self, cnpj):
        if not isinstance(cnpj, str):
            raise ValueError("O valor fornecido deve ser do tipo texto (str).")

        # Valida o formato exato: com máscara (XX.XXX.XXX/XXXX-XX) ou sem (14 dígitos)
        if not re.match(r'(^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$)|(^\d{14}$)', cnpj):
            return False

        # Remove a máscara
        numeros = re.sub(r'[^0-9]', '', cnpj)

        # Rejeita CNPJs com todos os números iguais
        if len(set(numeros)) == 1:
            return False

        pesos_d1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos_d2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        # Cálculo do primeiro dígito verificador
        soma_d1 = sum(int(numeros[i]) * pesos_d1[i] for i in range(12))
        d1 = 11 - (soma_d1 % 11)
        d1 = 0 if d1 >= 10 else d1
        if int(numeros[12]) != d1:
            return False

        # Cálculo do segundo dígito verificador
        soma_d2 = sum(int(numeros[i]) * pesos_d2[i] for i in range(13))
        d2 = 11 - (soma_d2 % 11)
        d2 = 0 if d2 >= 10 else d2
        if int(numeros[13]) != d2:
            return False

        return True