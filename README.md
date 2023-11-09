# Сервис для подсчета слов с помощью clickhouse 

## Установка проекта

1. Скопируйте репозиторий

```bash
git clone  https://github.com/VrHb/post-words-count.git
```

2. Разверните clickhouse, [инструкция](https://clickhouse.com/docs/en/getting-started/quick-start)

3. Загрузите данные [отсюда](https://www.kaggle.com/datasets/yutkin/corpus-of-russian-news-articles-from-lenta/)

4. Заполните базу по [инструкции](https://clickhouse.com/docs/en/integrations/data-formats/csv-tsv)

5. Запустите сервер

```bash
uvicorn main:app --port 9090 --reload
```

## Пример запроса

```bash
curl -X 'GET' \
  'http://127.0.0.1:9090/getWords'
```
