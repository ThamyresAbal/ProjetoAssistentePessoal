import clima
import informacoes_cpu_memoria
import ultimas_noticias
import web_browser
import web_scrapping


def menu():
    while True:
        print('=' * 35)
        print('        M     E     N     U')
        print('=' * 35)
        opcao = int(input('(1) Últimas Notícias\n'
                          '(2) Clima\n'
                          '(3) Youtube\n'
                          '(4) Informações do CPU\n'
                          '(5) Informações da Memória\n'
                          '(6) Ibovespa\n'
                          '(7) Sair\n'
                          'Opção escolhida: '))
        print('=' * 35)
        if opcao == 1:
            ultimas_noticias.noticias()
        elif opcao == 2:
            clima.informacao_clima()
        elif opcao == 3:
            web_browser.youtube()
        elif opcao == 4:
            informacoes_cpu_memoria.info_cpu()
        elif opcao == 5:
            informacoes_cpu_memoria.info_memoria()
        elif opcao == 6:
            web_scrapping.ibovespa()
        elif opcao == 7:
            break
        else:
            print('Opção inválida! Tente novamente!')


menu()
