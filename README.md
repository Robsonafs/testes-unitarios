# testes-unitarios
Atividade da disciplina de Testes Unitários realizada pelo aluno: **Robson Antonio França Souza**

## Estrutura do Projeto
- `validador.py`: Contém a lógica principal de validação de formatos.
- `servico_correios.py`: Classe responsável por simular o consumo de uma API externa para CEP.
- `test_validador.py`: Suíte de testes automatizados com `pytest` e `pytest-mock`.
- `.github/workflows/ci.yml`: Configuração do pipeline CI/CD no GitHub Actions.

## Requisitos
- Python 3.8+
- Gerenciador de pacotes `pip`

## Como instalar as dependências
No terminal, execute o seguinte comando na raiz do projeto:

```bash
pip install pytest pytest-mock pytest-cov requests
```

## Para executar os testes direto do terminal, rodar esse comando
```bash
pytest test_validador.py -v
```
## Forçando os tests
