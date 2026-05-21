# Calculadora de Gorjetas com Divisão de Contas e Log Local

Este é um script em Python desenvolvido para calcular o valor total de uma conta com acréscimo de gorjeta e dividir o resultado igualmente entre um grupo de pessoas. O projeto foca em lógica dinâmica e validação de regras de negócio.

## Diferenciais do código

* **Lógica Dinâmica:** Diferente de estruturas engessadas, o cálculo matemático foi unificado para aceitar qualquer porcentagem de gorjeta informada pelo usuário, tornando o código mais limpo e escalável.
* **Prevenção de Erros Críticos:** Possui validação interna para impedir a divisão da conta por zero ou por números negativos, tratando o cenário antes que gere uma falha no sistema (`ZeroDivisionError`).
* **Tratamento de Exceções e Strings:** Utiliza blocos try/except para capturar entradas de texto inválidas e faz a conversão automática de vírgulas para pontos.
* **Persistência de Dados:** Grava o histórico de cada conta calculada no arquivo local `historico_gorjetas.txt`.

## Tecnologias utilizadas

* Python 3
* Manipulação de arquivos (Built-in)

## Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/Kleverson03/Porcentagem-de-gorjeta.git](https://github.com/Kleverson03/Porcentagem-de-gorjeta.git)