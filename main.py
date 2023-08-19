from aiohttp import web
import jinja2
import aiohttp_jinja2


def setup_routes(application):
    """Настройка url-путей для всего приложения"""
    from app.forum.routes import setup_routes as setup_forum_routes
    setup_forum_routes(application)


def setup_external_libraries(application: web.Application) -> None:
    """Указываем шаблонизатру, что искать html-шаблоны надо в папке templates"""
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))


def setup_app(application):
    """Настройка всего приложения"""
    setup_external_libraries(application)  # Настройка внешних библиотек
    setup_routes(application)  # Настройка раутера приложения


app = web.Application()  # Создаём наш веб-сервер

if __name__ == "__main__":
    setup_app(app)
    web.run_app(app)
