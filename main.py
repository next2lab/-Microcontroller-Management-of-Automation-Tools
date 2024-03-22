from datetime import datetime
from pathlib import Path
from pyqtgraph import PlotWidget
from threads import MyTimerThread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QIODevice, QTimer
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

# main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 570)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 570))
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(51, 53, 52);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_19.setObjectName("gridLayout_19")

# options block
        self.widget_options_block = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_options_block.sizePolicy().hasHeightForWidth())
        self.widget_options_block.setSizePolicy(sizePolicy)
        self.widget_options_block.setMinimumSize(QtCore.QSize(330, 500))
        self.widget_options_block.setMaximumSize(QtCore.QSize(1222222, 16777215))
        self.widget_options_block.setStyleSheet("")
        self.widget_options_block.setObjectName("widget_options_block")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.widget_options_block)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.toolButton = QtWidgets.QToolButton(self.widget_options_block)
        self.toolButton.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_17.addWidget(self.toolButton, 0, 0, 1, 1)

# connection, logs
        self.widget_connection_block = QtWidgets.QWidget(self.widget_options_block)
        self.widget_connection_block.setMaximumSize(QtCore.QSize(1808, 88888))
        self.widget_connection_block.setObjectName("widget_connection_block")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_connection_block)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox_COM_ports = QtWidgets.QComboBox(self.widget_connection_block)
        self.comboBox_COM_ports.activated.connect(self.get_port_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_COM_ports.sizePolicy().hasHeightForWidth())
        self.comboBox_COM_ports.setSizePolicy(sizePolicy)
        self.comboBox_COM_ports.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_COM_ports.setMaximumSize(QtCore.QSize(200, 30))
        self.comboBox_COM_ports.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.comboBox_COM_ports.setObjectName("comboBox_COM_ports")
        self.gridLayout_5.addWidget(self.comboBox_COM_ports, 0, 0, 1, 1)
        self.pushButton_com_port_connect = QtWidgets.QPushButton(self.widget_connection_block)
        self.pushButton_com_port_connect.clicked.connect(self.open_port)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_com_port_connect.sizePolicy().hasHeightForWidth())
        self.pushButton_com_port_connect.setSizePolicy(sizePolicy)
        self.pushButton_com_port_connect.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_com_port_connect.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_com_port_connect.setFont(font)
        self.pushButton_com_port_connect.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.pushButton_com_port_connect.setObjectName("pushButton_com_port_connect")
        self.gridLayout_5.addWidget(self.pushButton_com_port_connect, 1, 0, 1, 1)
        self.pushButton_com_port_disconnect = QtWidgets.QPushButton(self.widget_connection_block)
        self.pushButton_com_port_disconnect.clicked.connect(self.close_port)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_com_port_disconnect.sizePolicy().hasHeightForWidth())
        self.pushButton_com_port_disconnect.setSizePolicy(sizePolicy)
        self.pushButton_com_port_disconnect.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_com_port_disconnect.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_com_port_disconnect.setFont(font)
        self.pushButton_com_port_disconnect.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.pushButton_com_port_disconnect.setObjectName("pushButton_com_port_disconnect")
        self.gridLayout_5.addWidget(self.pushButton_com_port_disconnect, 2, 0, 1, 1)
        self.frame_log_view = QtWidgets.QFrame(self.widget_connection_block)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_log_view.sizePolicy().hasHeightForWidth())
        self.frame_log_view.setSizePolicy(sizePolicy)
        self.frame_log_view.setMinimumSize(QtCore.QSize(300, 320))
        self.frame_log_view.setMaximumSize(QtCore.QSize(300, 700))
        self.frame_log_view.setStyleSheet("background-color:rgb(90, 93, 92);")
        self.frame_log_view.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_log_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_log_view.setLineWidth(2)
        self.frame_log_view.setObjectName("frame_log_view")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_log_view)
        self.gridLayout_4.setContentsMargins(3, -1, 3, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_com_port_number = QtWidgets.QLabel(self.frame_log_view)
        self.label_com_port_number.setObjectName("label_com_port_number")
        self.gridLayout_4.addWidget(self.label_com_port_number, 4, 0, 1, 1)
        self.label_log = QtWidgets.QLabel(self.frame_log_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_log.sizePolicy().hasHeightForWidth())
        self.label_log.setSizePolicy(sizePolicy)
        self.label_log.setMinimumSize(QtCore.QSize(216, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_log.setFont(font)
        self.label_log.setStyleSheet("")
        self.label_log.setObjectName("label_log")
        self.gridLayout_4.addWidget(self.label_log, 1, 0, 1, 1)
        self.label_arduino_connection_status = QtWidgets.QLabel(self.frame_log_view)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_arduino_connection_status.setFont(font)
        self.label_arduino_connection_status.setStyleSheet("color: rgb(255, 185, 139);")
        self.label_arduino_connection_status.setObjectName("label_arduino_connection_status")
        self.gridLayout_4.addWidget(self.label_arduino_connection_status, 1, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.frame_log_view)
        self.listWidget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.listWidget.setStyleSheet("background-color:#989590;")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_4.addWidget(self.listWidget, 3, 0, 1, 2)
        self.gridLayout_5.addWidget(self.frame_log_view, 3, 0, 1, 1)
        self.gridLayout_17.addWidget(self.widget_connection_block, 1, 0, 1, 1)
        self.gridLayout_19.addWidget(self.widget_options_block, 0, 0, 1, 1)

# sensor block
        self.widget_devices_block = QtWidgets.QWidget(self.centralwidget)
        self.widget_devices_block.setStyleSheet("")
        self.widget_devices_block.setObjectName("widget_devices_block")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_devices_block)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_devices_subblock1 = QtWidgets.QWidget(self.widget_devices_block)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_devices_subblock1.sizePolicy().hasHeightForWidth())

# sub-block 1 (upper) I2C1602, PWM, Matrix8x8, Character Display
        self.widget_devices_subblock1.setSizePolicy(sizePolicy)
        self.widget_devices_subblock1.setMaximumSize(QtCore.QSize(3000, 3000))
        self.widget_devices_subblock1.setObjectName("widget_devices_subblock1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_devices_subblock1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(80, 1, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(369, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(368, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(369, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(80, 1, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(80, 1, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(120, 1, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(369, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 0, 1, 1, 1)

# I2C1602 display
        self.widget_i2c1602 = QtWidgets.QWidget(self.widget_devices_subblock1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_i2c1602.sizePolicy().hasHeightForWidth())
        self.widget_i2c1602.setSizePolicy(sizePolicy)
        self.widget_i2c1602.setMinimumSize(QtCore.QSize(150, 105))
        self.widget_i2c1602.setMaximumSize(QtCore.QSize(330, 330))
        self.widget_i2c1602.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.widget_i2c1602.setObjectName("widget_i2c1602")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_i2c1602)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.widget_i2c1602)
        self.widget.setMinimumSize(QtCore.QSize(132, 138))
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(140, 0))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.checkBox_i2c1602_show_log = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_i2c1602_show_log.setObjectName("checkBox_i2c1602_show_log")
        self.gridLayout_9.addWidget(self.checkBox_i2c1602_show_log, 2, 0, 1, 1)
        self.checkBox_i2c1602_show_pwm = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_i2c1602_show_pwm.setObjectName("checkBox_i2c1602_show_pwm")
        self.gridLayout_9.addWidget(self.checkBox_i2c1602_show_pwm, 2, 1, 1, 1)
        self.checkBox_i2c1602_show_weather = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_i2c1602_show_weather.setObjectName("checkBox_i2c1602_show_weather")
        self.gridLayout_9.addWidget(self.checkBox_i2c1602_show_weather, 1, 1, 1, 1)
        self.checkBox_i2c1602_show_moisure = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_i2c1602_show_moisure.setObjectName("checkBox_i2c1602_show_moisure")
        self.gridLayout_9.addWidget(self.checkBox_i2c1602_show_moisure, 1, 0, 1, 1)
        self.checkBox_i2c1602_show_timer = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_i2c1602_show_timer.setObjectName("checkBox_i2c1602_show_timer")
        self.gridLayout_9.addWidget(self.checkBox_i2c1602_show_timer, 3, 0, 1, 1)
        self.checkBox_i2c1602_show_clock = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_i2c1602_show_clock.setObjectName("checkBox_i2c1602_show_clock")
        self.gridLayout_9.addWidget(self.checkBox_i2c1602_show_clock, 3, 1, 1, 1)
        self.gridLayout_7.addWidget(self.widget_3, 3, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.textEdit_i2c1602_send_text = QtWidgets.QTextEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_i2c1602_send_text.sizePolicy().hasHeightForWidth())
        self.textEdit_i2c1602_send_text.setSizePolicy(sizePolicy)
        self.textEdit_i2c1602_send_text.setMinimumSize(QtCore.QSize(0, 35))
        self.textEdit_i2c1602_send_text.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit_i2c1602_send_text.setStyleSheet("background-color:#fdfef9;")
        self.textEdit_i2c1602_send_text.setMidLineWidth(3)
        self.textEdit_i2c1602_send_text.setObjectName("textEdit_i2c1602_send_text")
        self.gridLayout_8.addWidget(self.textEdit_i2c1602_send_text, 0, 0, 1, 2)
        self.pushButton_i2c1602_send_text = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_i2c1602_send_text.clicked.connect(self.send_text_to_lcd1602)
        self.pushButton_i2c1602_send_text.setObjectName("pushButton_i2c1602_send_text")
        self.gridLayout_8.addWidget(self.pushButton_i2c1602_send_text, 1, 0, 1, 2)
        self.gridLayout_7.addWidget(self.widget_2, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget)
        self.line = QtWidgets.QFrame(self.widget_i2c1602)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.widget_i2c1602)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout_2.addWidget(self.widget_i2c1602, 2, 1, 1, 1)

