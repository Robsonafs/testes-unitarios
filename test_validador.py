import pytest
from validador import Validador

# Fixture para fornecer a instância da classe Validador aos testes
@pytest.fixture
def validador():
    return Validador()

# TESTES DE VALIDAÇÃO DE CEP

@pytest.mark.parametrize("cep_valido", [
    "01001-000", # Com máscara
    "01001000",  # Sem máscara
    "20040-002",
    "20040002"
])
def test_validar_cep_cenarios_positivos(validador, cep_valido):
    assert validador.validar_cep(cep_valido) is True

@pytest.mark.parametrize("cep_invalido", [
    "01001-00",   # Tamanho incorreto (menor)
    "01001-0000", # Tamanho incorreto (maior)
    "0100A-000",  # Letras no meio do formato
    "01001.000",  # Formato/pontuação inválida
    "1234567"     # Faltando dígito na versão sem máscara
])
def test_validar_cep_cenarios_negativos(validador, cep_invalido):
    assert validador.validar_cep(cep_invalido) is False

@pytest.mark.parametrize("cep_excecao", [
    12345678,     # Inteiro (não é string)
    None,         # Tipo NoneType
    ["01001-000"] # Lista
])
def test_validar_cep_excecao_tipo_invalido(validador, cep_excecao):
    with pytest.raises(ValueError):
        validador.validar_cep(cep_excecao)


# TESTES DE VALIDAÇÃO DE CPF

@pytest.mark.parametrize("cpf_valido", [
    "111.444.777-35", # Válido com máscara
    "11144477735",    # Válido sem máscara
    "529.982.247-25",
    "52998224725"
])
def test_validar_cpf_cenarios_positivos(validador, cpf_valido):
    assert validador.validar_cpf(cpf_valido) is True

@pytest.mark.parametrize("cpf_invalido", [
    "111.444.777-36", # Dígito verificador matemático incorreto
    "111.111.111-11", # Regra de números todos iguais
    "111.444.777-3",  # Tamanho incorreto (menor)
    "111.444.777-350",# Tamanho incorreto (maior)
    "111/444/777-35", # Formato de máscara inválido para CPF
    "A11.444.777-35"  # Caracteres não numéricos em posições erradas
])
def test_validar_cpf_cenarios_negativos(validador, cpf_invalido):
    assert validador.validar_cpf(cpf_invalido) is False

@pytest.mark.parametrize("cpf_excecao", [
    11144477735,
    False,
    {"cpf": "111.444.777-35"}
])
def test_validar_cpf_excecao_tipo_invalido(validador, cpf_excecao):
    with pytest.raises(ValueError):
        validador.validar_cpf(cpf_excecao)


# TESTES DE VALIDAÇÃO DE CNPJ

@pytest.mark.parametrize("cnpj_valido", [
    "06.990.590/0001-23", # Válido com máscara (Google Brasil)
    "06990590000123",     # Válido sem máscara
    "00.000.000/0001-91", # Válido com máscara (Banco do Brasil)
    "00000000000191"
])
def test_validar_cnpj_cenarios_positivos(validador, cnpj_valido):
    assert validador.validar_cnpj(cnpj_valido) is True

@pytest.mark.parametrize("cnpj_invalido", [
    "06.990.590/0001-24", # Dígito verificador incorreto
    "00.000.000/0000-00", # Numeração zerada
    "06.990.590/0001-2",  # Tamanho menor
    "06.990.590/0001-230",# Tamanho maior
    "06-990-590/0001.23", # Máscara com pontuação invertida/incorreta
    "06.990.590/000A-23"  # Caracteres inválidos
])
def test_validar_cnpj_cenarios_negativos(validador, cnpj_invalido):
    assert validador.validar_cnpj(cnpj_invalido) is False

@pytest.mark.parametrize("cnpj_excecao", [
    6990590000123,
    True,
    3.14
])
def test_validar_cnpj_excecao_tipo_invalido(validador, cnpj_excecao):
    with pytest.raises(ValueError):
        validador.validar_cnpj(cnpj_excecao)