import sqlite3
import sys
import googletrans
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QTableWidgetItem, QTextEdit, QPushButton, QDialog
from translate import Ui_MainWindow
from question import Ui_Dialog
import speech_recognition as speech_r
import gtts
from playsound import playsound
import os
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt
import icons
import questiondesign
from PyQt5.uic import loadUi
import random
import csv

lang_to_speech = ""

counter_speakings = 0
LANGUAGES_SUPPORTED_TO_SPEAK = (
    'af', 'sq', 'ar', 'hy', 'bn', 'bs', 'ca', 'hr', 'ru', 'cs', 'da', 'es', 'nl', 'en', 'et', 'tl', 'fi', 'fr', 'de',
    'el', 'en-us',
    'gu', 'hi', 'hu', 'is', 'id', 'it', 'ja', 'en-ca', 'jw', 'kn', 'km', 'ko', 'la', 'lv', 'mk', 'ml', 'mr', 'en-in')


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ETool")
        self.textEdit.clear()
        self.add_languages()
        self.pushButton.clicked.connect(self.microphone)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_3.clicked.connect(self.translate)
        self.pushButton_4.clicked.connect(self.speaking_1)
        self.pushButton_5.clicked.connect(self.speaking_2)
        self.pushButton_6.clicked.connect(self.history_clear)
        self.textEdit_2.setReadOnly(True)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.load_data()
        self.history_show()
        self.lineEdit.setPlaceholderText("Search...")
        self.lineEdit.textChanged.connect(self.search)
        self.pushButton_7.clicked.connect(self.open_test)

    def add_languages(self):
        for x in googletrans.LANGUAGES.values():
            self.comboBox.addItem(x.capitalize())
            self.comboBox_2.addItem(x.capitalize())

    def translate(self):
        flag_error = False
        try:
            text_1 = self.textEdit.toPlainText()
            if len(text_1) == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Error')
                msg.setText("Вы ничего не ввели!")
                flag_error = True
                msg.exec_()
            lang_1 = self.comboBox.currentText()
            lang_2 = self.comboBox_2.currentText()

            translator = googletrans.Translator()
            translate = translator.translate(text_1, src=lang_1, dest=lang_2)
            print(translate.text)
            self.textEdit_2.setText(translate.text)
            self.history_save(text_1, translate.text)
            self.history_show()

        except Exception as e:
            if flag_error is False:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Error')
                msg.setText(str(e))
                msg.exec_()
            else:
                pass

    def clear(self):
        try:
            self.textEdit.clear()
            self.textEdit_2.clear()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Error')
            msg.setText(str(e))
            msg.exec_()

    def record_volume(self):
        try:
            recognizer_v = speech_r.Recognizer()
            with speech_r.Microphone(device_index=1) as source:
                audio = recognizer_v.listen(source)

            text_to_enter = self.comboBox.currentText()
            for k, v in googletrans.LANGUAGES.items():
                if v == text_to_enter.lower():
                    language_to_translate = k
                    query = recognizer_v.recognize_google(audio, language=language_to_translate)

                    self.textEdit.setText(query.capitalize())

        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Этот язык не поддерживается голосовым вводом")
            msg.exec_()

    def microphone(self):
        try:
            self.record_volume()

        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Что-то не так с микрофоном")
            msg.exec_()

    def speaking_1(self):
        global LANGUAGES_SUPPORTED_TO_SPEAK
        global lang_to_speech
        try:
            text_to_speech = self.textEdit.toPlainText()
            if text_to_speech:
                lang = self.comboBox.currentText()
                for k, v in googletrans.LANGUAGES.items():
                    if v == lang.lower():
                        lang_to_speech = k
                        break
                speach = gtts.gTTS(text=text_to_speech, lang=lang_to_speech)
                speach.save(f"speach1.mp3")
                playsound(f"speach1.mp3")
                os.remove(f"speach1.mp3")
            else:
                self.textEdit.setText("Вы ничего не ввели!")

        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Кажется, этот язык мы не можем озвучить")
            msg.exec_()

    def speaking_2(self):
        global LANGUAGES_SUPPORTED_TO_SPEAK
        global lang_to_speech
        try:
            text_to_speech = self.textEdit_2.toPlainText()
            if text_to_speech:
                lang = self.comboBox_2.currentText()
                for k, v in googletrans.LANGUAGES.items():
                    if v == lang.lower():
                        lang_to_speech = k
                        break
                speach = gtts.gTTS(text=text_to_speech, lang=lang_to_speech)
                speach.save(f"speach2.mp3")
                playsound(f"speach2.mp3")
                os.remove(f"speach2.mp3")
            else:
                self.textEdit_2.setText("Вы ничего не ввели")

        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Кажется, этот язык мы не можем озвучить")
            msg.exec_()

    def load_data(self):
        try:
            connection = sqlite3.connect("irregulars.sqlite")
            cur = connection.cursor()
            query = "SELECT * FROM irregulars"
            self.tableWidget.setRowCount(173)
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[3]))
                self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[4]))
                tablerow += 1
            connection.close()
        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Кажется, что-то пошло не так")
            msg.exec_()

    def search(self, to_find):
        try:
            self.tableWidget.setCurrentItem(None)
            if not to_find:
                return

            suitable_values = self.tableWidget.findItems(to_find, Qt.MatchContains)
            if suitable_values:
                item = suitable_values[0]
                self.tableWidget.setCurrentItem(item)
        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Не удается осуществить поиск")
            msg.exec_()

    def history_save(self, _from, _to):
        try:
            with sqlite3.connect("history.sqlite") as history:
                cur = history.cursor()
                cur.execute(" INSERT INTO history VALUES (?, ?);", (_from, _to))
                history.commit()
        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Не удалось записать перевод в историю")
            msg.exec_()

    def history_show(self):
        try:
            connection = sqlite3.connect("history.sqlite")
            cur = connection.cursor()
            query = "SELECT * FROM history"
            cur.execute(query)
            self.tableWidget_2.setRowCount(len(cur.fetchall()))
            tablerow = 0
            for row in cur.execute(query):
                self.tableWidget_2.setItem(tablerow, 0, QTableWidgetItem(row[0]))
                self.tableWidget_2.setItem(tablerow, 1, QTableWidgetItem(row[1]))
                tablerow += 1
            connection.close()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Не удалось загрузить историю ваших переводов")
            msg.exec_()

    def history_clear(self):
        try:
            connection = sqlite3.connect("history.sqlite")
            cur = connection.cursor()
            query = "DELETE from history WHERE _from NOT NULL or _from is NULL"
            cur.execute(query)
            connection.commit()
            connection.close()
            self.history_show()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Не удалось удалить историю ваших переводов")
            msg.exec_()

    def open_test(self):
        tested = Question()
        tested.exec_()