# PWM Mosfet module
        self.widget_mosfet = QtWidgets.QWidget(self.widget_devices_subblock1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_mosfet.sizePolicy().hasHeightForWidth())
        self.widget_mosfet.setSizePolicy(sizePolicy)
        self.widget_mosfet.setMinimumSize(QtCore.QSize(150, 105))
        self.widget_mosfet.setMaximumSize(QtCore.QSize(330, 330))
        self.widget_mosfet.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.widget_mosfet.setObjectName("widget_mosfet")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_mosfet)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_13 = QtWidgets.QWidget(self.widget_mosfet)
        self.widget_13.setMinimumSize(QtCore.QSize(0, 138))
        self.widget_13.setObjectName("widget_13")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_13)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.widget_24 = QtWidgets.QWidget(self.widget_13)
        self.widget_24.setObjectName("widget_24")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.widget_24)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalSlider_pwm_duty_cycle = QtWidgets.QSlider(self.widget_24)
        self.horizontalSlider_pwm_duty_cycle.valueChanged.connect(self.change_pwm_value)
        self.horizontalSlider_pwm_duty_cycle.setRange(0, 255)
        self.horizontalSlider_pwm_duty_cycle.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_pwm_duty_cycle.setObjectName("horizontalSlider_pwm_duty_cycle")
        self.gridLayout_14.addWidget(self.horizontalSlider_pwm_duty_cycle, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.widget_24, 1, 0, 1, 1)
        self.frame_pwm_oscilloscope = QtWidgets.QFrame(self.widget_13)
        self.frame_pwm_oscilloscope.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_pwm_oscilloscope.setStyleSheet("background-color:rgb(90, 93, 92);")
        self.frame_pwm_oscilloscope.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_pwm_oscilloscope.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pwm_oscilloscope.setLineWidth(2)
        self.frame_pwm_oscilloscope.setMidLineWidth(0)
        self.frame_pwm_oscilloscope.setObjectName("frame_pwm_oscilloscope")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_pwm_oscilloscope)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_pwm_oscilloscope = PlotWidget(self.frame_pwm_oscilloscope)
        self.widget_pwm_oscilloscope.setObjectName("widget_pwm_oscilloscope")
        self.verticalLayout_9.addWidget(self.widget_pwm_oscilloscope)
        self.gridLayout_13.addWidget(self.frame_pwm_oscilloscope, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_13)
        self.line_3 = QtWidgets.QFrame(self.widget_mosfet)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.label_3 = QtWidgets.QLabel(self.widget_mosfet)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.gridLayout_2.addWidget(self.widget_mosfet, 2, 3, 1, 1)

