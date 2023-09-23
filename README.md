# AI-traslator
Приложение для распознавания текста на полученном от пользователя изображении (фотографии уличной вывески) и перевода его на русский язык (при необходимости). Выполнено в качестве курсовой работы по дисциплине "Методы искусственного интеллека".
## Стэк использованных инструментов
* язык программирования: **Python**;
* библиотека для написания пользовательского интерфейса: **PySimpleGUI** [1];
* ввод-вывод изображений: **OpenCV** [2];
* распознавание текста на изображении: **EasyOCR** [3];
* машинный перевод распознанного текста на русский: **TextBlob** [4];
* редактор кода: **VS Code**.
## Последовательность шагов работы с приложением
1. Пользователь указывает расположение фотографии, на которой необходимо распознать и перевести текст (программа поддерживает форматы изображений JPG, JPEG и PNG).
2. Пользователь указывает язык текста, который необходимо распознать на данной фотографии (поддерживаемые языки: русский, английский, испанский, немецкий и французский).
3. Если указанный язык – русский, то в текстовом окне появляется распознанный текст, а также отображается фотография с обведенными на ней участками, содержащими этот текст.
4. Если указанный язык не русский, в текстовом окне появляется переведенный текст, а также отображается фотография с обведенными на ней участками, содержащими иностранный текст, и подписями на русском языке рядом.
## Демонстрация работы приложения
Запустив программу, пользователь попадает в основное меню:

![Начальный экран приложения](https://github.com/Ilyaant/AI-translator/assets/21258800/ee7c485c-b539-4565-92fa-1902618a3fe2)

При нажатии на кнопку «Помощь», появляется окно с краткими пояснениями по работе с приложением:

![Окно "Помощь"](https://github.com/Ilyaant/AI-translator/assets/21258800/f4ae775a-02f2-49a1-92ce-0c0ec07a8960)

В раскрывающемся списке основного окна приложения можно выбрать один из пяти доступных для распознавания языков: русский, английский, испанский, немецкий, французский. Русский язык – вариант по умолчанию:

![Выбор языка распознавания текста](https://github.com/Ilyaant/AI-translator/assets/21258800/33d7ce19-6bd8-485d-90f8-7a62acb9636b)

Рассмотрим результат работы приложения для фотографии с текстом на русском языке: укажем путь к файлу, нажмем кнопку «Начать» и получим результат:

![Выбор файла](https://github.com/Ilyaant/AI-translator/assets/21258800/cd4157cb-8f9c-4b2e-b971-b084b5ae31c6)

![Результат работы программы для вывески с русскоязычным текстом](https://github.com/Ilyaant/AI-translator/assets/21258800/af788324-8461-4498-b7e7-c49b619afa2b)

Рассмотрим теперь результат работы приложения для фотографии с текстом на испанском языке: укажем путь к файлу и выберем испанский язык, нажмем кнопку «Начать» и получим результат:

![Выбор файла и испанского языка распознавания](https://github.com/Ilyaant/AI-translator/assets/21258800/a27627ba-5cae-40d7-85cc-2fc0a5e94d9a)

![Результат работы программы для вывески с текстом на испанском языке](https://github.com/Ilyaant/AI-translator/assets/21258800/e9d09471-fbd7-4072-9ba6-891f56b4a400)

Для вывесок на иностранных языках в качестве результата отображается картинка с не только обведенным текстом, но и подписями на русском языке.

## Ссылки на использованные ресурсы
1. PySimpleGUI URL: https://www.pysimplegui.org/en/latest/.
2. Home - OpenCV URL: https://opencv.org/.
3. JaidedAI / EasyOCR: Ready-to-use OCR with 80+ supported languages and all popular writing scripts including Latin, Chinese, Arabic, Devanagari, Cyrillic and etc. // GitHub URL: https://github.com/JaidedAI/EasyOCR.
4. TextBlob: Simplified Text Processing - TextBlob 0.16.0 Documentation URL: https://textblob.readthedocs.io/en/dev/.