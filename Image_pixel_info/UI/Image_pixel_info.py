# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_pixel_info.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_mw_image_pixel_info(object):
    def setupUi(self, mw_image_pixel_info):
        if not mw_image_pixel_info.objectName():
            mw_image_pixel_info.setObjectName(u"mw_image_pixel_info")
        mw_image_pixel_info.resize(251, 255)
        self.verticalLayout = QVBoxLayout(mw_image_pixel_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tv_image_pixel_info = QTableView(mw_image_pixel_info)
        self.tv_image_pixel_info.setObjectName(u"tv_image_pixel_info")

        self.verticalLayout.addWidget(self.tv_image_pixel_info)


        self.retranslateUi(mw_image_pixel_info)

        QMetaObject.connectSlotsByName(mw_image_pixel_info)
    # setupUi

    def retranslateUi(self, mw_image_pixel_info):
        mw_image_pixel_info.setWindowTitle(QCoreApplication.translate("mw_image_pixel_info", u"Image pixel info", None))
    # retranslateUi