# character display 4x7digit
        self.widget_symbolik4x7digit = QtWidgets.QWidget(self.widget_devices_subblock1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_symbolik4x7digit.sizePolicy().hasHeightForWidth())
        self.widget_symbolik4x7digit.setSizePolicy(sizePolicy)
        self.widget_symbolik4x7digit.setMinimumSize(QtCore.QSize(150, 105))
        self.widget_symbolik4x7digit.setMaximumSize(QtCore.QSize(330, 330))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.widget_symbolik4x7digit.setFont(font)
        self.widget_symbolik4x7digit.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.widget_symbolik4x7digit.setObjectName("widget_symbolik4x7digit")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.widget_symbolik4x7digit)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_4 = QtWidgets.QLabel(self.widget_symbolik4x7digit)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_24.addWidget(self.label_4, 4, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.widget_symbolik4x7digit)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_24.addWidget(self.line_4, 3, 0, 1, 1)
        self.widget_28 = QtWidgets.QWidget(self.widget_symbolik4x7digit)
        self.widget_28.setMinimumSize(QtCore.QSize(0, 138))
        self.widget_28.setObjectName("widget_28")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.widget_28)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.widget_11 = QtWidgets.QWidget(self.widget_28)
        self.widget_11.setStyleSheet("background-color: rgb(213, 209, 202);")
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber_symb_disp1 = QtWidgets.QLCDNumber(self.widget_11)
        self.lcdNumber_symb_disp1.setStyleSheet("color: rgb(207, 227, 255);\n"
                                                "background-color:#464847;")
        self.lcdNumber_symb_disp1.setDigitCount(1)
        self.lcdNumber_symb_disp1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_symb_disp1.setObjectName("lcdNumber_symb_disp1")
        self.horizontalLayout.addWidget(self.lcdNumber_symb_disp1)
        self.lcdNumber_symb_disp2 = QtWidgets.QLCDNumber(self.widget_11)
        self.lcdNumber_symb_disp2.setStyleSheet("color: rgb(207, 227, 255);\n"
                                                "background-color:#464847;")
        self.lcdNumber_symb_disp2.setDigitCount(1)
        self.lcdNumber_symb_disp2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_symb_disp2.setObjectName("lcdNumber_symb_disp2")
        self.horizontalLayout.addWidget(self.lcdNumber_symb_disp2)
        self.lcdNumber_symb_disp3 = QtWidgets.QLCDNumber(self.widget_11)
        self.lcdNumber_symb_disp3.setStyleSheet("color: rgb(207, 227, 255);\n"
                                                "background-color:#464847;")
        self.lcdNumber_symb_disp3.setDigitCount(1)
        self.lcdNumber_symb_disp3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_symb_disp3.setObjectName("lcdNumber_symb_disp3")
        self.horizontalLayout.addWidget(self.lcdNumber_symb_disp3)
        self.lcdNumber_symb_disp4 = QtWidgets.QLCDNumber(self.widget_11)
        self.lcdNumber_symb_disp4.setStyleSheet("color: rgb(207, 227, 255);\n"
                                                "background-color:#464847;")
        self.lcdNumber_symb_disp4.setDigitCount(1)
        self.lcdNumber_symb_disp4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_symb_disp4.setObjectName("lcdNumber_symb_disp4")
        self.horizontalLayout.addWidget(self.lcdNumber_symb_disp4)
        self.gridLayout_23.addWidget(self.widget_11, 0, 0, 1, 1)
        self.radioButton_symb_disp_show_timer = QtWidgets.QRadioButton(self.widget_28)
        self.radioButton_symb_disp_show_timer.clicked.connect(self.display_4x7digit)               # oновлюємо значення
        self.radioButton_symb_disp_show_timer.setChecked(True)                             # увімкнено за замовчуванням
        self.radioButton_symb_disp_show_timer.setObjectName("radioButton_symb_disp_show_timer")
        self.gridLayout_23.addWidget(self.radioButton_symb_disp_show_timer, 1, 0, 1, 1)
        self.radioButton_symb_disp_show_clock = QtWidgets.QRadioButton(self.widget_28)
        self.radioButton_symb_disp_show_clock.clicked.connect(self.display_4x7digit)               # oновлюємо значення
        self.radioButton_symb_disp_show_clock.setObjectName("radioButton_symb_disp_show_clock")
        self.gridLayout_23.addWidget(self.radioButton_symb_disp_show_clock, 2, 0, 1, 1)
        self.gridLayout_24.addWidget(self.widget_28, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_symbolik4x7digit, 2, 7, 1, 1)

# 8x8 matrix MAX7219
        self.widget_matrix8x8 = QtWidgets.QWidget(self.widget_devices_subblock1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_matrix8x8.sizePolicy().hasHeightForWidth())
        self.widget_matrix8x8.setSizePolicy(sizePolicy)
        self.widget_matrix8x8.setMinimumSize(QtCore.QSize(150, 105))
        self.widget_matrix8x8.setMaximumSize(QtCore.QSize(330, 330))
        self.widget_matrix8x8.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.widget_matrix8x8.setObjectName("widget_matrix8x8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_matrix8x8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_23 = QtWidgets.QWidget(self.widget_matrix8x8)
        self.widget_23.setMinimumSize(QtCore.QSize(0, 138))
        self.widget_23.setObjectName("widget_23")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.widget_23)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.widget_9 = QtWidgets.QWidget(self.widget_23)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.pushButton_matrix8x8_send = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_matrix8x8_send.clicked.connect(self.matrix_8x8)
        self.pushButton_matrix8x8_send.setObjectName("pushButton_matrix8x8_send")
        self.gridLayout_22.addWidget(self.pushButton_matrix8x8_send, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.widget_9, 2, 0, 1, 1)
        self.widget_29 = QtWidgets.QWidget(self.widget_23)
        self.widget_29.setObjectName("widget_29")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_29)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_matrix8x8 = QtWidgets.QTextEdit(self.widget_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_matrix8x8.sizePolicy().hasHeightForWidth())
        self.textEdit_matrix8x8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.textEdit_matrix8x8.setFont(font)
        self.textEdit_matrix8x8.setStyleSheet("background-color: rgb(213, 209, 202);")
        self.textEdit_matrix8x8.setObjectName("textEdit_matrix8x8")
        self.verticalLayout.addWidget(self.textEdit_matrix8x8)
        self.gridLayout_18.addWidget(self.widget_29, 1, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.widget_23)
        self.line_2 = QtWidgets.QFrame(self.widget_matrix8x8)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.widget_matrix8x8)
        self.label_2.setMinimumSize(QtCore.QSize(137, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.gridLayout_2.addWidget(self.widget_matrix8x8, 2, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 330, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem8, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget_devices_subblock1, 0, 1, 1, 1)

# sub-block 2 (Lower) Rain sensor, Relay/timer, Encoder, Soil moisture sensor
        self.widget_devices_subblock2 = QtWidgets.QWidget(self.widget_devices_block)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_devices_subblock2.sizePolicy().hasHeightForWidth())
        self.widget_devices_subblock2.setSizePolicy(sizePolicy)
        self.widget_devices_subblock2.setMaximumSize(QtCore.QSize(3000, 3000))
        self.widget_devices_subblock2.setObjectName("widget_devices_subblock2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_devices_subblock2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(369, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(369, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 0, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 0, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(368, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem13, 0, 4, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem14, 0, 5, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(369, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem15, 0, 6, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem16, 0, 7, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 330, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem17, 1, 7, 1, 1)

# rain sensor
        self.widget_rain_sensor = QtWidgets.QWidget(self.widget_devices_subblock2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_rain_sensor.sizePolicy().hasHeightForWidth())
        self.widget_rain_sensor.setSizePolicy(sizePolicy)
        self.widget_rain_sensor.setMinimumSize(QtCore.QSize(150, 105))
        self.widget_rain_sensor.setMaximumSize(QtCore.QSize(330, 330))
        self.widget_rain_sensor.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.widget_rain_sensor.setObjectName("widget_rain_sensor")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_rain_sensor)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_15 = QtWidgets.QWidget(self.widget_rain_sensor)
        self.widget_15.setMinimumSize(QtCore.QSize(0, 138))
        self.widget_15.setObjectName("widget_15")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget_15)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.widget_7 = QtWidgets.QWidget(self.widget_15)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_678 = QtWidgets.QLabel(self.widget_7)
        self.label_678.setObjectName("label_678")
        self.gridLayout_11.addWidget(self.label_678, 0, 0, 1, 1)
        self.progressBar_rain_sens_level = QtWidgets.QProgressBar(self.widget_7)
        font = QtGui.QFont()
        font.setKerning(True)
        self.progressBar_rain_sens_level.setFont(font)
        self.progressBar_rain_sens_level.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.progressBar_rain_sens_level.setStyleSheet("QProgressBar{\n"
                                                       "    background-color: #fdfef9;\n"
                                                       "    border-style: solid;\n"
                                                       "    border-radius: 10px;\n"
                                                       "    text-align: center;}\n"
                                                       "QProgressBar::chunk{\n"
                                                       "    background-color:rgb(0, 122, 217);\n"
                                                       "    border-radius: 10px;}")
        self.progressBar_rain_sens_level.setProperty("value", 0)
        self.progressBar_rain_sens_level.setObjectName("progressBar_rain_sens_level")
        self.gridLayout_11.addWidget(self.progressBar_rain_sens_level, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.widget_7, 0, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.widget_15)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem18, 1, 1, 1, 1)
        self.label_rain_sens_status_icon = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rain_sens_status_icon.sizePolicy().hasHeightForWidth())
        self.label_rain_sens_status_icon.setSizePolicy(sizePolicy)
        self.label_rain_sens_status_icon.setMinimumSize(QtCore.QSize(40, 40))
        self.label_rain_sens_status_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.label_rain_sens_status_icon.setText("")
        self.label_rain_sens_status_icon.setScaledContents(True)
        self.label_rain_sens_status_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rain_sens_status_icon.setObjectName("label_rain_sens_status_icon")
        self.gridLayout_12.addWidget(self.label_rain_sens_status_icon, 1, 2, 1, 1)
        self.checkBox_rain_sens_connect_to_relay = QtWidgets.QCheckBox(self.widget_6)
        self.checkBox_rain_sens_connect_to_relay.clicked.connect(self.enable_rain_buzzer)
        self.checkBox_rain_sens_connect_to_relay.setObjectName("checkBox_rain_sens_connect_to_relay")
        self.gridLayout_12.addWidget(self.checkBox_rain_sens_connect_to_relay, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.widget_6, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_15)
        self.line_7 = QtWidgets.QFrame(self.widget_rain_sensor)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_4.addWidget(self.line_7)
        self.label_7 = QtWidgets.QLabel(self.widget_rain_sensor)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.gridLayout_3.addWidget(self.widget_rain_sensor, 1, 0, 1, 1)

