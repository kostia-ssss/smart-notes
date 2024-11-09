from PyQt5 import QtCore, QtGui, QtWidgets
import json
from style import style

data = {}
note_name = ""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 500)
        MainWindow.setMinimumSize(QtCore.QSize(668, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 651, 401))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName("text")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.list_notes = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.list_notes.setObjectName("list_notes")
        self.verticalLayout.addWidget(self.list_notes)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create_note = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.create_note.setObjectName("create_note")
        self.horizontalLayout_2.addWidget(self.create_note)
        self._ = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self._.setObjectName("_")
        self.horizontalLayout_2.addWidget(self._)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.save_notes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.save_notes.setObjectName("save_notes")
        self.verticalLayout.addWidget(self.save_notes)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.list_tegs = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.list_tegs.setObjectName("list_tegs")
        self.verticalLayout.addWidget(self.list_tegs)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_to_note = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_to_note.setObjectName("add_to_note")
        self.horizontalLayout_3.addWidget(self.add_to_note)
        self.delete_in_note = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_in_note.setObjectName("delete_in_note")
        self.horizontalLayout_3.addWidget(self.delete_in_note)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.search_notes_with_teg = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_notes_with_teg.setObjectName("search_notes_with_teg")
        self.verticalLayout.addWidget(self.search_notes_with_teg)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        app.setStyleSheet(style)
        self.show_notes()
        
        self.list_notes.itemClicked.connect(self.show)
        self.create_note.clicked.connect(self.add)
        self.save_notes.clicked.connect(self.save_note)
        self._.clicked.connect(self.del_note)
        self.add_to_note.clicked.connect(self.add_tegs)
        self.delete_in_note.clicked.connect(self.del_tegs)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Список заміток"))
        self.create_note.setText(_translate("MainWindow", "Створити замітку"))
        self._.setText(_translate("MainWindow", "Видалити замітку"))
        self.save_notes.setText(_translate("MainWindow", "Зберегти замітку"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.add_to_note.setText(_translate("MainWindow", "Додати до замітки"))
        self.delete_in_note.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.search_notes_with_teg.setText(_translate("MainWindow", "Шукати замітки по тегу"))

    def add(self):
        global note_name
        note_name, ok = QtWidgets.QInputDialog.getText(MainWindow, "Додати замітку", "Назва замітки: ")
        print(note_name)
        if ok and note_name != "":
            data[note_name] = {"текст" : "", "теги" : []}
            self.list_notes.addItem(note_name)
        
    def del_note(self):
        if self.list_notes.currentItem():
            t = self.list_notes.currentItem().text()
            del data[t]
            self.list_notes.clear()
            self.textEdit.clear()
            self.list_tegs.clear()
            with open('notes.json' , 'w' , encoding='utf-8') as file:
                for note in data:
                    self.list_notes.addItem(note)
                json.dump(data, file)
    
    def save_note(self):
        global data
        if self.list_notes.currentItem():
            t = self.list_notes.currentItem().text()
            data[t]["текст"] = self.textEdit.toPlainText()
            with open('notes.json' , 'w' , encoding='utf-8') as file:
                json.dump(data, file)
            
    def show_notes(self):
        # отримуємо текст із замітки з виділеною назвою та відображаємо її в полі редагування
        # key = list_notes.selectedItems()[0].text()
        # print(key)
        # field_text.setText(notes[key]["текст"])
        # list_tags.clear()
        # list_tags.addItems(notes[key]["теги"])
        global data
        with open('notes.json' , 'r' , encoding='utf-8') as file:
            data = json.load(file)
        self.list_notes.addItems(data.keys())
    
    def show(self):
        t = self.list_notes.currentItem().text()
        self.textEdit.setText(data[t]["текст"])
        self.list_tegs.clear()
        self.list_tegs.addItems(data[t]["теги"])      
    
    def add_tegs(self):
        if self.list_notes.currentItem():
            teg = self.lineEdit.text()
            if teg and not (teg in data[self.list_notes.currentItem().text()]["теги"]):
                data[self.list_notes.currentItem().text()]["теги"].append(teg)
                self.list_tegs.addItem(teg)
                self.lineEdit.clear()
                with open("notes.json" , "w" , encoding="utf-8") as file:
                    json.dump(data , file , sort_keys=True)
    
    def del_tegs(self):
        if self.list_notes.currentItem() and self.list_tegs.currentItem():
            t = self.list_notes.currentItem().text()
            teg = self.list_tegs.currentItem().text()
            index = data[t]["теги"].index(teg)
            del data[t]["теги"][index]
            self.list_tegs.clear()
            with open('notes.json' , 'w' , encoding='utf-8') as file:
                for teg in data[t]["теги"]:
                    self.list_tegs.addItem(teg)
                json.dump(data , file)
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
