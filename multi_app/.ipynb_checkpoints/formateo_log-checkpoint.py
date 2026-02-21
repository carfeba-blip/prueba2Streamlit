import logging

#logging.basicConfig(level=10,format='%(asctime)s:%(name)s:%(message)s:%(threadName)s:%(preocess)s')

logging.debug('Mensaje')

# manejadores 

logger=logging.getLoagger('mi logger personalizado')
logger.setLevel(10)

handler= logging.StreamHandler()
formato=logging.Formatter('%(asctime)s:%(name)s:%(message)s:%(threadName)s:%(preocess)s')
handler.setFormatter(formato)

fhandler=logging.FileHandler(fichero)  # para ficheros
fhandler.setFormatter(formato)

logger.addHandler(handler)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

logger.error('Este es un registro de error')
logger.debug('Este es un registro de debug')
logger.info('Este es un registro de info')
logger.warning('Este es un registro de warning')
logger.critical('Este es un registro de critical')