# relay/timer
        self.widget_relay = QtWidgets.QWidget(self.widget_devices_subblock2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_relay.sizePolicy().hasHeightForWidth())
        self.widget_relay.setSizePolicy(sizePolicy)
        self.widget_relay.setMinimumSize(QtCore.QSize(150, 105))
        self.widget_relay.setMaximumSize(QtCore.QSize(330, 330))
        self.widget_relay.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.widget_relay.setObjectName("widget_relay")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_relay)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_17 = QtWidgets.QWidget(self.widget_relay)
        self.widget_17.setMinimumSize(QtCore.QSize(0, 138))
        self.widget_17.setObjectName("widget_17")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.widget_17)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.pushButton_relay_timer_stop = QtWidgets.QPushButton(self.widget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_relay_timer_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_relay_timer_stop.setSizePolicy(sizePolicy)
        self.pushButton_relay_timer_stop.clicked.connect(self.stop_timer)
        self.pushButton_relay_timer_stop.setObjectName("pushButton_relay_timer_stop")
        self.gridLayout_16.addWidget(self.pushButton_relay_timer_stop, 6, 2, 1, 1)
        self.horizontalSlider_relay_timer_value = QtWidgets.QSlider(self.widget_17)
        self.horizontalSlider_relay_timer_value.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_relay_timer_value.valueChanged.connect(self.update_timer_value)
        self.horizontalSlider_relay_timer_value.setObjectName("horizontalSlider_relay_timer_value")
        self.gridLayout_16.addWidget(self.horizontalSlider_relay_timer_value, 4, 0, 1, 3)
        self.lcdNumber_relay_timer = QtWidgets.QLCDNumber(self.widget_17)
        self.lcdNumber_relay_timer.setMinimumSize(QtCore.QSize(0, 25))
        self.lcdNumber_relay_timer.setObjectName("lcdNumber_relay_timer")
        self.gridLayout_16.addWidget(self.lcdNumber_relay_timer, 5, 0, 1, 3)
        self.radioButton_relay_on = QtWidgets.QRadioButton(self.widget_17)
        self.radioButton_relay_on.clicked.connect(self.relay_on)
        self.radioButton_relay_on.setObjectName("radioButton_relay_on")
        self.gridLayout_16.addWidget(self.radioButton_relay_on, 0, 0, 1, 1)
        self.radioButton_relay_off = QtWidgets.QRadioButton(self.widget_17)
        self.radioButton_relay_off.clicked.connect(self.relay_off)
        self.radioButton_relay_off.setChecked(True)                                          # вибрано за замовчуванням
        self.radioButton_relay_off.setObjectName("radioButton_relay_off")
        self.gridLayout_16.addWidget(self.radioButton_relay_off, 2, 0, 1, 1)
        self.radioButton_relay_timer = QtWidgets.QRadioButton(self.widget_17)
        self.radioButton_relay_timer.setObjectName("radioButton_relay_timer")
        self.gridLayout_16.addWidget(self.radioButton_relay_timer, 0, 2, 1, 1)
        self.pushButton_relay_timer_start = QtWidgets.QPushButton(self.widget_17)
        self.pushButton_relay_timer_start.clicked.connect(self.start_timer)                # пуск/пауза відліку таймера
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_relay_timer_start.sizePolicy().hasHeightForWidth())
        self.pushButton_relay_timer_start.setSizePolicy(sizePolicy)
        self.pushButton_relay_timer_start.setObjectName("pushButton_relay_timer_start")
        self.gridLayout_16.addWidget(self.pushButton_relay_timer_start, 6, 0, 1, 1)
        self.radioButton_relay_side_in = QtWidgets.QRadioButton(self.widget_17)
        self.radioButton_relay_side_in.setObjectName("radioButton_relay_side_in")
        self.gridLayout_16.addWidget(self.radioButton_relay_side_in, 2, 2, 1, 1)
        self.verticalLayout_5.addWidget(self.widget_17)
        self.line_8 = QtWidgets.QFrame(self.widget_relay)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_5.addWidget(self.line_8)
        self.label_8 = QtWidgets.QLabel(self.widget_relay)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.gridLayout_3.addWidget(self.widget_relay, 1, 2, 1, 1)

