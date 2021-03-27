from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main import *
import numpy as np


class Multi_Polinom():
    def __init__(self):
        #Initialization variables
        self.numbers_actions = ui.comboBox
        self.field_one = ui.comboBox_2
        self.field_two = ui.comboBox_3
        self.line = ui.lineEdit

    def Add_elements(self):# Function add elements from 1 to 3 combobox
        self.value_of_actions = ["1", "2"]
        self.actions = ["1011", "1101"]
        self.numbers_actions.addItems(self.value_of_actions)
        self.field_one.addItems(self.actions)
        self.field_two.addItems(self.actions)
        self.field_two.setDisabled(True)#disable 3 combobox

    def Switch(self):#Function switching disable 3 combobox
        if(self.numbers_actions.currentIndex() == 0):
            self.field_two.setDisabled(True)
        elif(self.numbers_actions.currentIndex() == 1):
            self.field_two.setDisabled(False)

    def Multiplay(self):#Function multiplay
        self.x = self.field_one.currentText()#take text from combobox
        self.y = self.field_two.currentText()
        self.arr_x = list(self.x)#transform string to list
        self.arr_y = list(self.y)
        for i in range(len(self.arr_x)):#every elemnts list's transform from str to int
            self.arr_x[i] = int(self.arr_x[i])

        self.arr1 = np.array(self.arr_x)#write new arr(int)
        for i in range(len(self.arr_y)):
            self.arr_y[i] = int(self.arr_y[i])
        self.arr_y.reverse()#reverse list for corect multiplay
        self.arr2 = np.array(self.arr_y)
        self.res_arr = []#create empty arr
        for item in self.arr2:#multiplay every elemnt from arr1 on every element in arr2
            self.res = self.arr1 * item
            self.res_arr.append(self.res)#append result to empty arr

        self.array = np.array([self.res_arr])#transform from list to ndarray
        self.zero = np.zeros((7, 7), dtype=int)#create zero matrix
        self.zero[0:1, 3:7] = np.array(self.array[0, 0]) #вставка по оси У, по оси Х. Тоесть от первой строки до второй строки!!!!!
        self.zero[1:2, 2:6] = np.array(self.array[0, 1])
        self.zero[2:3, 1:5] = np.array(self.array[0, 2])
        self.zero[3:4, 0:4] = np.array(self.array[0, 3])
        #print(self.zero)
        self.result = np.sum(self.zero, axis=0)#sum arr on vertical
        for i in range(len(self.result)):#transform on module 2
            if(self.result[i] % 2 == 0):
                self.result[i] = 0
            else:
                self.result[i] = 1
        #print(self.result)
        self.z = [str(c) for c in self.result]#transform every elemnts from int to str
        self.s = "".join(self.z)#transform arr in str
        self.line.setText(self.s)#write result ot lineEdit
        #print(self.z)

    def Calc(self):#function detect which index current in 1 combobox
        if(self.numbers_actions.currentIndex() == 0):
            self.line.setText(self.field_one.currentText())
        elif(self.numbers_actions.currentIndex() == 1):
            self.Multiplay()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    polinom = Multi_Polinom()
    drop_box = ui.comboBox
    btn = ui.pushButton
    polinom.Add_elements()
    drop_box.currentIndexChanged.connect(polinom.Switch)#detect switching in 1 combobox
    btn.clicked.connect(polinom.Calc)

    sys.exit(app.exec_())

'''app = QtWidgets.QApplication(sys.argv)    

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

#Inizialization variables
numbers_actions = ui.comboBox
field_one = ui.comboBox_2
field_two = ui.comboBox_3
value_of_actions = ["1", "2"]
actions = ["1011", "1101"]
#Set actions
numbers_actions.addItems(value_of_actions)
field_one.addItems(actions)
field_two.addItems(actions)
field_two.setDisabled(True)

#Function switched disabled beetwen field
def Switch_num():
    if(numbers_actions.currentIndex() == 0):
        field_two.setDisabled(True)
    elif(numbers_actions.currentIndex() == 1):
        field_two.setDisabled(False)
        

numbers_actions.currentIndexChanged.connect(Switch_num)

sys.exit(app.exec_())'''
