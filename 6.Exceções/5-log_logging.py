# Logging é uma maneira de manter um histórico da aplicação

import logging 

# Niveis do logging dependendo do impacto na aplicação

# debug - info para devs
# info - informar algo que não é erro
# warning - algo fora do esperado, pode virar erro
# error - ocorreu algum erro
# critical - erro grave

# Por padrão as msgs nivel warning e posteriores são exibidas
# Para habilitar outros niveis de logging até DEBUG
# Depois do DEBUG é a configuração para criar um arquivo de log.
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
logging.debug('Logging nivel debug')
logging.info('Logging nivel info')
logging.warning('Logging nivel warning')
logging.error('Logging nivel error')
logging.critical('Logging nivel critical')
