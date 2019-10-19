Dockerfile
===

1. __¿Qué es y para qué sirve?__

Es un archivo en el que se declaran las instrucciones necesarias para construir una nueva imagen.

Nos ayuda a crear imágenes personalizadas para nuestros proyectos.

2. __Sentencias básicas__

- __FROM:__ Elegir una imagen base.
- __RUN:__ Correr comandos dentro del contenedor.
- __ADD/COPY:__ Copiar fichero del host al contenedor, add permite agregar urls.
- __ENTRYPOINT/CMD:__ Ejecutar comandos al instanciar el contenedor. _CMD_ también se puede usar como parámetros de _ENTRYPOINT_.
- __ENV:__ Definir variables de entorno.

3. __CONSTRUIR IMAGEN__

```bash
$ docker build -f /path/to/a/Dockerfile . -t username/name_image
```
