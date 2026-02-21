import logging

# per poder veure tots el nivell configurem aixi:-

logging.basicConfig(level=logging.INFO)

logging.error('Este es un registro de error')
logging.debug('Este es un registro de debug')
logging.info('Este es un registro de info')
logging.warning('Este es un registro de warning')
logging.critical('Este es un registro de critical')

