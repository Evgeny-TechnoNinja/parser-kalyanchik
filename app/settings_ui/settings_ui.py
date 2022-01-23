from typing import Dict, Any

MENU_MAIN_ITEMS = {
    "parse": "Парсить",
    "autoparse": "Автопарсинг",
    "download": "Скачать",
    "link": "Ссылка"
}

DIALOGUE: Dict[str, Any] = {
    "hello_admin": "Дорогой Администратор, я помогу тебе парсить данные с сайта kalyanchik.ua\n",
    "warning_not_admin": "Похоже, что вы не являетесь администратором.\n"
                         "Если это не так, то добавьте ваш ID {} в переменную \"BOT_ADMIN\" в файле конфигурации "
                         "переменных окружения\n",
    "panel": "Предоставляю панель управления парсером\n",
    "parser_notifi": "Дождитесь уведомления о завершении парсинга\n",
    "proxy_data": {
        "sentence": "Не вижу данные о {}\n",
        "proxy": "прокси",
        "login": "логине",
        "password": "пароль"
    },
    "parsing_not_possible": "Парсинг данных невозможен\n",
    "bad_connect": "Прокси вероятно не действительны. Проверьте прокси\n",
}
