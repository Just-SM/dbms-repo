# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cr.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Create_Table(object):

    def __init__(self,data):

        self.data = data
        self.colNum = -1
        self.dataList = []
        super().__init__()

        


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 285)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableLine = QtWidgets.QLineEdit(Dialog)
        self.tableLine.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tableLine.setObjectName("tableLine")
        self.tableLine.setPlaceholderText("table name")
        self.gridLayout.addWidget(self.tableLine, 0, 0, 1, 1)
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 7, 0, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 7, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 3, 1, 1)
  
        self.bindButtons(Dialog)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(lambda :self.updateData(Dialog)) 
        self.buttonBox.rejected.connect(Dialog.reject) 
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def updateData(self, Dial):
        temp = ""
        for col in self.dataList:
            temp += col[1].text() + " "
            temp += col[2].currentText() + "  "
            if col[2].currentText() == "varchar" or col[2].currentText() == "char":
                temp = temp[:-1]+"("+col[3].text()+") ,"
            if col[4].isChecked():
                temp = temp[:-1]+"NOT NULL  ,\n"
            else:
                temp = temp[:-1]+"NULL  ,\n"
            if col[5].isChecked():
                temp = temp[:-3]+"UNIQUE ,\n"

            



        self.data.createNewTable(self.data.cursor,self.tableLine.text(),temp[:-3])
        Dial.accept()


    def addOneColumn(self,Dialog):
        
        self.colNum += 1

        label = QtWidgets.QLabel(Dialog)
        label.setMaximumSize(QtCore.QSize(200, 20))
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("label")
        self.gridLayout.addWidget(label, 1, self.colNum , 1, 1)

        lineEdit = QtWidgets.QLineEdit(Dialog)
        lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        lineEdit.setObjectName("lineEdit")
        lineEdit.setPlaceholderText("column name")
        self.gridLayout.addWidget(lineEdit, 2, self.colNum , 1, 1)


        comboBox = QtWidgets.QComboBox(Dialog)
        comboBox.setObjectName("comboBox")
        comboBox.addItem("varchar")
        comboBox.addItem("char")
        comboBox.addItem("serial")
        comboBox.addItem("int")
        comboBox.addItem("boolean")
        comboBox.addItem("float4")
        self.gridLayout.addWidget(comboBox, 3, self.colNum , 1, 1)


        lineEdit2 = QtWidgets.QLineEdit(Dialog)
        lineEdit2.setMaximumSize(QtCore.QSize(200, 16777215))
        lineEdit2.setObjectName("lineEdit2")
        lineEdit2.setPlaceholderText("var lenght")
        self.gridLayout.addWidget(lineEdit2, 4, self.colNum , 1, 1)

        checkBox = QtWidgets.QCheckBox(Dialog)
        checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(checkBox, 5, self.colNum , 1, 1)
        
        checkBox_2 = QtWidgets.QCheckBox(Dialog)
        checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(checkBox_2, 6, self.colNum , 1, 1)
        

        checkBox.setText("Not NULL")
        checkBox_2.setText("UNIQUE")
        label.setText("Column: " + str(self.colNum))
        self.dataList.append((label,lineEdit,comboBox,lineEdit2,checkBox,checkBox_2))



    def delLastCol(self):

        if self.colNum > -1:

            self.gridLayout.removeWidget(self.dataList[self.colNum][0])
            self.gridLayout.removeWidget(self.dataList[self.colNum][1])
            self.gridLayout.removeWidget(self.dataList[self.colNum][2])
            self.gridLayout.removeWidget(self.dataList[self.colNum][3])
            self.gridLayout.removeWidget(self.dataList[self.colNum][4])
            self.gridLayout.removeWidget(self.dataList[self.colNum][5])

            self.dataList.pop(self.colNum)
            self.colNum -= 1





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
       
        self.addButton.setText(_translate("Dialog", "Add column"))

        self.deleteButton.setText(_translate("Dialog", "Delete"))
    

    def bindButtons(self,Dialog):
        self.addButton.clicked.connect(lambda : self.addOneColumn(Dialog))
        self.deleteButton.clicked.connect(self.delLastCol)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Create_Table(1)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())