# encoder
        self.widget_encoder = QtWidgets.QWidget(self.widget_devices_subblock2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_encoder.sizePolicy().hasHeightForWidth())
        self.widget_encoder.setSizePolicy(sizePolicy)
        self.widget_encoder.setMinimumSize(QtCore.QSize(150, 105))
        self.widget_encoder.setMaximumSize(QtCore.QSize(330, 330))
        self.widget_encoder.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.widget_encoder.setObjectName("widget_encoder")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_encoder)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_19 = QtWidgets.QWidget(self.widget_encoder)
        self.widget_19.setMinimumSize(QtCore.QSize(0, 138))
        self.widget_19.setObjectName("widget_19")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_19)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_connect_encoder_to_timer = QtWidgets.QRadioButton(self.widget_19)
        self.radioButton_connect_encoder_to_timer.setChecked(True)                           # вибрано за замовчуванням
        self.radioButton_connect_encoder_to_timer.setObjectName("radioButton_connect_encoder_to_timer")
        self.gridLayout.addWidget(self.radioButton_connect_encoder_to_timer, 2, 0, 1, 1)
        self.radioButton_connect_encoder_to_pwm = QtWidgets.QRadioButton(self.widget_19)
        self.radioButton_connect_encoder_to_pwm.setObjectName("radioButton_connect_encoder_to_pwm")
        self.gridLayout.addWidget(self.radioButton_connect_encoder_to_pwm, 2, 1, 1, 1)
        self.dial_encoder = QtWidgets.QDial(self.widget_19)
        self.dial_encoder.valueChanged.connect(lambda: self.dial_move())                           # під'єднуємо дайлер
        self.dial_encoder.setStyleSheet("background-color:#fdfef9;")
        self.dial_encoder.setObjectName("dial_encoder")
        self.gridLayout.addWidget(self.dial_encoder, 1, 0, 1, 2)
        self.verticalLayout_6.addWidget(self.widget_19)
        self.line_5 = QtWidgets.QFrame(self.widget_encoder)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_6.addWidget(self.line_5)
        self.label_5 = QtWidgets.QLabel(self.widget_encoder)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.gridLayout_3.addWidget(self.widget_encoder, 1, 4, 1, 1)

