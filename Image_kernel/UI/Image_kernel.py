# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_kernel.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_mw_kernel(object):
    def setupUi(self, mw_kernel):
        if not mw_kernel.objectName():
            mw_kernel.setObjectName(u"mw_kernel")
        mw_kernel.resize(622, 387)
        self.verticalLayout = QVBoxLayout(mw_kernel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tw_kernel = QTabWidget(mw_kernel)
        self.tw_kernel.setObjectName(u"tw_kernel")
        self.tw_kernel.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.tv_3x3 = QTableView(self.tab)
        self.tv_3x3.setObjectName(u"tv_3x3")
        self.tv_3x3.horizontalHeader().setCascadingSectionResizes(False)
        self.tv_3x3.horizontalHeader().setMinimumSectionSize(50)
        self.tv_3x3.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_4.addWidget(self.tv_3x3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(40, 0))
        self.label_11.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_6.addWidget(self.label_11)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(40, 0))
        self.label_10.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_6.addWidget(self.label_10)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.dsb_scale_kernel_3x3 = QDoubleSpinBox(self.tab)
        self.dsb_scale_kernel_3x3.setObjectName(u"dsb_scale_kernel_3x3")
        self.dsb_scale_kernel_3x3.setMinimumSize(QSize(70, 0))
        self.dsb_scale_kernel_3x3.setMaximumSize(QSize(70, 16777215))
        self.dsb_scale_kernel_3x3.setDecimals(4)
        self.dsb_scale_kernel_3x3.setMinimum(-1000.000000000000000)
        self.dsb_scale_kernel_3x3.setMaximum(1000.000000000000000)
        self.dsb_scale_kernel_3x3.setSingleStep(0.010000000000000)

        self.verticalLayout_8.addWidget(self.dsb_scale_kernel_3x3)

        self.dsb_offset_kernel_3x3 = QDoubleSpinBox(self.tab)
        self.dsb_offset_kernel_3x3.setObjectName(u"dsb_offset_kernel_3x3")
        self.dsb_offset_kernel_3x3.setMinimumSize(QSize(60, 0))
        self.dsb_offset_kernel_3x3.setMaximumSize(QSize(60, 16777215))
        self.dsb_offset_kernel_3x3.setLayoutDirection(Qt.LeftToRight)
        self.dsb_offset_kernel_3x3.setDecimals(0)
        self.dsb_offset_kernel_3x3.setMinimum(-255.000000000000000)
        self.dsb_offset_kernel_3x3.setMaximum(255.000000000000000)

        self.verticalLayout_8.addWidget(self.dsb_offset_kernel_3x3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.pb_apply_kernel_3x3 = QPushButton(self.tab)
        self.pb_apply_kernel_3x3.setObjectName(u"pb_apply_kernel_3x3")
        self.pb_apply_kernel_3x3.setEnabled(True)
        self.pb_apply_kernel_3x3.setMinimumSize(QSize(40, 0))
        self.pb_apply_kernel_3x3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.pb_apply_kernel_3x3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addLayout(self.verticalLayout_4)

        self.tw_kernel.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_5.addWidget(self.label_12)

        self.tv_5x5 = QTableView(self.tab_2)
        self.tv_5x5.setObjectName(u"tv_5x5")

        self.verticalLayout_5.addWidget(self.tv_5x5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(40, 0))
        self.label_14.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_2.addWidget(self.label_14)

        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(40, 0))
        self.label_13.setMaximumSize(QSize(40, 16777215))

        self.verticalLayout_2.addWidget(self.label_13)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dsb_scale_kernel_5x5 = QDoubleSpinBox(self.tab_2)
        self.dsb_scale_kernel_5x5.setObjectName(u"dsb_scale_kernel_5x5")
        self.dsb_scale_kernel_5x5.setMinimumSize(QSize(70, 0))
        self.dsb_scale_kernel_5x5.setMaximumSize(QSize(70, 16777215))
        self.dsb_scale_kernel_5x5.setDecimals(4)
        self.dsb_scale_kernel_5x5.setSingleStep(0.010000000000000)

        self.verticalLayout_3.addWidget(self.dsb_scale_kernel_5x5)

        self.dsb_offset_kernel_5x5 = QDoubleSpinBox(self.tab_2)
        self.dsb_offset_kernel_5x5.setObjectName(u"dsb_offset_kernel_5x5")
        self.dsb_offset_kernel_5x5.setMinimumSize(QSize(60, 0))
        self.dsb_offset_kernel_5x5.setMaximumSize(QSize(60, 16777215))
        self.dsb_offset_kernel_5x5.setDecimals(0)
        self.dsb_offset_kernel_5x5.setMinimum(-255.000000000000000)
        self.dsb_offset_kernel_5x5.setMaximum(255.000000000000000)

        self.verticalLayout_3.addWidget(self.dsb_offset_kernel_5x5)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.pb_apply_kernel_5x5 = QPushButton(self.tab_2)
        self.pb_apply_kernel_5x5.setObjectName(u"pb_apply_kernel_5x5")
        self.pb_apply_kernel_5x5.setEnabled(True)
        self.pb_apply_kernel_5x5.setMinimumSize(QSize(50, 0))
        self.pb_apply_kernel_5x5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.pb_apply_kernel_5x5)

        self.horizontalLayout_8.setStretch(2, 60)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.tw_kernel.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tw_kernel)


        self.retranslateUi(mw_kernel)

        self.tw_kernel.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mw_kernel)
    # setupUi

    def retranslateUi(self, mw_kernel):
        mw_kernel.setWindowTitle(QCoreApplication.translate("mw_kernel", u"Kernel", None))
        self.label_7.setText(QCoreApplication.translate("mw_kernel", u"kernel matrix:", None))
        self.label_11.setText(QCoreApplication.translate("mw_kernel", u"scale:", None))
        self.label_10.setText(QCoreApplication.translate("mw_kernel", u"offset:", None))
        self.pb_apply_kernel_3x3.setText(QCoreApplication.translate("mw_kernel", u"Apply", None))
        self.tw_kernel.setTabText(self.tw_kernel.indexOf(self.tab), QCoreApplication.translate("mw_kernel", u"3x3", None))
        self.label_12.setText(QCoreApplication.translate("mw_kernel", u"kernel matrix:", None))
        self.label_14.setText(QCoreApplication.translate("mw_kernel", u"scale", None))
        self.label_13.setText(QCoreApplication.translate("mw_kernel", u"offset:", None))
        self.pb_apply_kernel_5x5.setText(QCoreApplication.translate("mw_kernel", u"Apply", None))
        self.tw_kernel.setTabText(self.tw_kernel.indexOf(self.tab_2), QCoreApplication.translate("mw_kernel", u"5x5", None))
    # retranslateUi

