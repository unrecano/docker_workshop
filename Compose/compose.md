Docker Compose
===

1. __¿Qué es y para qué sirve?__

Es una herramienta que permite definir y correr aplicaciones multicontenedores. Con compose podemos construir y ejecutar todos los servicios de la aplicación que son especificados en el archivo _docker-compose.yaml_

**Comandos**

- __docker-compose up:__ Levantar los contenedores especificados en el archivo docker-compose.yaml, --build sirve para forzar que la construcción de los contenedores.
- __docker-compose logs -f {service}:__ Mostrar los logs del servicio.
- __docker-compose top:__ Ver las tareas que se están ejecutando en los servicios.
- __docker-compose ps:__ Ver los contenedores o servicios que se están ejecutando.

2. __Sentencias básicas__

- __build:__ Especificar la carpeta de contexto para la construcción de la imagen.
- __command:__ Sobreescribe el commando de ejecución por defecto.
- __depends_on:__ Describe dependencia entre contenedores.
- __environment:__ Agregar variables de entorno
- __image:__ Especificar la imagen desde la cual se inicia el contenedor.
- __ports:__ Exponer puertos.
- __volumes:__ Permite montar volumenes (carpetas).