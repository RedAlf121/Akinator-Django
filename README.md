# 🧙‍♂️ Akinator-Django

Este proyecto es una implementación de un juego tipo [Akinator](https://akinator.com/) utilizando Django como framework web. El objetivo es adivinar el personaje en el que el usuario está pensando, haciendo preguntas y aprendiendo de los errores para mejorar con el tiempo.

> ⚠️ Este proyecto no llega ni a la mitad del original. La base de datos debe de crecer, así que por el momento se equivocará muchas veces hasta que tenga suficientes datos. Lo importante de este proyecto es entender cómo funciona su algoritmo por detrás. Para entender mejor su funcionamiento vea este [enlace](Akinator.md).

## ✨ Características
- 🎲 Juego interactivo de adivinanza de personajes.
- 💻 Interfaz web moderna y responsiva con Tailwind CSS.
- 📈 Sistema de aprendizaje: el juego mejora cada vez que no adivina correctamente.
- 🌳 Gestión de preguntas y personajes mediante un árbol de decisiones.

## 🗂️ Estructura del Proyecto
- `Akinator/`: Configuración principal de Django.
- `AkinatorTree/`: Lógica del juego, modelos, vistas, formularios y servicios.
- `theme/`: Archivos estáticos por defecto de Tailwind.css.
- `db.sqlite3`: Base de datos SQLite por defecto.

## 📝 Licencia
Este proyecto está bajo la licencia MIT.
