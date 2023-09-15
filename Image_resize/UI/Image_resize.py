# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_resize.ui'
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

class Ui_mw_image_resize(object):
    def setupUi(self, mw_image_resize):
        if not mw_image_resize.objectName():
            mw_image_resize.setObjectName(u"mw_image_resize")
        mw_image_resize.resize(282, 218)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mw_image_resize.sizePolicy().hasHeightForWidth())
        mw_image_resize.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(mw_image_resize)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(mw_image_resize)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 280, 216))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tv_image_resize = QTableView(self.scrollAreaWidgetContents)
        self.tv_image_resize.setObjectName(u"tv_image_resize")
        sizePolicy.setHeightForWidth(self.tv_image_resize.sizePolicy().hasHeightForWidth())
        self.tv_image_resize.setSizePolicy(sizePolicy)
        self.tv_image_resize.setMinimumSize(QSize(0, 0))
        self.tv_image_resize.setLineWidth(1)
        self.tv_image_resize.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tv_image_resize.setSortingEnabled(False)
        self.tv_image_resize.horizontalHeader().setVisible(False)
        self.tv_image_resize.horizontalHeader().setMinimumSectionSize(19)
        self.tv_image_resize.horizontalHeader().setDefaultSectionSize(100)
        self.tv_image_resize.horizontalHeader().setHighlightSections(True)
        self.tv_image_resize.verticalHeader().setVisible(False)
        self.tv_image_resize.verticalHeader().setHighlightSections(True)

        self.verticalLayout_2.addWidget(self.tv_image_resize)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(mw_image_resize)

        QMetaObject.connectSlotsByName(mw_image_resize)
    # setupUi

    def retranslateUi(self, mw_image_resize):
        mw_image_resize.setWindowTitle(QCoreApplication.translate("mw_image_resize", u"Image resize", None))
    # retranslateUi

