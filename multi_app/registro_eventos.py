import logging

# per poder veure tots el nivell configurem aixi amb el nivell info que es el mes baix:-També ho podem fer a través del numero del valor numeric
logging.basicConfig(level=20)

logging.basicConfig(level=logging.INFO,filename='app.log',filemode='W')
logging.error('Este es un registro de error')
logging.debug('Este es un registro de debug')
logging.info('Este es un registro de info')
logging.warning('Este es un registro de warning')
logging.critical('Este es un registro de critical')

# personalitzem el logging

logger= logging.getLogger('Mi logger personalizado')
logger.setLevel(10)
logger.error('Este es un registro de error')




