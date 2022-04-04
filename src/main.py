import logging
import uvicorn

from src.config import APP_PRODUCT_HOST, APP_PRODUCT_PORT

if __name__ == "__main__":
    try:
        uvicorn.run("apps.products_app.api:app", host=APP_PRODUCT_HOST, port=APP_PRODUCT_PORT, reload=True)
    except Exception as e:
        error = 'No se puede iniciar el sistema: %s' %e
        print(error)
        logging.error(error)