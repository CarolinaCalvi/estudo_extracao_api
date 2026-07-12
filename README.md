# Estudo de Extracao de API

Este projeto e um estudo simples de consumo de API com Python usando a biblioteca `requests`.

O objetivo do codigo e consultar vagas na API da Gupy, buscando por um termo especifico e tratando a paginacao automaticamente para reunir todos os resultados.

## O que o codigo faz

1. Instala e utiliza a biblioteca `requests`.
2. Faz uma requisicao para a API:
   `https://employability-portal.gupy.io/api/v1/jobs`
3. Busca os dados em formato JSON.
4. Verifica a paginacao retornada pela API, por exemplo:
   `pagination: {"total": 100, "limit": 12, "offset": 0}`
5. Calcula quantas paginas precisam ser consultadas com base em `total / limit`.
6. Arredonda esse valor para cima com `math.ceil`.
   Exemplo:
   `100 / 12 = 8,33`, entao o total de paginas sera `9`.
7. Percorre os offsets de `0` ate `8` para buscar todas as vagas disponiveis.
8. Junta todos os resultados em uma unica estrutura final.

## Como a logica funciona

- `total`: quantidade total de vagas encontradas.
- `limit`: quantidade de registros retornados por pagina.
- `offset`: indice da pagina consultada.

Com isso, o programa descobre quantas paginas existem e faz novas requisicoes ate trazer todos os dados da busca.

## Exemplo do retorno final

O script retorna um dicionario com:

- termo pesquisado (`jobName`)
- total de vagas
- limite por pagina
- quantidade de paginas
- offsets consultados
- lista completa de vagas retornadas pela API

## Requisito

Instale a dependencia antes de executar:

```bash
pip install requests
```
