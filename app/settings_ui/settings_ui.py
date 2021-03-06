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
    "bad_connect": "Прокси вероятно недействительны. Проверьте прокси\n",
    "data_received": "Данные с сайта донора получены",
    "data_not_received": "Не удается получить данные с сайта донора",
    "creation_yml": "\nПриступаю к созданию YML документа",
    "ready_yml": "Документ стандарта YML создан",
    "written_file": "\nВ файл записано {} товаров",
    "upload_fail": "\nФайл не удалось загрузить на сервер. Проверьте настройки FTP соединения\n",
    "successful_upload": "Файл отправлен на сервер\n",
    "successful_parsing": "Парсинг успешно завершён",
    "time_notifi": "Установите время парсинга\nВидите время в  24 часовом формате\n{}Время:",
    "time_example": "Пример: 07:00\n",
    "wrong_time_format": "Вы указали время в неправильном формате\nВремя не установлено\n"
                         "Укажите время в правильном формате\n",
    "autoparse_fail": "Автопарсинг не выполнен\n",
    "document_yml_fail": "Не могу создать документ стандарта YML\n",
    "autoparse_time_set": "Время автопарсинга установлено успешно",
    "autoparse_ready": "Автопарсинг выполнен успешно\n",
    "ftp_fail": "Не могу подключиться к FTP серверу",
    "download_fail": "Не могу предоставить файл. Убедитесь что файл существует.",
    "download_file": "Получите ваш файл",
    "file_info": "Последние изменения файла: {}\n",
    "hot_link": "Ваша горячая ссылка: {}",
}
