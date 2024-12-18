import sys
import io

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPixmap, QImage, QTransform, QColor
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QButtonGroup, QPushButton, QFileDialog

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>714</width>
    <height>609</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true"/>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QComboBox" name="lst">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>10</y>
      <width>451</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-radius: 10px;
font: 10pt &quot;Noto Sans Armenian&quot;;</string>
    </property>
    <property name="currentText">
     <string/>
    </property>
    <item>
     <property name="text">
      <string/>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Москва</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Санкт-Петербург</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Казань</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Новосибирск</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Сочи</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Элиста</string>
     </property>
    </item>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>714</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusBar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()


    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setFixedSize(800, 600)

        self.lst.activated.connect(self.current_text)

    def open_new_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
    def current_text(self, _):
        if self.lst.currentText() == 'Москва':
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec())
