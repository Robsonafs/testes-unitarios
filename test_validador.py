import pytest
import requests
from validador import Validador

# Fixtures

@pytest.fixture
def validador():
    """Fornece uma instância limpa da classe Validador para os testes."""
    return Validador()

# Testes: Validação de CEP (Mockando ServicoCorreios)

@pytest.mark.parametrize("cep_valido", ["01001-000", "01001000"])
def test_validar_cep_sucesso_com_api(validador, mocker, cep_valido):
    # Mock simulando retorno True da API
    mocker.patch.object(validador.servico_correios, 'valida_cep_api', return_value=True)
    assert validador.validar_cep(cep_valido) is True

@pytest.mark.parametrize("cep_invalido_api", ["99999-999"])
def test_validar_cep_falha_rejeitado_pela_api(validador, mocker, cep_invalido_api):
    # Mock simulando retorno False da API
    mocker.patch.object(validador.servico_correios, 'valida_cep_api', return_value=False)
    assert validador.validar_cep(cep_invalido_api) is False

@pytest.mark.parametrize("cep_formato_invalido", ["01001-00", "010010000", "abcde-fgh"])
def test_validar_cep_falha_formato_incorreto(validador, mocker, cep_formato_invalido):
    # A API nem deve ser chamada se o formato falhar na validação primária
    mock_api = mocker.patch.object(validador.servico_correios, 'valida_cep_api')
    assert validador.validar_cep(cep_formato_invalido) is False
    mock_api.assert_not_called()

def test_validar_cep_excecao_erro_http(validador, mocker):
    # Mock simulando erro de conexão HTTPError
    mocker.patch.object(
        validador.servico_correios,
        'valida_cep_api',
        side_effect=requests.exceptions.HTTPError("Erro 500 do servidor")
    )
    with pytest.raises(requests.exceptions.HTTPError):
        validador.validar_cep("01001-000")

def test_validar_cep_excecao_tipo_incorreto(validador):
    # Garante que um número inteiro levante ValueError
    with pytest.raises(ValueError):
        validador.validar_cep(1001000)

# Testes: Validação de CPF

# Usando um CPF matematicamente válido (apenas para fins de teste)
@pytest.mark.parametrize("cpf_valido", ["111.444.777-35", "11144477735"])
def test_validar_cpf_sucesso(validador, cpf_valido):
    assert validador.validar_cpf(cpf_valido) is True

@pytest.mark.parametrize("cpf_invalido", [
    "111.111.111-11", # Dígitos repetidos (rejeitado pela regra)
    "123.456.789-00", # Dígitos verificadores matematicamente incorretos
    "123",            # Tamanho incorreto
    "abcdefghijk",    # Letras
    ""                # Vazio
])
def test_validar_cpf_falha(validador, cpf_invalido):
    assert validador.validar_cpf(cpf_invalido) is False

def test_validar_cpf_excecao_tipo_incorreto(validador):
    with pytest.raises(ValueError):
        validador.validar_cpf(11144477735)

# Testes: Validação de CNPJ

# Usando um CNPJ matematicamente válido (apenas para fins de teste)
@pytest.mark.parametrize("cnpj_valido", ["11.222.333/0001-81", "11222333000181"])
def test_validar_cnpj_sucesso(validador, cnpj_valido):
    assert validador.validar_cnpj(cnpj_valido) is True

@pytest.mark.parametrize("cnpj_invalido", [
    "33.012.339/0001-00", # Dígitos verificadores incorretos
    "00.000.000/0000-00", # Dígitos repetidos
    "123",                # Tamanho incorreto
    "AA.AAA.AAA/AAAA-AA"  # Letras
])
def test_validar_cnpj_falha(validador, cnpj_invalido):
    assert validador.validar_cnpj(cnpj_invalido) is False

def test_validar_cnpj_excecao_tipo_incorreto(validador):
    with pytest.raises(ValueError):
        validador.validar_cnpj(11222333000181)
