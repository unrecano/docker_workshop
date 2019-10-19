Docker
===

1. __¿Qué es Docker?__

Docker es una plataforma para construir, compartir y ejecutar aplicaciones.

2. __¿Qué es un contenedor?__

Un contendor es un proceso que es está ejecutando, que vive aislado de nuestro ordenador y de otros contenedores.

3. __¿Qué es una imagen?__

Una imagen contiene todo lo necesario para ejecutar una aplicación (código, binario, dependencias).

4. __Contenedores y Máquinas virtuales__

Un contenedor corre nativamente en linux y comparte el mismo Kernel, mientras que una máquina virtual, instala un sistema operativo invitado sobre el ordenador accediendo virtualmente a los recursos del mismo.

**Comandos**
- __docker run:__ Instancia un nuevo contenedor.
```bash
$ docker run image_name
```
- __docker pull:__ Descarga una imagen alojada en docker hub.
```bash
$ docker pull image_name
```
- __docker push:__ Sube una imagen a una cuenta de docker hub.
```bash
$ docker push username/image_name
```
- __docker images:__ Lista las imagenes descargadas.
```bash
$ docker images
```
- __docker ps:__ Lista los contenedores que están ejecutándose.
```bash
$ docker ps
```
- __docker build:__ Construye imágenes a partir de un Dockerfile.
```bash
$ docker build -f /path/to/a/Dockerfile . -t username/name_image
```
- __docker exec:__ Ejecuta comandos dentro del contenedor.
```bash
$ docker exec {container ID}
```
- __docker stop:__ Detiene la ejecución de un contendor. (No elimina)
```bash
$ docker stop {container ID}
```
- __docker start:__ Inicia un contenedor detenido en el estado en el que se quedó.
```bash
$ docker start {container ID}
```

5. __Docker Hub__

Docker Hub es un repositorio de imágenes, donde se pueden compartir imágenes.