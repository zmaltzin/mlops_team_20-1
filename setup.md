# Instrucciones para Generar el Ambiente

## Creación de ambiente virtual de python (venv)
Primero, se requiere una instalación de Python 3.10. Favor dirigirse a la página oficial para obtener instrucciones de instalación:
`https://www.python.org/downloads/release/python-3100/`

Posteriormente, se debe correr el siguiente código desde una terminal:

```bash
python3.10 -m venv mlops_tme_venv
```

Para dispositivos Windows, el código para activar el ambiente es el siguiente:
```bash
mlops_tme_venv\Scripts\activate
```

En cambio, este es el código para MacOS y Linux:
```bash
source mlops_tme_venv/bin/activate
```

Finalmente, este código permite instalar las dependencias de python:
```bash
pip install -r requirements.txt
```


## Levantamiento de Contenedores de Docker

Para levantar los contenedores de docker, basta simplemente con navegar a la carpeta de `/docker`.
```bash
cd docker
```
Y luego correr el siguiente comando:
```bash
docker-compose up --build -d
```
*Nota*: Esto asume que ya se cuenta con el archivo `.env` en la carpeta de `/docker`.


## Configuración de DVC

DVC ya se encuentra configurado para manejar las versiones de los archivos dentro de la carpeta `data`. Sin embargo, es importante ejecutar este comando cada vez que se haga
un cambio a algún archivo de la carpeta, utilizando este comando:

```bash
dvc add data
```