## Тестовое задание.
### Описание
Тестирование сайта investing.com. Проект реализован на Python с использованием библиотеки selenium.
Возможность проводить тестирование в браузерах Google Chrome(по умолчанию) и  Mozilla Firefox.
Для обоих браузеров реализован headless режим.

### Запуск
Клонируйте репозиторий
```
    https://github.com/AlexKing777111/investing_test
```
Создайте и установите виртуальное окружение
```
    python -m venv venv
```
```
    source venv/Scripts/activate
```
Установите зависимости из файла requirements.txt
```
    pip install -r requirements.txt
```
Для тестирования на Google Chrome скачайте и устанновите браузер(если браузер уже установлен, перейдите к следующему шагу)
```
    По умолчанию тестирование проводится на Google Chrome
```

Для тестирования на Mozilla Firefox скачайте и установите браузер(если браузер уже установлен, перейдите к следующему шагу)
```
    https://www.mozilla.org/ru/firefox/
```
Скачайте geckodriver(выберите версию подходящую под вашу ОС)
```
    https://github.com/mozilla/geckodriver/releases/
```
Если вы планируете проводить тестирование на Mozilla Firefox в пункте executable_path в файле conftest.py укажите путь к файлу geckodriver.exe

![2022-06-03_15-22-04](https://user-images.githubusercontent.com/94525867/171836702-0ccfa3c5-c195-4335-830c-523d35c82c73.png)

Для тестирования на Mozilla Firefox в файле test_investing.py замените chrome_browser на firefox_browser

![2022-06-03_15-37-29](https://user-images.githubusercontent.com/94525867/171838741-6140d273-8d46-410f-b711-99b69cc60aa5.png)
![2022-06-03_15-39-37](https://user-images.githubusercontent.com/94525867/171841025-d710613f-7ba9-4cb7-a493-14c172deb808.png)


Для активации headless режима следуйте комментариям в файле conftest.py
Для Google Chrome разкомментируйте 14 строку (уберите знак # в начале строки).

![2022-06-03_15-42-49](https://user-images.githubusercontent.com/94525867/171839905-5fc5a783-7f74-4525-bb7b-f75af9a3bcb0.png)

Для Mozilla Firefox в файле conftest.py измените firefox_options.headless(строка 31). Значение True активирует режим headless.

![2022-06-03_15-43-31](https://user-images.githubusercontent.com/94525867/171840203-71a6af90-da2f-476e-9fe4-e142caf837c6.png)

Для запуска тестов запустите pytest.
```
    pytest
```
По завершению теста будет сделан скриншот, который будет сохранен под названием TestFullPage.png в папке с программой.

### Автор
Александр Королев

