import aiohttp_jinja2


@aiohttp_jinja2.template("index.html")
async def index(request):
    return {'title': 'Пишем первое приложение на aiohttp'}
