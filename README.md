### Описание
Стек - FastAPI, SQLAlchemy, Pydantic, Alembic.
Данный проект соответствует ТЗ.

### Запуск с помощью Docker Compose
1. Перейдите в пустую папку и клонируйте репозиторий
 - ```git clone https://github.com/Stepan1771/ucar.git```
2. Соберите образ
 - ```docker compose build```
3. Запустите
 - ```docker compose up -d```
4. Просмотрите логи
 - ```docker compose logs -f app```
 в логах должна сработать миграция и запуститься приложение по адресу:
 "http://0.0.0.0:8000", если не открывается по этому адресу:
 "http://127.0.0.1:8000", "http://localhost:8000"

### Связь со мной:
- тг: @BonusYou
- резюме: https://hh.ru/resume/02efc04aff0f738fe90039ed1f47356d686a63