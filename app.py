import PySimpleGUI as sg
import cv2
from easyocr import Reader
from PIL import Image
import io
from textblob import TextBlob


def prepare_image(path):
    res = Image.open(path)
    res.thumbnail((400, 400))
    bio = io.BytesIO()
    res.save(bio, format="PNG")
    return bio.getvalue()


def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV
    return "".join([c if ord(c) < 128 or (ord(c) >= 1040 and ord(c) <= 1103) else "" for c in text]).strip()


def text_to_send(text):
    s = ''
    for t in text:
        s += t + '\n'
    return s


def process(path, lang, gpu):
    print('OCR`ing with the following language: {}'.format(lang))
    image = cv2.imread(path)

    reader = Reader([lang], gpu=gpu > 0)
    results = reader.readtext(image)

    all_text = []

    for (bbox, text, prob) in results:
        if lang != 'ru':
            blob = TextBlob(text)
            text = str(blob.translate(from_lang=lang, to='ru'))

        all_text.append(text)

        # unpack the bounding box
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))

        # cleanup the text and draw the box surrounding the text along
        # with the OCR'd text itself
        text = cleanup_text(text)
        cv2.rectangle(image, tl, br, (0, 255, 0), 2)
        if lang != 'ru':
            cv2.putText(image, text, (tl[0], tl[1] - 10),
                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

    # show the output image
    cv2.imwrite('res.png', image)
    result = prepare_image('res.png')
    res_text = text_to_send(all_text)
    return result, res_text


def create_help_window():
    layout_help = [
        [sg.Text('Нажмите на кнопку "Выберите изображение", чтобы перейти к поиску необходимой фотографии.')],
        [sg.Text('Щелкните на выпадающий список, чтобы выбрать язык текста, который необходимо распознать на изображении:\n"ru" - русский;\n"en" - английский;\n"es" - испанский;\n"de" - немецкий;\n"fr" - французский.')],
        [sg.Text('Нажмите на кнопку "Начать" и ожидайте окончания выполнения процесса.')],
        [sg.Button('Закрыть')]
    ]
    return sg.Window('Помощь', layout_help)


sg.theme('sandy beach')

layout = [
    [sg.Text('Пожалуйста, выберите изображение:')],
    [sg.InputText(key='-FILEPATH-'), sg.FileBrowse(button_text='Выбрать файл...',
                                                   file_types=[('JPG Files', '*.jpg'), ('PNG Files', '*.png'), ('JPEG Files', '*.jpeg')])],
    [sg.Text('Пожалуйста, выберите язык текста:')],
    [sg.Combo(['ru', 'en', 'es', 'de', 'fr'],
              key='-COMBO-', default_value='ru')],
    [sg.Multiline(key='-TEXT-', size=(50, 5),
                  default_text='Здесь будет распознанный текст...')],
    [sg.Image(key='-IMAGE-')],
    [sg.Button('Начать'), sg.Button('Выход'), sg.Push(), sg.Button('Помощь')]
]

window = sg.Window('Помощник в путешествии', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Выход':
        break

    if event == 'Начать':
        r, t = process(values['-FILEPATH-'], values['-COMBO-'], -1)
        window['-IMAGE-'].update(data=r)
        window['-TEXT-'].update(t)
        print(t)

    if event == 'Помощь':
        window_help = create_help_window()
        while True:
            event2, values2 = window_help.read()
            if event2 == 'Закрыть' or event2 == sg.WINDOW_CLOSED:
                break
        window_help.close()

window.close()
