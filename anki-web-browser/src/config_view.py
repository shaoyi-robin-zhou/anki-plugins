# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/config_view.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfigView(object):
    def setupUi(self, ConfigView):
        ConfigView.setObjectName("ConfigView")
        ConfigView.setWindowModality(QtCore.Qt.ApplicationModal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(ConfigView.sizePolicy().hasHeightForWidth())
        ConfigView.setSizePolicy(sizePolicy)
        ConfigView.resize(510, 540)
        ConfigView.setFixedSize(510, 540)
        # ConfigView.setMinimumSize(QtCore.QSize(0, 0))
        # ConfigView.setMaximumSize(QtCore.QSize(1000, 1000))
        ConfigView.setAutoFillBackground(True)
        ConfigView.setStyleSheet("")
        ConfigView.setSizeGripEnabled(False)
        self.verticalLayWidget = QtWidgets.QWidget(ConfigView)
        self.verticalLayWidget.setGeometry(QtCore.QRect(0, 0, 510, 540))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.verticalLayWidget.sizePolicy().hasHeightForWidth())
        self.verticalLayWidget.setSizePolicy(sizePolicy)
        self.verticalLayWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayWidget.setObjectName("verticalLayWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.verticalLayWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 475, 520))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbProviders = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbProviders.setObjectName("lbProviders")
        self.verticalLayout.addWidget(self.lbProviders)
        self.tbProviders = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbProviders.sizePolicy().hasHeightForWidth())
        self.tbProviders.setSizePolicy(sizePolicy)
        self.tbProviders.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText)
        self.tbProviders.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbProviders.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbProviders.setColumnCount(2)
        self.tbProviders.setObjectName("tbProviders")
        self.tbProviders.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbProviders.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbProviders.setHorizontalHeaderItem(1, item)
        self.tbProviders.horizontalHeader().setStretchLastSection(True)
        self.tbProviders.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tbProviders)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(100, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btProviderUp = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btProviderUp.setObjectName("btProviderUp")
        self.horizontalLayout.addWidget(self.btProviderUp)
        self.btProviderDown = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btProviderDown.setObjectName("btProviderDown")
        self.horizontalLayout.addWidget(self.btProviderDown)
        self.btSortProvider = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btSortProvider.setObjectName("btSortProvider")
        self.horizontalLayout.addWidget(self.btSortProvider)
        self.btRemove = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btRemove.setObjectName("btRemove")
        self.horizontalLayout.addWidget(self.btRemove)
        self.btAdd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btAdd.setObjectName("btAdd")
        self.horizontalLayout.addWidget(self.btAdd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.cbSystemBrowser = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cbSystemBrowser.setObjectName("cbSystemBrowser")
        self.verticalLayout.addWidget(self.cbSystemBrowser)
        self.browserInfo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.browserInfo.setStyleSheet("QLabel  {\n"
"color: rgb(255, 0, 0);\n"
"}")
        self.browserInfo.setObjectName("browserInfo")
        self.verticalLayout.addWidget(self.browserInfo)
        self.rbKeepOpened = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.rbKeepOpened.setObjectName("rbKeepOpened")
        self.verticalLayout.addWidget(self.rbKeepOpened)
        self.rbOnTop = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.rbOnTop.setObjectName("rbOnTop")
        self.verticalLayout.addWidget(self.rbOnTop)
        self.bottomInfo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.bottomInfo.setStyleSheet("QLabel  {\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.bottomInfo.setObjectName("bottomInfo")
        self.verticalLayout.addWidget(self.bottomInfo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbWordFilter = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbWordFilter.setObjectName("lbWordFilter")
        self.horizontalLayout_2.addWidget(self.lbWordFilter)
        self.teWordFilter = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.teWordFilter.setMaximumSize(QtCore.QSize(300, 16777215))
        self.teWordFilter.setObjectName("teWordFilter")
        self.horizontalLayout_2.addWidget(self.teWordFilter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.lbShortcut = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbShortcut.setObjectName("lbShortcut")
        self.verticalLayout.addWidget(self.lbShortcut)
        self.horizontalLayoutShortcuts = QtWidgets.QHBoxLayout()
        self.horizontalLayoutShortcuts.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayoutShortcuts.setObjectName("horizontalLayoutShortcuts")
        self.verticalLayMenu = QtWidgets.QVBoxLayout()
        self.verticalLayMenu.setObjectName("verticalLayMenu")
        self.lbShortMenu = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbShortMenu.setObjectName("lbShortMenu")
        self.verticalLayMenu.addWidget(self.lbShortMenu)
        self.teShortcutMenu = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.teShortcutMenu.setMaximumSize(QtCore.QSize(180, 16777215))
        self.teShortcutMenu.setObjectName("teShortcutMenu")
        self.verticalLayMenu.addWidget(self.teShortcutMenu)
        self.horizontalLayoutShortcuts.addLayout(self.verticalLayMenu)
        self.verticalLayRepeat = QtWidgets.QVBoxLayout()
        self.verticalLayRepeat.setObjectName("verticalLayRepeat")
        self.lbShortRepeat = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbShortRepeat.setObjectName("lbShortRepeat")
        self.verticalLayRepeat.addWidget(self.lbShortRepeat)
        self.teShortcutRepeat = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.teShortcutRepeat.setMaximumSize(QtCore.QSize(180, 16777215))
        self.teShortcutRepeat.setObjectName("teShortcutRepeat")
        self.verticalLayRepeat.addWidget(self.teShortcutRepeat)
        self.horizontalLayoutShortcuts.addLayout(self.verticalLayRepeat)
        self.verticalLayout.addLayout(self.horizontalLayoutShortcuts)
        self.btActionsBox = QtWidgets.QHBoxLayout()
        self.btActionsBox.setContentsMargins(200, -1, -1, -1)
        self.btActionsBox.setSpacing(7)
        self.btActionsBox.setObjectName("btActionsBox")
        self.btSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btSave.setObjectName("btSave")
        self.btActionsBox.addWidget(self.btSave)
        self.btCancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btCancel.setObjectName("btCancel")
        self.btActionsBox.addWidget(self.btCancel)
        self.verticalLayout.addLayout(self.btActionsBox)

        self.retranslateUi(ConfigView)
        QtCore.QMetaObject.connectSlotsByName(ConfigView)

    def retranslateUi(self, ConfigView):
        _translate = QtCore.QCoreApplication.translate
        ConfigView.setWindowTitle(_translate("ConfigView", "Web Browser Config"))
        self.lbProviders.setText(_translate("ConfigView", "Providers"))
        item = self.tbProviders.horizontalHeaderItem(0)
        item.setText(_translate("ConfigView", "Name"))
        item = self.tbProviders.horizontalHeaderItem(1)
        item.setText(_translate("ConfigView", "URL"))
        self.btProviderUp.setText(_translate("ConfigView", "Up"))
        self.btProviderDown.setText(_translate("ConfigView", "Down"))
        self.btSortProvider.setText(_translate("ConfigView", "Sort"))
        self.btRemove.setText(_translate("ConfigView", "Remove"))
        self.btAdd.setText(_translate("ConfigView", "&Add"))
        self.cbSystemBrowser.setText(_translate("ConfigView", "Use System Browser (instead of Anki-Web-Browser)"))
        self.browserInfo.setText(_translate("ConfigView", "Importing features won\'t work for external browsers"))
        self.rbKeepOpened.setText(_translate("ConfigView", "Keep browser opened (after current card is changed)"))
        self.rbOnTop.setText(_translate("ConfigView", "Keep always visible (on top)"))
        self.bottomInfo.setText(_translate("ConfigView", "It may be necessary to restart Anki to apply the changes"))
        self.lbWordFilter.setText(_translate("ConfigView", "Filter following words: "))
        self.lbShortcut.setText(_translate("ConfigView", "Shortcuts"))
        self.lbShortMenu.setText(_translate("ConfigView", "Show Web Browser menu"))
        self.lbShortRepeat.setText(_translate("ConfigView", "Search again, repeating last provider"))
        self.btSave.setText(_translate("ConfigView", "&Save"))
        self.btCancel.setText(_translate("ConfigView", "&Cancel"))
