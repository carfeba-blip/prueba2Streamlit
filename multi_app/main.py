import streamlit as st
from eda import eda_app
from ml import ml_app
import logging
from memory_profiler import profile

# registro de visitas

logger=logging.getLogger('Registrador de visitas')
logger.setLevel(logging.INFO)
fhandler=logging.FileHandler('actividad.txt')

formato=logging.Formatter('%(asctime)s- %(levelname)s- %(name)s- %(message)s')                          
fhandler.setFormatter(formato)

logger.addHandler(fhandler)

st.set_page_config('App principal')
@profile   # optimizació memoria
def main():
    st.title('Aplicación principal')
    menu= ['Home','EDA','ML','Acerca de']
    opcion= st.sidebar.selectbox('Menú',menu)
    
    if opcion== 'Home':
        st.subheader('Home')
        logger.info('Home')
    elif opcion== 'EDA':
        eda_app()
        logger.info('EDA')
    elif opcion== 'ML':
        ml_app()
        logger.info('ML')
    else:
        st.subheader('Acerca de...')
        logger.info('Acerca de...')
main()