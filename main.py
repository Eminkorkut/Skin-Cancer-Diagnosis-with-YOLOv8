from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import glob
import sys
import os

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setWindowTitle("Skin Cancer Detection with Deep Learning Models")

        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setSpread(QGradient.PadSpread)
        gradient.setColorAt(0.0, QColor(22, 88, 167, 255))
        gradient.setColorAt(1.0, QColor(0, 46, 112, 255))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        app_icon = QIcon("icon/icon.png")
        app.setWindowIcon(app_icon)

        self.resize(1000, 550)
        self.setMaximumSize(1000, 550)
        self.setMinimumSize(1000, 550)   
        self.img_lbl = QLabel(self)
        self.img_lbl.setGeometry(30, 60, 475, 475)   
        self.img_lbl.resize(600, 450) 
        self.img_lbl.setStyleSheet("border: 2px solid white; border-radius: 10px;") 

        # Kanser Tablosu
        self.kanserTablosu = QTableWidget(self)
        self.kanserTablosu.setGeometry(680, 320, 270, 150)
        self.kanserTablosu.setColumnCount(2)
        self.kanserTablosu.setRowCount(3)
        self.kanserTablosu.setHorizontalHeaderLabels(["Cancer Type", "Ratio"])
        self.kanserTablosu.verticalHeader().setVisible(False)
        self.kanserTablosu.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.kanserTablosu.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.kanserTablosu.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)

        self.kanserTablosu.setStyleSheet('''
        QTableWidget {
            border: 1px solid #ccc;
            background-color: transparent;
        }
        QTableWidget QHeaderView::section {
            background-color: #dcdcdc;
            color: #333;
            padding: 4px;
        }
        QTableWidget QTableWidgetItem {
            color: #333;
            font: 12px "Times New Roman";
            padding: 6px;
            border: 1px solid #ccc;
        }
        ''')

        # Melanoma
        self.melanomaItem = QTableWidgetItem("Melanoma")
        self.melanomaItem.setTextAlignment(Qt.AlignLeft)
        self.melanomaItem.setFlags(Qt.ItemIsEnabled)
        self.kanserTablosu.setItem(0, 0, self.melanomaItem)

        self.melanomaOranItem = QTableWidgetItem("Ratio: 0.00")
        self.melanomaOranItem.setTextAlignment(Qt.AlignLeft)
        self.melanomaOranItem.setFlags(Qt.ItemIsEnabled)
        self.kanserTablosu.setItem(0, 1, self.melanomaOranItem)

        # Basel
        self.basalItem = QTableWidgetItem("Basel")
        self.basalItem.setTextAlignment(Qt.AlignLeft)
        self.basalItem.setFlags(Qt.ItemIsEnabled)
        self.kanserTablosu.setItem(1, 0, self.basalItem)

        self.basalOranItem = QTableWidgetItem("Ratio: 0.00")
        self.basalOranItem.setTextAlignment(Qt.AlignLeft)
        self.basalOranItem.setFlags(Qt.ItemIsEnabled)
        self.kanserTablosu.setItem(1, 1, self.basalOranItem)

        # Dermatofibroma
        self.dermatofibromaItem = QTableWidgetItem("Dermatofibroma")
        self.dermatofibromaItem.setTextAlignment(Qt.AlignLeft)
        self.dermatofibromaItem.setFlags(Qt.ItemIsEnabled)
        self.kanserTablosu.setItem(2, 0, self.dermatofibromaItem)

        self.dermatofibromaOranItem = QTableWidgetItem("Ratio: 0.00")
        self.dermatofibromaOranItem.setTextAlignment(Qt.AlignLeft)
        self.dermatofibromaOranItem.setFlags(Qt.ItemIsEnabled)
        self.kanserTablosu.setItem(2, 1, self.dermatofibromaOranItem)

        # Doğruluk Oranlarına Göre Sıralama
        def sort_rows_by_accuracy(table_widget):
            row_count = table_widget.rowCount()

            # Satırları doğruluk oranına göre sıralama
            for i in range(row_count - 1):
                for j in range(i + 1, row_count):
                    item1 = table_widget.item(i, 1)  # İlgili satırın doğruluk oranı hücresini al
                    item2 = table_widget.item(j, 1)  # İlgili satırın doğruluk oranı hücresini al

                    if item1 is not None and item2 is not None:
                        accuracy1 = float(item1.text())
                        accuracy2 = float(item2.text())

                        if accuracy2 > accuracy1:
                            for column in range(table_widget.columnCount()):
                                item = table_widget.takeItem(i, column)
                                table_widget.setItem(i, column, table_widget.takeItem(j, column))
                                table_widget.setItem(j, column, item)

        def dialog(): 

            sliderValue = self.eventSlider.value()

            detectBasalText = ""
            detectBasalConf = 0.00

            detectDermatofibromaText = ""
            detectDermatofibromaConf = 0.00

            detectMelanomaText = ""
            detectMelanomaConf = 0.00

            maxConf = 0

            number = self.patient_id.text()

            confList = []
            
            try :
                if (sliderValue == 0):
                    if (len(number) == 11 and int(number)):                        
                        file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()","Image files (*.jpg *.jpeg *.png)")
                        if check:
                            print(file)
                            for a in range(0,3):
                                if (a == 0):
                                    os.system("python3 detect.py --weights {0} --source {1} --patientNumber {2} --skinType {3}".format("Models/basal.pt", file, number, "Basal"))
                                if(a == 1):
                                    os.system("python3 detect.py --weights {0} --source {1} --patientNumber {2} --skinType {3}".format("Models/dermatofibroma.pt", file, number, "Dermatofibroma"))  
                                if(a == 2):
                                    os.system("python3 detect.py --weights {0} --source {1} --patientNumber {2} --skinType {3}".format("Models/melanoma.pt", file, number, "Melanoma"))       
                    else :
                        QMessageBox.about(self, "Error!", "Please enter your Turkish ID number with 11 digits.")                                                           

                
                if os.path.exists(f'Logs/{number}/Basal/'):
                    # Basel # 
                    os.chdir(f'Logs/{number}/Basal/')
                    
                    for file in glob.glob("*.txt"):
                        txt_file = open(file, "r")
                        detectBasalText = txt_file.read()  
                        #self.basalLabel.setText(detectBasalText)                               
                        txt_file.close()
                    os.chdir("../../..")
                    detectBasalConf = float(detectBasalText.split(":")[2].strip())  
                    self.basalOranItem.setText(str(detectBasalConf))
                    confList.append(detectBasalConf)
                else :
                    self.basalOranItem.setText("0.00")
                    #self.basalLabel.setText("Kanser Türü: Basal, Doğruluk Oranı: 0.00")

                if os.path.exists(f'Logs/{number}/Dermatofibroma/'):
                    # Dermatofibroma #
                    os.chdir(f'Logs/{number}/Dermatofibroma/')

                    for file in glob.glob("*.txt"):
                        txt_file = open(file, "r")
                        detectDermatofibromaText = txt_file.read()
                        #self.dermatofibromaLabel.setText(detectDermatofibromaText)
                        txt_file.close()
                    os.chdir("../../..")
                    detectDermatofibromaConf = float(detectDermatofibromaText.split(":")[2].strip())
                    self.dermatofibromaOranItem.setText(str(detectDermatofibromaConf))
                    confList.append(detectDermatofibromaConf)
                else :
                    self.dermatofibromaOranItem.setText("0.00")
                    #self.dermatofibromaLabel.setText("Kanser Türü: Dermatofibroma, Doğruluk Oranı: 0.00")
                
                if os.path.exists(f'Logs/{number}/Melanoma/'):
                    # Dermatofibroma #
                    os.chdir(f'Logs/{number}/Melanoma/')

                    for file in glob.glob("*.txt"):
                        txt_file = open(file, "r")
                        detectMelanomaText = txt_file.read()
                        #self.melanomaLabel.setText(detectMelanomaText)
                        txt_file.close()
                    os.chdir("../../..")
                    detectMelanomaConf = float(detectMelanomaText.split(":")[2].strip())
                    self.melanomaOranItem.setText(str(detectMelanomaConf))
                    confList.append(detectMelanomaConf)
                else :
                    self.melanomaOranItem.setText("0.00")
                    #self.melanomaLabel.setText("Kanser Türü: Melanoma, Doğruluk Oranı: 0.00")

                if (len(confList) > 0):
                    maxConf = max(confList)
                else :
                    maxConf = 0

                def maxConfImageChange(maxiConf):
                    os.chdir(f"Logs/{number}")
        
                    if (maxiConf == 0):
                        for file in glob.glob("*.jpg"):
                            pass
                        pixmap = QPixmap(file)
                        os.chdir("../..")
                
                    elif (maxiConf == detectBasalConf):
                        os.chdir(f"Basal/Basal")
                        for file in glob.glob("*.jpg"):
                            pass
                        pixmap = QPixmap(file)
                        os.chdir("../../../..")
                    
                    elif (maxiConf == detectDermatofibromaConf):
                        os.chdir(f"Dermatofibroma/Dermatofibroma")
                        for file in glob.glob("*.jpg"):
                            pass
                        pixmap = QPixmap(file)
                        os.chdir("../../../..")

                    elif (maxiConf == detectMelanomaConf):
                        os.chdir(f"Melanoma/Melanoma")
                        for file in glob.glob("*.jpg"):
                            pass
                        pixmap = QPixmap(file)
                        os.chdir("../../../..")                            
                    
                    pixmap = pixmap.scaled(600,450)
                    self.img_lbl.setPixmap(pixmap)
            
                    self.img_lbl.resize(pixmap.width(),pixmap.height())   
                    self.img_lbl.setStyleSheet("border: 2px solid white")

                    sort_rows_by_accuracy(self.kanserTablosu)

                maxConfImageChange(maxConf)
                                                                     
            except Exception :
                    QMessageBox.about(self, "Error!", "An unexpected error occurred.")
                
                                             
        self.detect_label = QLabel(self, text="Detection Panel")
        self.detect_label.setStyleSheet("color: white")
        font = QFont("Times New Roman", 14)
        font.setBold(True)
        self.detect_label.setFont(font)
        self.detect_label.setGeometry(30, 20, 150, 30)  

        self.options_label = QLabel(self, text="Options Panel")
        self.options_label.setStyleSheet("color: white")
        self.options_label.setFont(font)
        self.options_label.setGeometry(680, 25, 150, 30)   

        self.eventSlider = QSlider(Qt.Horizontal, self)
        self.eventSlider.setMinimum(0)
        self.eventSlider.setMaximum(1)
        self.eventSlider.setGeometry(765, 90, 100, 20)
        self.eventSlider.setStyleSheet(
            """
            QSlider::groove:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #8CB2D6, stop:1 #4180C5);
                height: 8px;
                border-radius: 4px;
            }

            QSlider::handle:horizontal {
                background: #ffffff;
                border: 1px solid #4180C5;
                width: 16px;
                height: 16px;
                margin: -8px 0px;
                border-radius: 8px;
            }
            """
        )

        self.newPatientlabel = QLabel("<html>New Patient<br>Entry</html>", self)
        self.newPatientlabel.setGeometry(680, 85, 100, 40)
        self.newPatientlabel.setFont(QFont("Times New Roman", 11))

        self.oldPatientlabel = QLabel("<html>Old Patient<br>Entry</html>", self)
        self.oldPatientlabel.setGeometry(875, 85, 120, 40)
        self.oldPatientlabel.setFont(QFont("Times New Roman", 11))

        self.patient_id_text = QLabel(self, text="Please enter your T.C. Identity Number:") 
        self.patient_id_text.setGeometry(680, 140, 300, 40)
        self.patient_id_text.setStyleSheet("color: white")
        self.patient_id_text.setFont(QFont("Times New Roman", 12))

        self.patient_id = QLineEdit(self)  
        self.patient_id.setGeometry(770, 180, 160, 30)
        self.patient_id.setStyleSheet('''
        QLineEdit {
            background-color: transparent;
            border: 2px solid black;
            border-radius: 15px;
            color: #ffffff;
            font-size: 14px;
            padding: 8px;
        }

        QLineEdit:focus {
            border: 2px solid black;
        }
        ''')
        self.patient_id.setFont(QFont("Times New Roman", 12))
        self.patient_id.setMaxLength(11)       

        self.button = QPushButton(self, text="Detect")
        self.button.setStyleSheet('''
        QPushButton {
            background-color: transparent;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: white;
            font: 12px;
            min-width: 10em;
            padding: 6px;
            color: white;
        }

        QPushButton:hover {
            background-color: #58126a;
        }

        QPushButton:pressed {
            background-color: #78305b;
            border-style: inset;
        }
        ''')

        self.button.setFont(QFont("Times New Roman", 9))
        self.button.setGeometry(745, 230, 160, 30)
        self.button.clicked.connect(dialog)          

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())
