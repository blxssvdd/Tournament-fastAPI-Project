# 🏆 Tournament Manager API

[![Версия Python](https://img.shields.io/badge/python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

Учебный проект системы управления турнирами на FastAPI. Разработан в рамках курса по Python.

---

## 🔍 О проекте

Это API для организации киберспортивных турниров, где можно:
- Создавать турниры по разным играм
- Регистрировать участников и команды
- Организовывать матчи между командами

Проект создавался для изучения:
- Современного Python (3.10+)
- Фреймворка FastAPI
- Асинхронного программирования
- Работы с базами данных через SQLAlchemy
- Профессиональной разработки API

---

## 🛠 Технологический стек

### Основные технологии
- **FastAPI** - ядро проекта, обработка запросов
- **SQLAlchemy** - ORM для работы с БД
- **Pydantic** - валидация данных
- **JWT** - аутентификация

### Вспомогательные инструменты
- **Uvicorn** - ASGI-сервер
- **Docker** - контейнеризация (опционально)
- **venv** - виртуальное окружение

---

## 🚀 Запуск проекта

### Требования
- Python 3.10 или новее
- MySQL (можно и SQLite для разработки)
- Docker (опционально)

### Установка
1. Клонируем репозиторий:
```bash
git clone https://github.com/blxssvdd/Tournament-fastAPI-Project.git
cd Tournament-fastAPI-Project
