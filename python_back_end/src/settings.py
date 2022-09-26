from dotenv import dotenv_values

class Settings:
    temp = dotenv_values("../.env")
    SOLR_HOST: str = temp['SOLR_HOST']
    SOLR_PORT: str = temp['SOLR_PORT']
    SOLR_CORE: str = temp['SOLR_CORE']
    SOLR_URL = f'http://{SOLR_HOST}:{SOLR_PORT}/solr/{SOLR_CORE}/'