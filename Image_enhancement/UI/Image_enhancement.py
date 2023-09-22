# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_enhancement.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_mw_enhance_image(object):
    def setupUi(self, mw_enhance_image):
        if not mw_enhance_image.objectName():
            mw_enhance_image.setObjectName(u"mw_enhance_image")
        mw_enhance_image.resize(374, 351)
        self.verticalLayout_5 = QVBoxLayout(mw_enhance_image)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(mw_enhance_image)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hs_color = QSlider(mw_enhance_image)
        self.hs_color.setObjectName(u"hs_color")
        self.hs_color.setMinimumSize(QSize(200, 0))
        self.hs_color.setMaximumSize(QSize(150, 16777215))
        self.hs_color.setMaximum(100)
        self.hs_color.setSingleStep(1)
        self.hs_color.setValue(100)
        self.hs_color.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.hs_color)

        self.dsb_color = QDoubleSpinBox(mw_enhance_image)
        self.dsb_color.setObjectName(u"dsb_color")
        self.dsb_color.setMinimumSize(QSize(50, 0))
        self.dsb_color.setMaximumSize(QSize(50, 16777215))
        self.dsb_color.setMaximum(1.000000000000000)
        self.dsb_color.setSingleStep(0.010000000000000)
        self.dsb_color.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.dsb_color)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_color = QPushButton(mw_enhance_image)
        self.pb_color.setObjectName(u"pb_color")

        self.horizontalLayout.addWidget(self.pb_color)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 30)
        self.verticalLayout_2.setStretch(1, 70)

        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.line = QFrame(mw_enhance_image)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(mw_enhance_image)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hs_contrast = QSlider(mw_enhance_image)
        self.hs_contrast.setObjectName(u"hs_contrast")
        self.hs_contrast.setMinimumSize(QSize(200, 0))
        self.hs_contrast.setMaximumSize(QSize(150, 16777215))
        self.hs_contrast.setMaximum(200)
        self.hs_contrast.setSingleStep(1)
        self.hs_contrast.setValue(100)
        self.hs_contrast.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.hs_contrast)

        self.dsb_contrast = QDoubleSpinBox(mw_enhance_image)
        self.dsb_contrast.setObjectName(u"dsb_contrast")
        self.dsb_contrast.setMinimumSize(QSize(50, 0))
        self.dsb_contrast.setMaximumSize(QSize(50, 16777215))
        self.dsb_contrast.setMaximum(2.000000000000000)
        self.dsb_contrast.setSingleStep(0.010000000000000)
        self.dsb_contrast.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.dsb_contrast)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pb_contrast = QPushButton(mw_enhance_image)
        self.pb_contrast.setObjectName(u"pb_contrast")

        self.horizontalLayout_2.addWidget(self.pb_contrast)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 30)
        self.verticalLayout.setStretch(1, 70)

        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.line_2 = QFrame(mw_enhance_image)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(mw_enhance_image)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(70, 0))

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.hs_brightness = QSlider(mw_enhance_image)
        self.hs_brightness.setObjectName(u"hs_brightness")
        self.hs_brightness.setMinimumSize(QSize(200, 0))
        self.hs_brightness.setMaximumSize(QSize(150, 16777215))
        self.hs_brightness.setMaximum(500)
        self.hs_brightness.setSingleStep(1)
        self.hs_brightness.setValue(100)
        self.hs_brightness.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.hs_brightness)

        self.dsb_brightness = QDoubleSpinBox(mw_enhance_image)
        self.dsb_brightness.setObjectName(u"dsb_brightness")
        self.dsb_brightness.setMinimumSize(QSize(50, 0))
        self.dsb_brightness.setMaximumSize(QSize(50, 16777215))
        self.dsb_brightness.setMaximum(5.000000000000000)
        self.dsb_brightness.setSingleStep(0.010000000000000)
        self.dsb_brightness.setValue(1.000000000000000)

        self.horizontalLayout_4.addWidget(self.dsb_brightness)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pb_brightness = QPushButton(mw_enhance_image)
        self.pb_brightness.setObjectName(u"pb_brightness")

        self.horizontalLayout_4.addWidget(self.pb_brightness)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 30)
        self.verticalLayout_3.setStretch(1, 70)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.line_3 = QFrame(mw_enhance_image)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(mw_enhance_image)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(70, 0))

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.hs_sharpness = QSlider(mw_enhance_image)
        self.hs_sharpness.setObjectName(u"hs_sharpness")
        self.hs_sharpness.setMinimumSize(QSize(200, 0))
        self.hs_sharpness.setMaximumSize(QSize(150, 16777215))
        self.hs_sharpness.setMaximum(200)
        self.hs_sharpness.setSingleStep(1)
        self.hs_sharpness.setValue(100)
        self.hs_sharpness.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.hs_sharpness)

        self.dsb_sharpness = QDoubleSpinBox(mw_enhance_image)
        self.dsb_sharpness.setObjectName(u"dsb_sharpness")
        self.dsb_sharpness.setMinimumSize(QSize(50, 0))
        self.dsb_sharpness.setMaximumSize(QSize(50, 16777215))
        self.dsb_sharpness.setMaximum(2.000000000000000)
        self.dsb_sharpness.setSingleStep(0.010000000000000)
        self.dsb_sharpness.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.dsb_sharpness)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pb_sharpness = QPushButton(mw_enhance_image)
        self.pb_sharpness.setObjectName(u"pb_sharpness")

        self.horizontalLayout_3.addWidget(self.pb_sharpness)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_4.setStretch(0, 30)
        self.verticalLayout_4.setStretch(1, 70)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.retranslateUi(mw_enhance_image)

        QMetaObject.connectSlotsByName(mw_enhance_image)
    # setupUi

    def retranslateUi(self, mw_enhance_image):
        mw_enhance_image.setWindowTitle(QCoreApplication.translate("mw_enhance_image", u"Enhancement window", None))
        self.label.setText(QCoreApplication.translate("mw_enhance_image", u"Color", None))
        self.pb_color.setText(QCoreApplication.translate("mw_enhance_image", u"Apply", None))
        self.label_2.setText(QCoreApplication.translate("mw_enhance_image", u"Contrast", None))
        self.pb_contrast.setText(QCoreApplication.translate("mw_enhance_image", u"Apply", None))
        self.label_3.setText(QCoreApplication.translate("mw_enhance_image", u"Brightness", None))
        self.pb_brightness.setText(QCoreApplication.translate("mw_enhance_image", u"Apply", None))
        self.label_4.setText(QCoreApplication.translate("mw_enhance_image", u"Sharpness", None))
        self.pb_sharpness.setText(QCoreApplication.translate("mw_enhance_image", u"Apply", None))
    # retranslateUi

