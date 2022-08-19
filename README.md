# Обрезка ссылок с помощью Битли

Это консольная утилита для работы с сервисом bit.ly. Если она получает на вход длинную ссылку, то сокращает её. Если она получает на вход короткую ссылку bitly, то считает количество переходов по ней.

### Как установить

Для работы с утилитой у вас уже должен быть установлен Python 3.

- Скачайте код программы на свой локальный диск.
- Запустите консоль (команда `cmd` в Windows).
- Затем перейдите в папку с программой и используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
cmd {папка_на_локальном_диске}
pip install -r requirements.txt
```

### Переменные окружения

Персональный ключ – “токен” для взаимодействия с API Bitly берётся из переменных окружения. Для определения настроек окружения создайте файл `.env` рядом с `main.py` и запишите туда такие данные: 
```
BITLY_TOKEN={токен}
```
Вместо `{токен}` подставьте значение вашего токена с сервиса bitly. Чтобы получить этот токен, зарегистрируйтесь на сервисе [bitly](https://bit.ly/) и получите токен типа `GENERIC ACCESS TOKEN` на [Генераторе токенов](https://bitly.com/a/oauth_apps). Там вы получите строку наподобие такой: `hg639e20ad155405123dk5677542fecf00231da7`.

### Запуск

Для запуска утилиты наберите в командной строке:
```
python main.py
```
затем введите ссылку в появившемся приглашении ввода и нажмите Enter.

Или можете указать ссылку прямо в командной строке. Тогда вызов программы будет следующим:
```
python main.py {ссылка}
```
где вместо `{ссылка}` подставлено значение вашей ссылки.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).