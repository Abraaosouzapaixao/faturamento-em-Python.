import json

while True:
    try:
        # Leitura dos dados de faturamento a partir de um arquivo json
        faturamento = [1500, 2000, 1200, 0, 1800, 2200, 0, 1900, 2100, 2300, 0, 1700, 1300, 1400, 2000, 2500, 2400, 1900, 2300, 2200, 2100, 2000, 0, 0, 2500, 1800, 2200, 1900, 2000, 2300, 2400]
        with open('faturamento.json', 'w') as f:
            json.dump(faturamento, f)

        # Cálculo do menor valor de faturamento
        menor_faturamento = min(faturamento)

        # Cálculo do maior valor de faturamento
        maior_faturamento = max(faturamento)

        # Cálculo da média mensal desconsiderando dias sem faturamento
        dias_com_faturamento = [f for f in faturamento if f > 0]
        media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

        # Contagem de dias com faturamento acima da média mensal
        dias_acima_da_media = len([f for f in dias_com_faturamento if f > media_mensal])

        # Impressão dos resultados
        print(f'Menor faturamento: R${menor_faturamento:.2f}')
        print(f'Maior faturamento: R${maior_faturamento:.2f}')
        print(f'Número de dias com faturamento acima da média: {dias_acima_da_media}')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    finally:
        # Pergunta ao usuário se deseja executar novamente ou sair
        resposta = input('Deseja executar novamente? (s/n): ')
        if resposta.lower() != 's':
            break
