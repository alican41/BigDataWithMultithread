import timeit
from PyQt5.QtWidgets import *
from gui1_python import Ui_MainWindow
import pandas as pd
from PyQt5.QtCore import QRunnable, QThreadPool

class firstPage(QMainWindow):
    a = ""
    b = ""
    def __init__(self):
        super().__init__()
        self.firstform = Ui_MainWindow()
        self.firstform.setupUi(self)
        self.firstform.hesapla1Button.clicked.connect(self.hesapla1)
        self.firstform.hesapla2Button.clicked.connect(self.hesapla2)
        self.start = timeit.default_timer()


    def similarity(self, list1, list2):
        isize = len(list1)
        isize1 = len(list2)

        if isize > isize1:
            uks = isize
        else:
            uks = isize1

        list_same = [i for i in list1 if i in list1 and i in list2]
        list_same1 = [i for i in list2 if i in list1 and i in list2]
        size1 = len(list_same)
        size2 = len(list_same1)

        if size1 > size2:
            bks = size1
        else:
            bks = size2

        borani = (bks / uks) * 100

        return borani

    def benzerlik1(self, a, k):
        data = pd.read_csv("result5.csv")
        row = 0
        s1 = list()
        s2 = list()
        j = 0
        i = j + 1
        for j in range(100):
            s1 = str(data[f"{a}"][j]).split()
            for i in range(1000):
                s2 = str(data[f"{a}"][i]).split()
                d1 = self.similarity(s1, s2)
                if d1 > float(k):
                    self.firstform.tableWidget.setItem(row, 0, QTableWidgetItem(
                        str(str(d1) + "-" + data[f"{a}"][j] + "-" + data[f"{a}"][i])))
                    row = row + 1
                    # print(str(d1) + "-" + data['Product'][j] + "-" + data['Product'][i])

    def benzerlik2(self, a, b, k):
        data = pd.read_csv("result5.csv")
        s1 = list()
        s2 = list()
        row = 0
        j = 0
        i = j + 1
        for j in range(100):
            s1 = str(data[f"{a}"][j]).split()
            s3 = str(data[f"{b}"][j]).split()
            for i in range(100):

                s2 = str(data[f"{a}"][i]).split()
                s4 = str(data[f"{b}"][j]).split()
                d1 = self.similarity(s1, s2)
                if d1 == 100:
                    d2 = self.similarity(s3, s4)
                    if d2 > k:
                        self.firstform.tableWidget.setItem(row, 0, QTableWidgetItem(
                            str(data['Company'][j] + "-" + data['Company'][i])))
                        row = row + 1
                    # print(str(d2) + "-" + data[f"{b}"][j] + "-" + data[f"{b}"][i])

    def benzerlik3(self, a):
        data = pd.read_csv("result5.csv")
        s1 = list()
        s2 = list()
        i = 0
        j = 0
        row = 0
        c1 = int(self.firstform.IDEdit.text())
        for i in range(1000000):
            c2 = int(data['Complaint ID'][i])
            s1 = str(data[f"{a}"][i]).split()
            if c1 == c2:
                for j in range(1000):
                    s2 = str(data[f"{a}"][j]).split()
                    d1 = self.similarity(s1, s2)
                    if d1 > float(self.firstform.benzerlikEdit.text()):
                        self.firstform.tableWidget.setItem(row, 0, QTableWidgetItem(
                            str(str(d1) + "-" + str(data[f"{a}"][i]) + "-" + str(data[f"{a}"][j]))))
                        row = row + 1

    def hesapla1(self):
        if self.firstform.productButton1.isChecked() and self.firstform.IDEdit.text() == "":
            a = "Product"
            firstPage.benzerlik1(self, a, float(self.firstform.benzerlikEdit.text()))
        if self.firstform.productButton1.isChecked() and self.firstform.IDEdit.text() != "":
            a = "Product"
            firstPage.benzerlik3(self, a)
        if self.firstform.issueButton1.isChecked() and self.firstform.IDEdit.text() == "":
            a = "Issue"
            firstPage.benzerlik1(self, a, float(self.firstform.benzerlikEdit.text()))
        if self.firstform.issueButton1.isChecked() and self.firstform.IDEdit.text() != "":
            a = "Issue"
            firstPage.benzerlik3(self, a)
        if self.firstform.companyButton1.isChecked() and self.firstform.IDEdit.text() == "":
            a = "Company"
            firstPage.benzerlik1(self, a, float(self.firstform.benzerlikEdit.text()))
        if self.firstform.companyButton1.isChecked() and self.firstform.IDEdit.text() != "":
            a = "Company"
            firstPage.benzerlik3(self, a)
        if self.firstform.stateButton1.isChecked() and self.firstform.IDEdit.text() == "":
            a = "State"
            firstPage.benzerlik1(self, a, float(self.firstform.benzerlikEdit.text()))
        if self.firstform.stateButton1.isChecked() and self.firstform.IDEdit.text() != "":
            a = "State"
            firstPage.benzerlik3(self, a)
        if self.firstform.zipButton1.isChecked() and self.firstform.IDEdit.text() == "":
            a = "Zip Code"
            firstPage.benzerlik1(self, a, float(self.firstform.benzerlikEdit.text()))
        if self.firstform.zipButton1.isChecked() and self.firstform.IDEdit.text() != "":
            a = "Zip Code"
            firstPage.benzerlik3(self, a)
        if self.firstform.IDButton1.isChecked() and self.firstform.IDEdit.text() == "":
            a = "Complaint ID"
            firstPage.benzerlik1(self, a, float(self.firstform.benzerlikEdit.text()))
        if self.firstform.IDButton1.isChecked() and self.firstform.IDEdit.text() != "":
            a = "Complaint ID"
            firstPage.benzerlik3(self, a)
        stop = timeit.default_timer()
        self.firstform.toplamSure.setText(str(('Time:', stop - self.start)))



    def hesapla2(self):
        if self.firstform.productButton1.isChecked():
            a = "Product"
            if self.firstform.productButton2.isChecked():
                b = "Product"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.issueButton2.isChecked():
                b = "Issue"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.companyButton2.isChecked():
                b = "Company"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.stateButton2.isChecked():
                b = "State"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.zipButton2.isChecked():
                b = "Zip Code"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.IDButton2.isChecked():
                b = "Complaint ID"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            stop = timeit.default_timer()
            self.firstform.toplamSure.setText(str(('Time:', stop - self.start)))

        if self.firstform.issueButton1.isChecked():
            a = "Issue"
            if self.firstform.productButton2.isChecked():
                b = "Product"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.issueButton2.isChecked():
                b = "Issue"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.companyButton2.isChecked():
                b = "Company"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.stateButton2.isChecked():
                b = "State"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.zipButton2.isChecked():
                b = "Zip Code"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.IDButton2.isChecked():
                b = "Complaint ID"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            stop = timeit.default_timer()
            self.firstform.toplamSure.setText(str(('Time:', stop - self.start)))
        if self.firstform.companyButton1.isChecked():
            a = "Company"
            if self.firstform.productButton2.isChecked():
                b = "Product"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.issueButton2.isChecked():
                b = "Issue"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.companyButton2.isChecked():
                b = "Company"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.stateButton2.isChecked():
                b = "State"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.zipButton2.isChecked():
                b = "Zip Code"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.IDButton2.isChecked():
                b = "Complaint ID"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            stop = timeit.default_timer()
            self.firstform.toplamSure.setText(str(('Time:', stop - self.start)))
        if self.firstform.stateButton1.isChecked():
            a = "State"
            if self.firstform.productButton2.isChecked():
                b = "Product"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.issueButton2.isChecked():
                b = "Issue"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.companyButton2.isChecked():
                b = "Company"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.stateButton2.isChecked():
                b = "State"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.zipButton2.isChecked():
                b = "Zip Code"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.IDButton2.isChecked():
                b = "Complaint ID"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            stop = timeit.default_timer()
            self.firstform.toplamSure.setText(str(('Time:', stop - self.start)))
        if self.firstform.zipButton1.isChecked():
            a = "Zip Code"
            if self.firstform.productButton2.isChecked():
                b = "Product"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.issueButton2.isChecked():
                b = "Issue"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.companyButton2.isChecked():
                b = "Company"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.stateButton2.isChecked():
                b = "State"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.zipButton2.isChecked():
                b = "Zip Code"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.IDButton2.isChecked():
                b = "Complaint ID"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            stop = timeit.default_timer()
            self.firstform.toplamSure.setText(str(('Time:', stop - self.start)))
        if self.firstform.IDButton1.isChecked():
            a = "Complaint ID"
            if self.firstform.productButton2.isChecked():
                b = "Product"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.issueButton2.isChecked():
                b = "Issue"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.companyButton2.isChecked():
                b = "Company"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.stateButton2.isChecked():
                b = "State"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.zipButton2.isChecked():
                b = "Zip Code"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            if self.firstform.IDButton2.isChecked():
                b = "Complaint ID"
                firstPage.benzerlik2(self, a, b, float(self.firstform.benzerlikEdit.text()))
            stop = timeit.default_timer()
            self.firstform.toplamSure.setText(str(('Time:', stop - self.start)))


class Runnable(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.runTasks()

    def runTasks(self):
        pool = QThreadPool.globalInstance()
        for i in range(100):
            runnable = Runnable(i)
            pool.start(runnable)
