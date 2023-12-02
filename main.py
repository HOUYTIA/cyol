# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerwcwfgJ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
from PIL import Image,ImageDraw,ImageFont
import matplotlib.pyplot as plt
from qndxx import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(110, 85)
        icon=QIcon()
        icon.addFile('resources/cyol_logo.png')
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowFlags(Qt.WindowCloseButtonHint)



        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 81, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font: 9pt \"HarmonyOS Sans SC\";\n"
"text-align:center;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 91, 41))
        self.pushButton.setStyleSheet(u"font: 700 9pt \"HarmonyOS Sans SC\";\n"
"")

        def runing():
            cwd = os.path.abspath(os.path.dirname(sys.argv[0]))
            os.chdir(cwd)
            url = "http://news.cyol.com/gb/channels/vrGlAKDl/index.html"
            qndxx = Get_QNDXX_Picture(url)
            qndxx.get_body()
            qndxx.get_title()
            qndxx.get_phone_title()
            qndxx.finished()
            self.label.setText('运行完毕')
        def imgview():
            img =Image.open('new.jpg')
            plt.rcParams['font.sans-serif']=['SimHei']
            plt.subplot(121)
            plt.imshow(img)
            plt.axis('off')
            plt.tight_layout()
            plt.show()

        #click_event
        self.pushButton.clicked.connect(runing)



        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"生成器", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"quest", None))
    # retranslateUi

if __name__ == "__main__":
    app=QApplication()
    main_window=QMainWindow()

    ui_setup=Ui_MainWindow()
    ui_setup.setupUi(main_window)

    main_window.show()
    app.exec()

