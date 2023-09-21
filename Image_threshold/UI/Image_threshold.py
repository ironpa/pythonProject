# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_threshold.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_mw_image_threshold(object):
    def setupUi(self, mw_image_threshold):
        if not mw_image_threshold.objectName():
            mw_image_threshold.setObjectName(u"mw_image_threshold")
        mw_image_threshold.resize(350, 85)
        mw_image_threshold.setMinimumSize(QSize(350, 85))
        mw_image_threshold.setMaximumSize(QSize(350, 85))
        self.verticalLayout = QVBoxLayout(mw_image_threshold)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_treshold = QLabel(mw_image_threshold)
        self.lb_treshold.setObjectName(u"lb_treshold")

        self.verticalLayout.addWidget(self.lb_treshold)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hs_treshold = QSlider(mw_image_threshold)
        self.hs_treshold.setObjectName(u"hs_treshold")
        self.hs_treshold.setMinimumSize(QSize(0, 25))
        self.hs_treshold.setMaximum(255)
        self.hs_treshold.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.hs_treshold)

        self.sb_treshold = QSpinBox(mw_image_threshold)
        self.sb_treshold.setObjectName(u"sb_treshold")
        self.sb_treshold.setMinimumSize(QSize(50, 25))
        self.sb_treshold.setMaximum(255)

        self.horizontalLayout.addWidget(self.sb_treshold)

        self.pb_apply_treshold = QPushButton(mw_image_threshold)
        self.pb_apply_treshold.setObjectName(u"pb_apply_treshold")
        self.pb_apply_treshold.setEnabled(True)
        self.pb_apply_treshold.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.pb_apply_treshold)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(mw_image_threshold)

        QMetaObject.connectSlotsByName(mw_image_threshold)
    # setupUi

    def retranslateUi(self, mw_image_threshold):
        mw_image_threshold.setWindowTitle(QCoreApplication.translate("mw_image_threshold", u"Set threshold", None))
        self.lb_treshold.setText(QCoreApplication.translate("mw_image_threshold", u"Threshold setting:", None))
        self.pb_apply_treshold.setText(QCoreApplication.translate("mw_image_threshold", u"Apply", None))
    # retranslateUi

