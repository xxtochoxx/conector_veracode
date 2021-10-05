# Veracode Python 

## Setup

Clone this repository:

    git clone https://github.com/xxtochoxx/conector_veracode

## Install dependencies:

    
    $ mkdir .veracode
    cd conector_veracode
    pip install -r requirements.txt
    $ touch credentials


## Run


    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>


## Identificar microservicio (1)

    pip install veracode-api-signing
    sudo apt-get remove python-pip
    sudo easy_install pip
    sudo apt-get purge httpie
    pip install "PySocks!=1.5.7,>=1.5.6"
    chmod 600 ~/.veracode/credentials

# Generar reporte xml (2)
    
######
!
1)Ejecutar 
    id_gui.py

2)Ejecutar 
    generar_id_build.py

3)Ejecutar
    datos_para_recursos_build.py

4)Completar manualmente 
     Datos: nombre ms, id_bluid en recursos/build_id_veracode.csv

5)Ejecutar
    generar_xml.py (por cada MS)

*cada reporte en formato XML se debe guardar de manera manual en el directorio de nombre "reporte_x_ms"
6)Opcional ejecutar 
    total_microservicios.py
    microservicios-id.py
!
######

by Humberto Melendez