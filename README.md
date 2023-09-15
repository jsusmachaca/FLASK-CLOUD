# Servidor de almacenamiento en Red con Flask
Proporciona una interfaz intuitiva para sibir cualquier archivo a un dispositivo de almacenamiento físico mediante un servidor.

# Linux

## Instalación y Ejecución
Primero clonar el repo

```sh
git clone https://JsusMachaca/FLASK-CLOUD.git
cd FLASK-CLOUD
```

Instalar entorno virtual
```sh
python -m venv venv
. venv/bin/activate
```

Instalar dependencias

```sh
pip install -r requirements.txt
```

### Ejecución del servidor

Para mostrar información de como ejecutar correctamente el servidor
```sh
python src/app.py --help
```

Almacenamiento por defecto en home
```sh
python src/app.py -d
```

Almacenamiento en dispositivo especifico
```sh
python src/app.py -f /ruta/carpeta
```