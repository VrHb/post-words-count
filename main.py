import clickhouse_connect

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from loguru import logger


app = FastAPI()

client = clickhouse_connect.get_client(
    host='localhost',
    username='default',
)

client.command(
    """
    CREATE TABLE IF NOT EXISTS lenta_posts 
        (url String, title String, text String, topic String, tags String, date Date)
    ENGINE = MergeTree() 
    ORDER BY title
    """
)


@app.get('/')
def show_index():
    return {'name_service': 'count_post_words'}


@app.get('/getWords')
def count_words():
    result = client.query(
        """
            SELECT
            arrayJoin(splitByChar(' ', replaceRegexpAll(text, '[.,]', ' '))) AS w,
            count()
        FROM
        (
            SELECT text
            FROM lenta_posts
        )
        GROUP BY w
        ORDER BY count() DESC
        """
    )
    json_data = jsonable_encoder(result.result_set)
    logger.info(json_data)
    return JSONResponse(content=json_data)  