# soil moisture sensor
        self.widget_moisture_sensor = QtWidgets.QWidget(self.widget_devices_subblock2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_moisture_sensor.sizePolicy().hasHeightForWidth())
        self.widget_moisture_sensor.setSizePolicy(sizePolicy)
        self.widget_moisture_sensor.setMinimumSize(QtCore.QSize(150, 105))
        self.widget_moisture_sensor.setMaximumSize(QtCore.QSize(330, 330))
        self.widget_moisture_sensor.setStyleSheet("background-color:rgb(182, 179, 174);")
        self.widget_moisture_sensor.setObjectName("widget_moisture_sensor")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_moisture_sensor)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_21 = QtWidgets.QWidget(self.widget_moisture_sensor)
        self.widget_21.setMinimumSize(QtCore.QSize(0, 138))
        self.widget_21.setObjectName("widget_21")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.widget_21)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_moisture_relay_en_level = QtWidgets.QLabel(self.widget_21)
        self.label_moisture_relay_en_level.setObjectName("label_moisture_relay_en_level")
        self.gridLayout_21.addWidget(self.label_moisture_relay_en_level, 4, 0, 1, 1)
        self.widget_27 = QtWidgets.QWidget(self.widget_21)
        self.widget_27.setMinimumSize(QtCore.QSize(65, 65))
        self.widget_27.setObjectName("widget_27")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.widget_27)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.progressBar_moisture_level = QtWidgets.QProgressBar(self.widget_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_moisture_level.sizePolicy().hasHeightForWidth())
        self.progressBar_moisture_level.setSizePolicy(sizePolicy)
        self.progressBar_moisture_level.setMaximumSize(QtCore.QSize(130, 16777215))
        self.progressBar_moisture_level.setStyleSheet("QProgressBar{\n"
                                                      "    background-color:#fdfef9;\n"
                                                      "    border-style: solid;\n"
                                                      "    text-align: center;}\n"
                                                      "QProgressBar::chunk{\n"
                                                      "    background-color:rgb(36, 160, 217);}")
        self.progressBar_moisture_level.setProperty("value", 0)
        self.progressBar_moisture_level.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_moisture_level.setObjectName("progressBar_moisture_level")
        self.gridLayout_25.addWidget(self.progressBar_moisture_level, 0, 0, 1, 1)
        self.gridLayout_21.addWidget(self.widget_27, 0, 0, 1, 3)
        self.horizontalSlider_moisture_relay_en_level = QtWidgets.QSlider(self.widget_21)
        self.horizontalSlider_moisture_relay_en_level.valueChanged.connect(self.enable_relay_moisture_sens_level)
        self.horizontalSlider_moisture_relay_en_level.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_moisture_relay_en_level.setObjectName("horizontalSlider_moisture_relay_en_level")
        self.gridLayout_21.addWidget(self.horizontalSlider_moisture_relay_en_level, 3, 0, 1, 3)
        self.checkBox_connect_moisture_to_relay = QtWidgets.QCheckBox(self.widget_21)
        self.checkBox_connect_moisture_to_relay.clicked.connect(self.enable_pump)
        self.checkBox_connect_moisture_to_relay.setText("")
        self.checkBox_connect_moisture_to_relay.setObjectName("checkBox_connect_moisture_to_relay")
        self.gridLayout_21.addWidget(self.checkBox_connect_moisture_to_relay, 4, 2, 1, 1)
        self.verticalLayout_7.addWidget(self.widget_21)
        self.line_6 = QtWidgets.QFrame(self.widget_moisture_sensor)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_7.addWidget(self.line_6)
        self.label_6 = QtWidgets.QLabel(self.widget_moisture_sensor)
        self.label_6.setMinimumSize(QtCore.QSize(137, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.gridLayout_3.addWidget(self.widget_moisture_sensor, 1, 6, 1, 1)
        self.gridLayout_6.addWidget(self.widget_devices_subblock2, 1, 1, 1, 1)
        self.gridLayout_19.addWidget(self.widget_devices_block, 0, 1, 1, 1)

# змінні
        self.ports = []                                                                                 # list of ports
        self.port_is_connect = False                                                                # connection status
        self.status_connected = False                                    # connection status (if data from MCU is read)
        self.status_disconnected = True
        self.logs_count = 0                                                                              # logs counter
        self.current_timer = 0                                                                    # current timer value
        self.timer_is_running = False                                                                    # timer status
        self.current_encoder_position = 0                                                    # current encoder position
        self.input_data = ''                                                                       # initial indicators
        self.input_data_dict = {"1": "0", "2": "0", "3": "0"}
        self.output_data_dict = {"1": "0", "2": "0", "3": "0", "4": "0", "5": "1", "6": "0"}
        self.old_output_data_dict = {"1": "0", "2": "0", "3": "0", "4": "0", "5": "1", "6": "0"}
        self.moisture_value = 0                                                           # current soil moisture value
        self.rain_detector_value = 0                                                        # current rain sensor value
        # self.relay_is_active = False                                                                   # relay status
        self.ready_to_write = False                                                # availability of packet for sending
        self.pwm_value = 0                                                                          # current PWM value
        self.current_path = Path(__file__).parent                                       # path to the current directory
        self.current_log = ''                                                                             # current log
        self.weather_status = "Sunny"                                                                  # weather status
        self.lcd1602_cycle_count = 0                                                   # I2C1602 display update counter


        MainWindow.setCentralWidget(self.centralwidget)
# threads
        self.serial = QSerialPort()                                                         # create serial port object
        self.serial.setBaudRate(9600)                                                                   # set baud rate
        
        self.update_clock_timer = QTimer()                                                        # create timer object
        self.update_clock_timer.timeout.connect(self.clock_update)                      # connect clock update function
        self.update_clock_timer.start(60000)                                                     # timeout every minute
        
        self.update_lcd1602_timer = QTimer()
        self.update_lcd1602_timer.timeout.connect(self.lcd1602_cycle)                 # connect I2C1602 update function
        self.update_lcd1602_timer.start(3000)                                                       # timeout 3 seconds
        
        self.timer_thread = MyTimerThread(mainwindow=self)                           # create relay timer thread object
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "DUIT 2023 'Microcontroller management of automation tools'"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton_com_port_connect.setText(_translate("MainWindow", "Establish connection"))
        self.pushButton_com_port_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.label_com_port_number.setText(_translate("MainWindow", "disconnected"))
        self.label_log.setText(_translate("MainWindow", "log"))
        self.label_arduino_connection_status.setText(_translate("MainWindow", "noData"))
        self.checkBox_i2c1602_show_log.setText(_translate("MainWindow", "log"))
        self.checkBox_i2c1602_show_pwm.setText(_translate("MainWindow", "PWM"))
        self.checkBox_i2c1602_show_weather.setText(_translate("MainWindow", "Weather"))
        self.checkBox_i2c1602_show_moisure.setText(_translate("MainWindow", "Soil"))
        self.checkBox_i2c1602_show_timer.setText(_translate("MainWindow", "timer"))
        self.checkBox_i2c1602_show_clock.setText(_translate("MainWindow", "Clock"))
        self.pushButton_i2c1602_send_text.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Display I2C1602"))
        self.label_3.setText(_translate("MainWindow", "PWM Mosfet module"))
        self.label_4.setText(_translate("MainWindow", "Character display 4x7digit"))
        self.radioButton_symb_disp_show_timer.setText(_translate("MainWindow", "Display timer"))
        self.radioButton_symb_disp_show_clock.setText(_translate("MainWindow", "Clock"))
        self.pushButton_matrix8x8_send.setText(_translate("MainWindow", "Send"))
        self.label_2.setText(_translate("MainWindow", "Matrix 8x8 MAX7219"))
        self.label_678.setText(_translate("MainWindow", "Current moisture"))
        self.checkBox_rain_sens_connect_to_relay.setText(_translate("MainWindow", "Relay"))
        self.label_7.setText(_translate("MainWindow", "Rain sensor"))
        self.pushButton_relay_timer_stop.setText(_translate("MainWindow", "Stop"))
        self.radioButton_relay_on.setText(_translate("MainWindow", "On"))
        self.radioButton_relay_off.setText(_translate("MainWindow", "Off"))
        self.radioButton_relay_timer.setText(_translate("MainWindow", "Timer"))
        self.pushButton_relay_timer_start.setText(_translate("MainWindow", "Start"))
        self.radioButton_relay_side_in.setText(_translate("MainWindow", "Input"))
        self.label_8.setText(_translate("MainWindow", "Relay"))
        self.radioButton_connect_encoder_to_timer.setText(_translate("MainWindow", "Timer"))
        self.radioButton_connect_encoder_to_pwm.setText(_translate("MainWindow", "PWM"))
        self.label_5.setText(_translate("MainWindow", "Encoder"))
        self.label_moisture_relay_en_level.setText(_translate("MainWindow", "Start irrigation at"))
        self.label_6.setText(_translate("MainWindow", "Soil moisture sensor"))
        self.get_port_info()
        self.display_4x7digit()
        self.oscilloscope()

    def get_port_info(self):                                                 # update information about available ports
        if QSerialPortInfo().availablePorts():
            ports = [port.portName() for port in QSerialPortInfo().availablePorts()]           # generate list of ports
        else:
            ports = ["No ports found"]
        if self.ports != ports:                                                               # detect changes in ports
            self.add_to_log('Device list changed')                                                       # write to log
            self.comboBox_COM_ports.clear()
            self.ports = ports
            self.first_port = self.ports[0]
            for port in self.ports:
                self.comboBox_COM_ports.addItem(port)                                      # add port names to combobox

    def open_port(self):
        if self.port_is_connect or self.ports == ["No ports found"]:                        # check if not already open
            return                                                                                              # close
        self.serial.setPortName(self.comboBox_COM_ports.currentText())       # select the current entry in the combobox
        self.serial.open(QIODevice.ReadWrite)                                                                    # open
        self.add_to_log(f"{self.comboBox_COM_ports.currentText()} connected")                            # write to log
        self.label_com_port_number.setText(self.comboBox_COM_ports.currentText())   # add port number to the info panel
        self.port_is_connect = True
        self.serial.readyRead.connect(self.read_port)               # signal connection when incoming data is available

    def read_port(self):                                                                                 # reading data
        try:
            self.input_data = str(self.serial.readLine(), 'utf-8').strip()                                 # formatting
        except Exception as ex:
            self.add_to_log('Exception ' + str(ex))                                                # write error to log
            self.close_port()                                                              # call port closing function
        # data processing
        if self.input_data:
            self.connect_status()                                              # call connection status update function
            input_data = set(self.input_data.split(','))                                       # set removes duplicates
            input_data_dict = self.input_data_dict.copy()
            for data in input_data:                                  # filter out invalid entries and add to dictionary
                if len(data) > 2:
                    data = data.split(':')
                    if len(data[0]) == 1:
                        input_data_dict[data[0]] = data[1]
            # decoding received data according to protocol
            if input_data_dict['1'] != self.input_data_dict['1']:                                     # 1: encoder data
                self.input_data_dict['1'] = input_data_dict['1']
                self.arduino_encoder()
            if input_data_dict['2'] != self.input_data_dict['2']:                             # 2: soil moisture sensor
                self.input_data_dict['2'] = input_data_dict['2']
                self.moisture_sensor()
                if self.radioButton_relay_side_in.isChecked() and self.checkBox_connect_moisture_to_relay.isChecked():
                    if self.moisture_value > self.horizontalSlider_moisture_relay_en_level.value():
                        self.relay_off()
                    else:
                        self.relay_on()
            if input_data_dict['3'] != self.input_data_dict['3']:                                      # 3: rain sensor
                self.input_data_dict['3'] = input_data_dict['3']
                self.rain_detector()
                if self.radioButton_relay_side_in.isChecked() and self.checkBox_rain_sens_connect_to_relay.isChecked():
                    if self.weather_status == "rainy":
                        self.relay_off()
                    else:
                        self.relay_on()
        if self.ready_to_write:                                                              # if there is data to send
            self.send_to_port()                                                                 # call sending function
            self.ready_to_write = False                                                                 # toggle status

    def send_to_port(self):
        send_string = ''
        for key, value in self.output_data_dict.items():        # convert dictionary to a string of the required format
            if self.output_data_dict[key] != self.old_output_data_dict[key]:
                send_string += f"{key}:{value},"
        self.serial.write(send_string.encode())                                                         # write to port
        self.old_output_data_dict = self.output_data_dict.copy()                                    # update dictionary

    def close_port(self):
        self.serial.close()                                                                            # close the port
        if self.port_is_connect:
            self.add_to_log("disconnected")                                                          # write to the log
            self.port_is_connect = False
            self.label_com_port_number.setText('')                         # remove the port number from the info panel
            self.connect_status()                                          # call the connection status update function

    def connect_status(self):
        if not self.status_connected and self.port_is_connect:              # check status (to prevent constant calling
            self.label_arduino_connection_status.setStyleSheet("color: rgb(170, 199, 197);")             # change color
            self.label_arduino_connection_status.setText("read/write")
            self.status_connected = True                                                              # update statuses
            self.status_disconnected = False
        elif not self.port_is_connect:
            if not self.status_disconnected:
                self.label_arduino_connection_status.setStyleSheet("color: rgb(255, 185, 139);")
                self.label_arduino_connection_status.setText("noData")
                self.status_disconnected = True
                self.status_connected = False

    def arduino_encoder(self):                                                                # processing encoder data
        if self.input_data_dict["1"] == "2":                                                           # rotation RIGHT
            if self.radioButton_connect_encoder_to_timer.isChecked():                                   # send to timer
                self.update_timer_value(self.current_timer + 2)
            elif self.radioButton_connect_encoder_to_pwm.isChecked():                                     # send to PWM
                self.horizontalSlider_pwm_duty_cycle.setValue(self.pwm_value + 1)
        elif self.input_data_dict["1"] == "10":                                                # rotation RIGHT PRESSED
            if self.radioButton_connect_encoder_to_timer.isChecked():
                self.update_timer_value(self.current_timer + 10)
            elif self.radioButton_connect_encoder_to_pwm.isChecked():
                self.horizontalSlider_pwm_duty_cycle.setValue(self.pwm_value + 5)
        elif self.input_data_dict["1"] == "-2":                                                         # rotation LEFT
            if self.radioButton_connect_encoder_to_timer.isChecked():
                self.update_timer_value(self.current_timer - 2)
            elif self.radioButton_connect_encoder_to_pwm.isChecked():
                self.horizontalSlider_pwm_duty_cycle.setValue(self.pwm_value - 1)
        elif self.input_data_dict["1"] == "-10":                                                # rotation LEFT PRESSED
            if self.radioButton_connect_encoder_to_timer.isChecked():
                self.update_timer_value(self.current_timer - 10)
            elif self.radioButton_connect_encoder_to_pwm.isChecked():
                self.horizontalSlider_pwm_duty_cycle.setValue(self.pwm_value - 5)
        elif self.input_data_dict["1"] == "99":                                                           # short PRESS
            if self.radioButton_connect_encoder_to_timer.isChecked():
                self.start_timer()
        elif self.input_data_dict["1"] == "00":                                                         # holding PRESS
            if self.radioButton_connect_encoder_to_timer.isChecked():
                self.stop_timer()
        self.input_data_dict["1"] = "0"                                                                    # reset data

    def update_timer_value(self, value):                                           # function to change the timer value
        if value >= 0:
            self.current_timer = value                                                                   # update timer
            self.lcdNumber_relay_timer.display(value)
            self.horizontalSlider_relay_timer_value.setValue(value)                     # set the timer slider position
            # self.ready_to_write = True
            if self.radioButton_symb_disp_show_timer.isChecked():
                self.display_4x7digit()  # display on the screen

    def display_4x7digit(self):
        if self.radioButton_symb_disp_show_clock.isChecked():                                        # displaying clock
            current_time = str(datetime.now())
            self.lcdNumber_symb_disp1.display(current_time[11])                      # distribute datetime across cells
            self.lcdNumber_symb_disp2.display(current_time[12])
            self.lcdNumber_symb_disp3.display(current_time[14])
            self.lcdNumber_symb_disp4.display(current_time[15])
            self.output_data_dict['3'] = current_time[11:13] + current_time[14:16]
            self.ready_to_write = True                                                                  # ready to send
        elif self.radioButton_symb_disp_show_timer.isChecked():                                      # displaying timer
            self.lcdNumber_symb_disp1.display(self.current_timer // 1000 % 10)  # distribute current_timer across cells
            self.lcdNumber_symb_disp2.display(self.current_timer // 100 % 10)
            self.lcdNumber_symb_disp3.display(self.current_timer // 10 % 10)
            self.lcdNumber_symb_disp4.display(self.current_timer % 10)
            self.output_data_dict['3'] = self.current_timer   # update the sending dictionary according to the protocol
            self.ready_to_write = True                                                  # update the status for sending

    def clock_update(self):                                            # clock update function (called in timer thread)
        if self.radioButton_symb_disp_show_clock.isChecked():
            self.display_4x7digit()

    def start_timer(self):
        if self.timer_is_running:                                                            # make the button bistable
            self.stop_timer()                                                    # calling "start" again works as pause
            self.add_to_log(f'timer pause {self.current_timer}s')
        else:
            self.timer_is_running = True                                           # if the timer is off, just start it
            self.timer_thread.start()
            self.add_to_log(f'timer start  {self.current_timer}s')
        if self.radioButton_relay_timer.isChecked():
            self.relay_on()

    def stop_timer(self):
        if not self.timer_is_running:                                                             # if the timer is off
            self.current_timer = 0                                               # the call will act to reset the timer
            self.lcdNumber_relay_timer.display(self.current_timer)
            self.add_to_log('timer cleared')
            self.horizontalSlider_relay_timer_value.setValue(0)
        else:
            self.timer_is_running = False                                                       # stop the timer thread
            self.add_to_log('timer stop')
        self.relay_off()

    def dial_move(self):                                                        # operation of the dial in encoder mode
        value = self.dial_encoder.value()
        if self.radioButton_connect_encoder_to_timer.isChecked():                                  # timer control mode
            if self.current_encoder_position > value:
                self.update_timer_value(self.current_timer - 1)
            else:
                self.update_timer_value(self.current_timer + 1)
            self.current_encoder_position = value
        elif self.radioButton_connect_encoder_to_pwm.isChecked():                                    # PWM control mode
            if self.current_encoder_position > value:
                self.pwm_value -= 1 if self.pwm_value > 1 else 0                          # decrease but not below zero
                self.current_encoder_position = value
            else:
                self.pwm_value += 1 if self.pwm_value < 256 else 0                         # increase but not above 256
                self.current_encoder_position = value
            self.horizontalSlider_pwm_duty_cycle.setValue(self.pwm_value)

    def moisture_sensor(self):                                                   # processing soil moisture sensor data
        self.moisture_value = int(int(self.input_data_dict['2']) / 1024 * 100)                  # values in percentages
        self.progressBar_moisture_level.setValue(self.moisture_value)                              # display the values

    def enable_relay_moisture_sens_level(self, value):              # handling relay trigger according to soil moisture
            self.label_moisture_relay_en_level.setText(f'Watering at {value}%')                         # in percentage

    def rain_detector(self):
        self.rain_detector_value = 100 - int(int(self.input_data_dict['3']) / 1024 * 100)               # in percentage
        self.progressBar_rain_sens_level.setValue(self.rain_detector_value)
        if self.rain_detector_value >= 60:                                                    # cases based on readings
            self.label_rain_sens_status_icon.setPixmap(QtGui.QPixmap(f"{self.current_path}/rain.png"))      # icon file
            self.weather_status = "rainy"
        if self.rain_detector_value <= 20:
            self.label_rain_sens_status_icon.setPixmap(QtGui.QPixmap(f"{self.current_path}/sun.png"))
            self.weather_status = "sunny"
        if self.rain_detector_value > 20 and self.rain_detector_value < 60:
            self.label_rain_sens_status_icon.setPixmap(QtGui.QPixmap(f"{self.current_path}/cloud.png"))
            self.weather_status = "cloudy"

    def matrix_8x8(self):
        self.output_data_dict['4'] = self.textEdit_matrix8x8.toPlainText()
        self.ready_to_write = True                                                                      # ready to send

    def change_pwm_value(self, value):                # handling PWM slider change, adjusting the duty cycle percentage
        self.pwm_value = value
        self.output_data_dict["6"] = self.pwm_value
        self.oscilloscope()                                                         # calling the oscilloscope function
        self.ready_to_write = True                                                                      # ready to send

    def oscilloscope(self):
        self.create_pwm_diagram()
        self.widget_pwm_oscilloscope.clear()
        self.widget_pwm_oscilloscope.plot(self.pwm_times_list, self.pwm_levels_list)

    def create_pwm_diagram(self):                                                                # creating a PWM chart
        self.pwm_times_list = []
        self.pwm_levels_list = []
        for count in range(1280):
            self.pwm_times_list.append(count)
        for _ in range(self.pwm_value):
            self.pwm_levels_list.append(1)
        for _ in range(256 - self.pwm_value):
            self.pwm_levels_list.append(0)
        self.pwm_times_list.append(1280)                                         # decorative additions (not mandatory)
        self.pwm_levels_list *= 5
        self.pwm_levels_list.append(1)

    def lcd1602_cycle(self):                                  # function for cyclic display on the screen (cycle 3sec.)
        message_list = []
        if self.checkBox_i2c1602_show_clock.isChecked():                                                        # clock
            time = str(datetime.now())
            message_list.append("Date " + time[0:11] + "Time  " + time[11:16])
        if self.checkBox_i2c1602_show_log.isChecked():                                                            # log
            message_list.append("log " + self.current_log)
        if self.checkBox_i2c1602_show_moisure.isChecked():                                              # soil moisture
            message_list.append("Moisture sensor level " + str(self.moisture_value) + "%")
        if self.checkBox_i2c1602_show_pwm.isChecked():                                                            # PWM
            message_list.append("Pwm duty cycle        " + str(int(self.pwm_value / 256 * 100 // 1)) + "%")
        if self.checkBox_i2c1602_show_timer.isChecked():                                                        # timer
            message_list.append("Timer             " + str(self.current_timer) + "s")
        if self.checkBox_i2c1602_show_weather.isChecked():                                                    # weather
            message_list.append("The weather is " + self.weather_status)
        if len(message_list) > self.lcd1602_cycle_count:                                         # split into two lines
            self.output_data_dict['1'] = message_list[self.lcd1602_cycle_count][0:15]                      # first line
            self.output_data_dict['2'] = message_list[self.lcd1602_cycle_count][15:]                      # second line
            self.ready_to_write = True
        else:
            self.lcd1602_cycle_count = -1                                                                # reset cycles
        self.lcd1602_cycle_count += 1                                                               # cycle counter + 1

    def send_text_to_lcd1602(self):
        if self.textEdit_i2c1602_send_text.toPlainText():
            message = self.textEdit_i2c1602_send_text.toPlainText()             # get the message from the input window
            self.output_data_dict['1'] = message[0:16]                                           # split into two lines
            if len(message) > 15:
                self.output_data_dict['2'] = message[16:]
            else:
                self.output_data_dict['2'] = ' '
            self.ready_to_write = True                                                                  # ready to send

    def relay_on(self):
        self.output_data_dict['5'] = '0'                                            # add to the dictionary for sending
        self.ready_to_write = True

    def relay_off(self):
        self.output_data_dict['5'] = '1'                                            # add to the dictionary for sending
        self.ready_to_write = True

    def enable_pump(self):
        if self.checkBox_connect_moisture_to_relay.isChecked():
            self.add_to_log('pump relay connected')
        else:
            self.add_to_log('pump relay disconnected')
        self.checkBox_rain_sens_connect_to_relay.setChecked(False)    # prohibit simultaneous operation as a rain relay

    def enable_rain_buzzer(self):
        if self.checkBox_rain_sens_connect_to_relay.isChecked():
            self.add_to_log('buzzer relay connected')
        else:
            self.add_to_log('buzzer relay disconnected')
        self.checkBox_connect_moisture_to_relay.setChecked(False)  # prohibit simultaneous operation as a watering pump

    def add_to_log(self, item):                                                                  # log writing function
        if self.logs_count > 0:                                                             # cut logs at program start
            self.current_log = str(datetime.now())[11:19] + ' - ' + item
            self.listWidget.insertItem(0, self.current_log)
        self.logs_count += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
