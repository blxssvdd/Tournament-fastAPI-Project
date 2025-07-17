# 🏆 Tournament Manager API

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)

Учебный проект системы управления турнирами на FastAPI. Разработан в рамках курса по продвинутому Python.

---

## 🔍 О проекте

Это API для организации киберспортивных турниров, где можно:
- Создавать турниры по разным играм
- Регистрировать участников и команды
- Организовывать матчи между командами
- Отслеживать прогресс турнира

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
- **SQLAlchemy 2.0** - ORM для работы с БД
- **Alembic** - миграции базы данных
- **Pydantic** - валидация данных
- **JWT** - аутентификация

### Вспомогательные инструменты
- **Uvicorn** - ASGI-сервер
- **Poetry** - управление зависимостями
- **Docker** - контейнеризация
- **Pytest** - тестирование

---

## 🚀 Запуск проекта

### Требования
- Python 3.10 или новее
- PostgreSQL (можно и SQLite для разработки)
- Docker (опционально)

### Установка
1. Клонируем репозиторий:
```bash
git clone https://github.com/blxssvdd/Tournament-fastAPI-Project.git
cd Tournament-fastAPI-Project