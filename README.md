MediCore

🏥 Sistema de Gestión para Consultorios y Centros de Salud.

MediCore es una aplicación web en desarrollo orientada a la gestión integral de consultorios médicos, centros de salud y profesionales independientes. El objetivo del proyecto es que exista una aplicación que centralice profesionales, pacientes y turnos. Medicamentos y tratamientos; historias clínicas y operaciones administrativas; en un sistema claro, confiable y escalable.

Este repositorio me permite mostrar un producto real en constante cambio, documentando cada decisión técnica, mostrando buenas prácticas y adaptación a distintos flujos de trabajo.
También me permite incluir personas que colaboraron con el proyecto desde el frontend, el diseño, y los datos, entre otras cosas.

🎯 Objetivos del proyecto:

Digitalizar la gestión de pacientes y profesionales de la salud.
Centralizar información clínica y administrativa.
Ofrecer una base sólida para futuras integraciones (pagos, reportes, APIs externas)
Servir como proyecto portfolio backend / fullstack.

🧱 Stack tecnológico:

Backend
Python 3
FastAPI (arquitectura moderna, rápida y tipada)
PostgreSQL (base de datos relacional)
SQLAlchemy (ORM)
Pydantic (validación de datos)
Infraestructura / Herramientas
Git & GitHub
Entorno virtual (venv)
Variables de entorno (.env)

📂 Estructura del proyecto (simplificada):

medicore/
├── app/
│   ├── main.py
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   └── services/
├── alembic/
├── tests/
├── .env.example
├── requirements.txt
└── README.md


🧠 Decisiones técnicas:

FastAPI fue elegido por su probada performance y la posibilidad de mostrar datos de swagger en pruebas.
PostgreSQL garantiza integridad de datos y escalabilidad. Se busca llegar a definir una separación clara entre modelos, esquemas y rutas para favorecer el  mantenimiento y crecimiento.
Pensado desde el inicio para escalarm+odlos y funcionalidades y trabajar en equipo.

🎨 Diseño y Experiencia de Usuario (UX/UI):

El proyecto MediCore incluye trabajo de diseño realizado en colaboración con diseñadores UX/UI, como parte de un enfoque integral de producto.
Los mockups fueron desarrollados para explorar y validar flujos clave del sistema antes de su implementación técnica, tales como:
Inicio de sesión y registro de usuarios
Solicitud y gestión de turnos médicos
Navegación general del sistema
Estas piezas visuales permiten alinear criterios entre diseño y desarrollo, y funcionan como guía para la construcción del frontend.
📁 Los diseños se encuentran organizados en la carpeta /design/mockups del repositorio.
👥 Colaboración en diseño
El diseño visual y de experiencia de usuario fue realizado por colaboradores externos. La autoría y créditos correspondientes se detallan de forma explícita para reconocer el trabajo del equipo involucrado.

🚀 Estado actual:

🔧 En desarrollo activo

Funcionalidades iniciales:
Autenticación básica
Modelado de usuarios y entidades principales
Conexión estable a base de datos

Próximos pasos:

Gestión de pacientes
Turnos médicos
Roles y permisos
Historial clínico

🛠️ Instalación local (resumen)
git clone https://github.com/tu-usuario/medicore.git
cd medicore
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Configurar variables de entorno:
cp .env.example .env

Ejecutar:
uvicorn app.main:app --reload


🤝 Colaboración:

Este proyecto está abierto a mejoras, sugerencias y aprendizaje colaborativo.


👤 Autor
Fabricio Guiffrey
Backend / Fullstack Developer
LinkedIn: https://www.linkedin.com/in/fabriguiffrey/

Este proyecto forma parte de un proceso de aprendizaje continuo y construcción profesional.

