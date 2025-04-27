from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def __init__(self):
        self.total_income = 0
        self.total_expense = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)

        self.lineEdit_income = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_income.setPlaceholderText("Masukan Pendapatan")
        self.verticalLayout.addWidget(self.lineEdit_income)

        self.lineEdit_expense = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_expense.setPlaceholderText("Masukan Pengeluaran")
        self.verticalLayout.addWidget(self.lineEdit_expense)

        self.comboBox_category = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_category.addItems(["Makanan", "Transportasi", "Hiburan", "Investasi", "Lainnya"])
        self.verticalLayout.addWidget(self.comboBox_category)

        self.pushButton = QtWidgets.QPushButton("Tambah Transaksi", self.centralwidget)
        self.pushButton.clicked.connect(self.add_transaction)  
        self.verticalLayout.addWidget(self.pushButton)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Transaksi", "Kategori"])
        self.verticalLayout.addWidget(self.tableWidget)

        self.label_total_income = QtWidgets.QLabel("Total Pendapatan: 0", self.centralwidget)
        self.verticalLayout.addWidget(self.label_total_income)

        self.label_total_expense = QtWidgets.QLabel("Total Pengeluaran: 0", self.centralwidget)
        self.verticalLayout.addWidget(self.label_total_expense)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Finance Tracker"))

    def add_transaction(self):
        income_text = self.lineEdit_income.text()
        expense_text = self.lineEdit_expense.text()
        category = self.comboBox_category.currentText()

        if income_text:
            try:
                income = float(income_text)
                self.total_income += income
                self.tableWidget.insertRow(self.tableWidget.rowCount())
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(f"{income}"))
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(category))
                self.label_total_income.setText(f"Total Pendapatan: {self.total_income}")
            except ValueError:
                QtWidgets.QMessageBox.warning(None, "Input Error", "Masukkan nilai pendapatan yang valid.")

        if expense_text:
            try:
                expense = float(expense_text)
                self.total_expense += expense
                self.tableWidget.insertRow(self.tableWidget.rowCount())
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(f"-{expense}"))
                self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(category))
                self.label_total_expense.setText(f"Total Pengeluaran: {self.total_expense}")
            except ValueError:
                QtWidgets.QMessageBox.warning(None, "Input Error", "Masukkan nilai pengeluaran yang valid.")

        self.lineEdit_income.clear()
        self.lineEdit_expense.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())