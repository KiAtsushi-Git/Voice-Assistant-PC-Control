# 🎤 Voice Assistant PC Control

> 🚀 Голосовой ассистент на Python для управления компьютером: громкость, музыка, браузер, файлы и другое — с помощью **голоса**.

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&style=flat-square)](https://www.python.org/)
[![Vosk](https://img.shields.io/badge/Vosk-0.3.75-green?style=flat-square)](https://alphacephei.com/vosk/)
[![SoundDevice](https://img.shields.io/badge/SoundDevice-0.8.2-yellow?style=flat-square)](https://python-sounddevice.readthedocs.io/)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9.53-red?style=flat-square)](https://pyautogui.readthedocs.io/)
---

## ✨ Возможности

✅ Управление **громкостью** (увеличить, уменьшить, выключить звук, включить звук)  
✅ Управление **медиа** (пауза, воспроизведение, следующий/предыдущий трек)  
✅ Открытие **браузера и сайтов** (Google, YouTube, Яндекс)  
✅ Открытие **папок** (Документы, Рабочий стол, Проводник)  
✅ Поддержка **чисел словами** (например: "уменьши громкость на десять")  
✅ Автоматическое усиление входного звука для дальнего распознавания  

---

## 🖥️ Установка

1. Склонировать репозиторий:
   ```bash
   git clone https://github.com/KiAtsushi-Git/Voice-Assistant-PC-Control.git
   cd Voice-Assistant-PC-Control
   ```

2. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

**3. Скачать и распаковать русскую лёгкую модель Vosk** 👉 [vosk-model-small-ru-0.22](https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip).
После распаковки переименовать папку в `model` при необходимости и положить её в корень проекта. P.S: Другие модель можно найти [тут](https://alphacephei.com/vosk/models).


---

## 🚀 Запуск

```bash
python audio.py
```

После запуска ассистент начнёт слушать 🎧

---

## 🛠 Примеры команд

| Категория    | Команды-примеры                                               |
| ------------ | ------------------------------------------------------------- |
| 🔊 Громкость | "увеличь громкость", "сделай тише", "выключи звук"            |
| 🎵 Музыка    | "пауза", "следующий трек", "предыдущий"                       |
| 🌍 Браузер   | "открой браузер", "открой YouTube", "открой гугл"             |
| 📂 Файлы     | "открой проводник", "открой документы", "открой рабочий стол" |

---


## ‍💻 Автор

| **Name** | Faraday |
|-------------------|---------|
| **Old**          | 16      |
| **Country** | Russian |
| **Nickname** | KiAtsushi |
| **Email** | [kiatsushi@ki.ru.net](mailto:kiatsushi@ki.ru.net) |
| **Telegram** | [@KiAtsushi](https://t.me/KiAtsushi) |
