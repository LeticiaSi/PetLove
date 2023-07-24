# Análise de Churn e Métricas de Clientes

Este é um script em Python que realiza uma análise de churn e calcula algumas métricas relacionadas aos clientes da PetLove. O código utiliza a biblioteca pandas para manipulação e análise dos dados.

## Funcionalidades do Código

O código realiza as seguintes tarefas:

1. **Carregamento e Limpeza dos Dados**: Carrega um arquivo CSV contendo os dados dos clientes da empresa e realiza algumas etapas de limpeza e pré-processamento, como a conversão das colunas de data para o formato correto e a remoção de registros duplicados.

2. **Análise do Churn**: Calcula a taxa de churn, que representa a porcentagem de clientes que cancelaram suas assinaturas em relação ao total de clientes ativos, pausados e cancelados.

3. **Churn por Estado**: Analisa o churn por estado, ou seja, a quantidade de assinantes cancelados em cada estado, e calcula o percentual de churn em relação ao total de assinantes por estado.

4. **Métricas de Receita e Pedidos**: Calcula a média de gastos por pedido de todos os assinantes, o total de receita gerada por todos os pedidos realizados e o número total de pedidos realizados por todos os assinantes.

5. **Média de Itens na Assinatura**: Calcula a média de itens na assinatura de todos os assinantes.

6. **Distribuição Geográfica**: Analisa a distribuição geográfica dos assinantes, contando a quantidade de assinantes em cada cidade e estado.

7. **Canal de Marketing**: Analisa os canais de marketing que trouxeram mais clientes, contando a quantidade de assinantes originados de cada canal.

8. **Média de Idade dos Clientes**: Calcula a média de idade dos clientes com base na data de nascimento fornecida nos dados.

9. **Média de Recência da Última Compra**: Calcula a média da recência da última compra dos clientes, ou seja, o tempo médio que passou desde a última compra.

10. **Média de Tempo até o Cancelamento**: Calcula a média do tempo que os assinantes levaram para cancelar suas assinaturas após a criação.

## Utilização

Para utilizar o código, você precisa ter o Python e a biblioteca pandas instalados em seu ambiente de desenvolvimento. Além disso, certifique-se de ter um arquivo CSV contendo os dados dos clientes no caminho especificado no código.

Após executar o script, ele processará os dados e imprimirá as seguintes informações:

- Taxa de Churn: porcentagem de clientes que cancelaram suas assinaturas em relação ao total de clientes ativos, pausados e cancelados.
- Média de Gastos por Pedido: média de gastos por pedido de todos os assinantes.
- Total de Receita: total de receita gerada por todos os pedidos realizados.
- Total de Pedidos Realizados: número total de pedidos realizados por todos os assinantes.
- Média de Itens na Assinatura: média de itens na assinatura de todos os assinantes.
- Distribuição Geográfica (Estados): quantidade de assinantes em cada estado.
- Churn por Estado: quantidade de assinantes cancelados em cada estado e o percentual de churn por estado.
- Canal de Marketing: quantidade de assinantes originados de cada canal de marketing.
- Média de Idade dos Clientes: média de idade dos clientes com base na data de nascimento.
- Média de Recência da Última Compra: média da recência da última compra dos clientes.
- Média de Tempo até o Cancelamento: média do tempo que os assinantes levaram para cancelar suas assinaturas após a criação.
