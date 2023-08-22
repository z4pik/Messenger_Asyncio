from aiohttp import web


class PostgresAccessor:
    """Отвечает за подключение к базе данных и отключение после завершения работы"""
    def __init__(self) -> None:
        """Инициализация класса PostgresAccessor.

        Здесь происходит импорт модели "Message" из модуля "app.forum.models",
        а также инициализация переменных self.message для работы с моделью и self.db для хранения соединения с базой данных.
        """
        from app.forum.models import Message

        self.message = Message
        self.db = None

    def setup(self, application: web.Application) -> None:
        """Настройка класса PostgresAccessor для работы с приложением.

        Добавляет методы _on_connect и _on_disconnect в список функций,
        которые будут вызваны при старте и остановке приложения соответственно.
        """
        application.on_startup.append(self._on_connect)
        application.on_cleanup.append(self._on_disconnect)

    async def _on_connect(self, application: web.Application):
        """Подключение к базе данных при старте приложения.

        Получает конфигурацию базы данных из настроек приложения,
        устанавливает соединение с базой данных на основе полученной конфигурации.
        """
        from app.store.database.models import db

        self.config = application["config"]["postgres"]
        await db.set_bind(self.config["database_url"])
        self.db = db

    async def _on_disconnect(self, _) -> None:
        """Отключение от базы данных при остановке приложения.

        При отключении приложения закрывает соединение с базой данных,
        если оно было установлено ранее.
        """
        if self.db is not None:
            await self.db.pop_bind().close()
