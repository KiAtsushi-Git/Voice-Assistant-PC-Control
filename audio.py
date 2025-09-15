import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer
import pyautogui
import re
import numpy as np
import webbrowser
import os

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    amplified = (np.frombuffer(indata, dtype=np.int16) * 3).clip(-32768, 32767).astype(np.int16)
    q.put(amplified.tobytes())


# ======= Числа словами =======
NUM_WORDS = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
    "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
    "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50,
    "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90,
    "сто": 100, "двести": 200, "триста": 300, "четыреста": 400,
    "пятьсот": 500, "шестьсот": 600, "семьсот": 700, "восемьсот": 800, "девятьсот": 900,
    "тысяча": 1000
}

def words_to_num(text: str) -> int | None:
    words = text.split()
    total = 0
    current = 0
    for word in words:
        if word in NUM_WORDS:
            val = NUM_WORDS[word]
            if val == 1000:
                current = (current if current else 1) * 1000
                total += current
                current = 0
            elif val >= 100:
                current = (current if current else 1) * val
            else:
                current += val
    total += current
    return total if total > 0 else None




# ======= Обработка команд =======
def handle_command(text: str):
    text = text.lower().strip()

    # ищем число
    match = re.search(r"\d+", text)
    steps = int(match.group()) if match else words_to_num(text) or 10
    print("Полученый текст:", text)
    print("Шаги:", steps)
    # ======= Громкость =======
    if any(cmd in text for cmd in ["уменьши громкость", "уменьшиьб громкость", "уменьшай громкость", "сделай тише", "снизь громкость", "потише"]):
        for _ in range(steps // 2):
            pyautogui.press("volumedown")

    elif any(cmd in text for cmd in ["увеличь громкость", "увеличить громкость", "прибавь громкость", "сделай громче", "громче"]):
        for _ in range(steps // 2):
            pyautogui.press("volumeup")

    elif any(cmd in text for cmd in ["выключи звук", "отключи звук", "отключить звук", "без звука", "мьют"]):
        pyautogui.press("volumemute")

    elif any(cmd in text for cmd in ["включи звук", "восстанови звук", "восстановить звук", "звук обратно"]):
        pyautogui.press("volumemute")

    # ======= Медиаклавиши =======
    elif any(cmd in text for cmd in ["пауза", "стоп", "прекрати", "воспроизвести", "воспроизведение", "играй", "играть", "проигрывай", "проиграть", "продолжи", "продолжить", "стопни", "поставь на паузу", "снять с паузы"]):
        pyautogui.press("playpause")

    elif any(cmd in text for cmd in ["следующий", "дальше", "пропусти", "вперед", "вперёд", "следующая", "следующую", "следующее"]):
        pyautogui.press("nexttrack")

    elif any(cmd in text for cmd in ["предыдущий", "назад", "вернись", "вернуться", "предыдущая", "предыдущую", "предыдущее", "прошлый"]):
        pyautogui.press("prevtrack")

    # ======= Браузер и файлы =======
    elif any(cmd in text for cmd in ["открой браузер", "запусти браузер", "интернет"]):
        webbrowser.open("https://www.google.com")

    elif any(cmd in text for cmd in ["открой google", "открой гугл"]):
        webbrowser.open("https://www.google.com")

    elif any(cmd in text for cmd in ["открой yandex", "открой яндекс"]):
        webbrowser.open("https://ya.ru")

    elif any(cmd in text for cmd in ["открой youtube", "открой ютуб"]):
        webbrowser.open("https://www.youtube.com")

    elif any(cmd in text for cmd in ["открой проводник", "открой explorer"]):
        os.startfile("C:\\")  # открывает корень диска C

    elif any(cmd in text for cmd in ["открой документы"]):
        os.startfile(os.path.expanduser("~/Documents"))

    elif any(cmd in text for cmd in ["открой рабочий стол", "desktop"]):
        os.startfile(os.path.expanduser("~/Desktop"))

    else:
        print("Команда не распознана.")

def listen():
    model = Model("model")  # путь к скачанной модели vosk
    rec = KaldiRecognizer(model, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        print("Слушаю...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if result.get("text"):
                    print("Распознано:", result["text"])
                    handle_command(result["text"])


if __name__ == "__main__":
    listen()
