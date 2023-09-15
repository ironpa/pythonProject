# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_info.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHeaderView, QScrollArea,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_mw_image_info(object):
    def setupUi(self, mw_image_info):
        if not mw_image_info.objectName():
            mw_image_info.setObjectName(u"mw_image_info")
        mw_image_info.resize(393, 309)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mw_image_info.sizePolicy().hasHeightForWidth())
        mw_image_info.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(mw_image_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(mw_image_info)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 391, 307))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView = QTableView(self.scrollAreaWidgetContents)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.verticalLayout_2.addWidget(self.tableView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(mw_image_info)

        QMetaObject.connectSlotsByName(mw_image_info)
    # setupUi

    def retranslateUi(self, mw_image_info):
        mw_image_info.setWindowTitle(QCoreApplication.translate("mw_image_info", u"Image info", None))
    # retranslateUi

