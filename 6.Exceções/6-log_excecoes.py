# Como manter um log de exceções da aplicação

import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(message)s - %(asctime)s' )
                    # Nivel              # arquivo criado     # escrita     # formatação              # mensagem     # hora 

try:
    email = input('Digite seu e-mail')
    senha = int(input('Digite seua senha'))
    if senha == 1234:
        print('Login feito com sucesso!')
        logging.info(f'{email} entrou em sua conta bancária')
except ValueError as error:
    print('Digite apenas numeros')
    logging.info(error)