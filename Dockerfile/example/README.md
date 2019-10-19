Ejemplo:
===

1. Crea un nuevo directorio para el proyecto.
2. Crea un archivo _main.py_ con el siguiente contenido:
    ```python
    nombre = 'Tu nombre'
    print('¡Yo soy, {}!'.format(name))
    ```
3. Crea un archivo _Dockerfile_ para empaquetar tu aplicación.
4. Usar ```docker build``` para constuir la image.