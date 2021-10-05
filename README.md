# Veracode Python 

## Setup

Clone this repository:

    git clone https://github.com/xxtochoxx/conector_veracode

## Create files:

    
    $ mkdir .veracode
    cd conector_veracode
    $ touch credentials


## Credentials necessary


    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>


## Install dependencies (1)

    pip install -r requirements.txt
    pip install veracode-api-signing
    sudo apt-get remove python-pip
    sudo easy_install pip
    sudo apt-get purge httpie
    pip install "PySocks!=1.5.7,>=1.5.6"
    chmod 600 ~/.veracode/credentials

# Pasos para generar reporte xml (2)
    1)Ejecutar 
        1_generar_app_build.py

    2)Ejecutar
        2_datos_para_recursos_build.py

    3)Completar manualmente 
        Datos: nombre ms, id_bluid en recursos/build_id_veracode.csv

    4)Ejecutar
        3_generar_xml.py (por cada MS) 

    5)Opcional ejecutar 
        total_microservicios.py
        microservicios-id.py
        para conocer el gui por microservicio se debe ejecutar el script id_gui.py


*cada reporte en formato XML se debe guardar de manera manual en el directorio de nombre "reporte_x_ms"


by Humberto Melendez