counter = 0


class Question(QDialog, Ui_Dialog):
    def __init__(self):
        super(Question, self).__init__()
        self.setupUi(self)
        loadUi('question.ui', self)
        self.setWindowTitle("Test")
        self.download_data()
        global counter
        self.pushButton_2.clicked.connect(self.first_button)
        self.pushButton_3.clicked.connect(self.second_button)
        self.pushButton.setText("Play again")
        self.pushButton_4.setText("Clear score")
        self.pushButton.clicked.connect(self.download_data)
        self.pushButton_4.clicked.connect(self.clear_score)

    def download_data(self):
        data = []
        global counter
        with open("enrusbase.csv", 'r', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for word in reader:
                for v in word.values():
                    data.append(v)
        main_word = random.choice(data)
        self.pushButton_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)
        correct = None
        incorrect = random.choice(data)
        num = data.index(main_word)
        if num % 2 == 0:
            correct = data[num + 1]
        elif num % 2 != 0:
            correct = data[num - 1]
        while data.index(correct) % 2 != data.index(incorrect) % 2:
            incorrect = random.choice(data)
        values = [correct, incorrect]
        first_word = random.choice(values)
        values.remove(first_word)
        second_word = values[0]
        self.correct_first_button = False
        self.correct_second_button = False

        if first_word == correct:
            self.correct_first_button = True
        else:
            self.correct_second_button = True
        self.textEdit_44.setText(f'The right translation for "{main_word}"')
        self.textEdit_2.setText(str(counter))
        self.pushButton_2.setText(first_word)
        self.pushButton_3.setText(second_word)

    def first_button(self):
        global counter
        if self.correct_first_button is True:
            counter += 1
            self.textEdit_2.setText(str(counter))
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(True)

    def second_button(self):
        global counter
        if self.correct_second_button is True:
            counter += 1
            self.textEdit_2.setText(str(counter))
            self.pushButton_2.setDisabled(True)
            self.pushButton_3.setDisabled(True)

    def clear_score(self):
        global counter
        counter = 0
        self.textEdit_2.setText(str(counter))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
