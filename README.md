# scrapy_parser_pep

# Проект парсинга pep

Простой парсер статусов PEP для https://peps.python.org.

В папке results создает два csv файла:
- Список PEP вида Номер, Название, Статус - pep_ДатаВремя.csv.
- Количество уникальных статусов, так же подсчитывает общее количество PEP - status_summary_ДатаВремя.csv.

***

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/KapkaDibab/scrapy_parser_pep
```

```bash
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Запустить с логом в терминал:

```bash
scrapy crawl pep
```

Запустить с логом в файл scrapy.log:

```bash
scrapy crawl pep -s LOG_FILE=scrapy.log
```


***

## Tech Stack

+ `Python` : <https://github.com/python>
+ `Scrapy` : <https://github.com/scrapy/scrapy>
    + .css
    + .xpath
    + Pipelines
    + Feeds
    + Items

***

## Авторы

- [@yandex-praktikum](https://github.com/yandex-praktikum)
- [@KapkaDibab](https://github.com/KapkaDibab)
