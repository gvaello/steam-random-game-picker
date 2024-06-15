# Random Steam Game Selector

Este proyecto utiliza Flask para seleccionar aleatoriamente un juego de Steam basado en los juegos que posee un usuario, las horas jugadas mínimas y los géneros seleccionados.

## Descripción

El Random Steam Game Selector es una aplicación web que permite a los usuarios ingresar su nombre de usuario de Steam, establecer un número mínimo de horas jugadas y seleccionar géneros específicos de juegos. Luego, la aplicación selecciona aleatoriamente un juego que cumpla con estos criterios y muestra información relevante sobre él.

## Funcionalidades

- **Ingreso de Usuario**: Permite a los usuarios ingresar su nombre de usuario de Steam.
- **Filtro por Horas Jugadas**: Los usuarios pueden establecer un mínimo de horas jugadas para filtrar los juegos.
- **Selección de Géneros**: Los usuarios pueden seleccionar uno o más géneros de juegos para restringir la selección.
- **Selección Aleatoria**: La aplicación selecciona aleatoriamente un juego que cumpla con los criterios especificados.
- **Visualización de Información**: Muestra información detallada del juego seleccionado, incluyendo nombre, imagen y horas jugadas.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/random-steam-game-selector.git

    Instala las dependencias necesarias:

    bash

pip install -r requirements.txt

Configura el archivo .env con tu clave de API de Steam:

makefile

    API_KEY=TU_API_KEY_DE_STEAM

Uso

    Ejecuta la aplicación Flask:
    bash
    python main.py

    Abre tu navegador web y ve a http://localhost:5000 para acceder a la aplicación.

    Ingresa tu nombre de usuario de Steam, establece el mínimo de horas jugadas.

    Haz clic en el botón "Get Random Game" para obtener un juego aleatorio que cumpla con tus criterios.

Dependencias

    Flask
    requests
    python-dotenv

Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor crea un fork del repositorio, realiza tus cambios y envía un pull request.
Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

Este README está diseñado para proporcionar toda la información necesaria sobre el proyecto, incluyendo cómo instalarlo, configurarlo, usarlo y contribuir a él. Asegúrate de reemplazar `TU_API_KEY_DE_STEAM` en el archivo `.env` con tu propia clave de API de Steam antes de ejecutar la aplicación.
