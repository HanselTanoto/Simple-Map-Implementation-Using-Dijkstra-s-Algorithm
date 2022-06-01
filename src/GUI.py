import timeit
import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from pyvis.network import Network
import DirectedGraph as dg
import Dijkstra as dj
import ReadFile as rf

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)

        font = QtGui.QFont()
        font.setFamily("Lucida Sans")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #FFFFFF;")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 20, 820, 725))
        self.widget1.setObjectName("widget1")

        self.widget1_1 = QtWidgets.QWidget(self.widget1)
        self.widget1_1.setGeometry(QtCore.QRect(10, 10, 800, 705))
        self.widget1_1.setStyleSheet("background-color: #222222;")
        self.widget1_1.setObjectName("widget1_1")
        
        # Container for the graph
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.widget1)
        self.webEngineView.setGeometry(QtCore.QRect(0, 0, 820, 725))
        self.webEngineView.setStyleSheet("background-color: #222222;")
        self.webEngineView.setVisible(False)
        self.webEngineView.setObjectName("webEngineView")

        # Container for showing the shortest path
        self.label0 = QtWidgets.QLabel(self.widget1)
        self.label0.setGeometry(QtCore.QRect(45, 30, 730, 30))
        self.label0.setStyleSheet("background-color: #FFFFFF; border-radius: 10px;")
        font.setPointSize(10)
        self.label0.setFont(font)
        self.label0.setAlignment(QtCore.Qt.AlignCenter)
        self.label0.setVisible(False)
        self.label0.setObjectName("label0")

        # Container for showing the shortest distance from source to destination
        self.label1 = QtWidgets.QLabel(self.widget1)
        self.label1.setGeometry(QtCore.QRect(45, 660, 200, 30))
        self.label1.setStyleSheet("background-color: #FFFFFF; border-radius: 10px;")
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setVisible(False)
        self.label1.setObjectName("label1")
        
        # Container for showing the number of iterations
        self.label2 = QtWidgets.QLabel(self.widget1)
        self.label2.setGeometry(QtCore.QRect(285, 660, 200, 30))
        self.label2.setStyleSheet("background-color: #FFFFFF; border-radius: 10px;")
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setVisible(False)
        self.label2.setObjectName("label2")
        
        # Container for showing the time taken to find the shortest path
        self.label3 = QtWidgets.QLabel(self.widget1)
        self.label3.setGeometry(QtCore.QRect(525, 660, 250, 30))
        self.label3.setStyleSheet("background-color: #FFFFFF; border-radius: 10px;")
        font.setPointSize(10)
        self.label3.setFont(font)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setVisible(False)
        self.label3.setObjectName("label3")

        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(860, 20, 475, 250))
        self.widget2.setStyleSheet("background-color: #222222; border-radius: 25px;")
        self.widget2.setObjectName("widget2")

        # Container for input file name
        self.lineEdit1 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit1.setGeometry(QtCore.QRect(20, 20, 300, 50))
        self.lineEdit1.setStyleSheet("background-color: #FFFFFF; border-radius: 15px;")
        font.setPointSize(14)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit1.setPlaceholderText("Enter File Name")
        self.lineEdit1.setObjectName("lineEdit1")

        # Button to view the graph
        self.button1 = QtWidgets.QPushButton(self.widget2)
        self.button1.setGeometry(QtCore.QRect(345, 20, 110, 50))
        self.button1.setStyleSheet("background-color: #FFFFFF; border-radius: 15px;")
        font.setPointSize(14)
        self.button1.setFont(font)
        self.button1.setText("VIEW")
        self.button1.setObjectName("button1")

        self.widget2_1 = QtWidgets.QWidget(self.widget2)
        self.widget2_1.setGeometry(QtCore.QRect(20, 90, 190, 50))
        self.widget2_1.setStyleSheet("background-color: #FFFFFF; border-radius: 15px;")
        self.widget2_1.setObjectName("widget2_1")

        # Container for source node
        self.comboBox1 = QtWidgets.QComboBox(self.widget2)
        self.comboBox1.setGeometry(QtCore.QRect(25, 95, 175, 40))
        self.comboBox1.setStyleSheet("background-color: #FFFFFF;")
        font.setPointSize(10)
        self.comboBox1.setEditable(True)
        self.comboBox1.lineEdit().setFont(font)
        self.comboBox1.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox1.lineEdit().setPlaceholderText("Source Node")
        self.comboBox1.setObjectName("comboBox1")

        self.label5 = QtWidgets.QLabel(self.widget2)
        self.label5.setGeometry(QtCore.QRect(220, 90, 35, 50))
        self.label5.setStyleSheet("color: #FFFFFF;")
        font.setPointSize(14)
        self.label5.setFont(font)
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setText("to")
        self.label5.setObjectName("label5")

        self.widget2_2 = QtWidgets.QWidget(self.widget2)
        self.widget2_2.setGeometry(QtCore.QRect(265, 90, 190, 50))
        self.widget2_2.setStyleSheet("background-color: #FFFFFF; border-radius: 15px;")
        self.widget2_2.setObjectName("widget2_2")

        # Container for destination node
        self.comboBox2 = QtWidgets.QComboBox(self.widget2)
        self.comboBox2.setGeometry(QtCore.QRect(270, 95, 175, 40)) 
        self.comboBox2.setStyleSheet("background-color: #FFFFFF;")
        font.setPointSize(10)
        self.comboBox2.setEditable(True)
        self.comboBox2.lineEdit().setFont(font)
        self.comboBox2.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox2.lineEdit().setPlaceholderText("Destination Node")
        self.comboBox2.setObjectName("comboBox2")
        
        # Button to find the shortest path
        self.button2 = QtWidgets.QPushButton(self.widget2)
        self.button2.setGeometry(QtCore.QRect(20, 160, 435, 50))
        self.button2.setStyleSheet("background-color: #FFFFFF; border-radius: 15px;")
        font.setPointSize(14)
        self.button2.setFont(font)
        self.button2.setText("FIND PATH")
        self.button2.setEnabled(False)
        self.button2.setObjectName("button2")

        self.line1 = QtWidgets.QFrame(self.widget2)
        self.line1.setGeometry(QtCore.QRect(20, 225, 435, 7))
        self.line1.setStyleSheet("background-color: #FFFFFF; border-radius: 15px;")
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(860, 300, 475, 440))
        self.widget3.setStyleSheet("background-color: #222222; border-radius: 25px;")
        self.widget3.setObjectName("widget3")

        self.label6 = QtWidgets.QLabel(self.widget3)
        self.label6.setGeometry(QtCore.QRect(20, 10, 435, 30))
        self.label6.setStyleSheet("background-color: rgba(0,0,0,0); color: #FFFFFF;")
        font.setPointSize(14)
        self.label6.setFont(font)
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setText("STEPS")
        self.label6.setObjectName("label6")

        # Container for the steps
        self.tableWidget = QtWidgets.QTableWidget(self.widget3)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 435, 370))
        self.tableWidget.setStyleSheet("background-color: #222222; gridline-color: #FFFFFF; border: 1px solid #FFFFFF; border-radius: 0px;")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Step", "Distance"])
        self.tableWidget.horizontalHeader().setStyleSheet("background-color: #FFFFFF;")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
       
        # Error message dialog
        self.errorMessage = QtWidgets.QMessageBox(self.centralwidget)
        self.errorMessage.setWindowTitle("Dijkstra's Shortest Path Finder")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dijkstra's Shortest Path Finder"))
        MainWindow.setWindowIcon(QtGui.QIcon("../bin/logo.png"))
    

    def main(self):
        print("Application Started")
        self.button1.clicked.connect(lambda: self.viewClicked())
    

    # Event handler for the VIEW Button
    def viewClicked(self):
        print("view button clicked")
        self.reset()
        file_name = self.lineEdit1.text()
        
        try :
            self.graph = rf.read_file(file_name)
            self.graph = dg.DirectedGraph(self.graph)
        except Exception as e:
            self.errorMessage.setText(file_name + ".\nFile not found.\nCheck the file name and try again.")
            self.errorMessage.setIcon(QtWidgets.QMessageBox.Warning)
            self.errorMessage.exec_()
            print(e)
            self.fileAvailable = False
            self.button2.setEnabled(False)
            return

        self.fileAvailable = True
        self.graph.print_graph()
        net = Network(height="700px", width="800", bgcolor="#222222", font_color="black", directed=True)
        for i in range(self.graph.nodes):
            net.add_node(i, label=str(i), title=str(i), shape="circle", color="#3DFF94", labelHighlightedBold=True)
        for i in range(self.graph.nodes):
            for j in range(self.graph.nodes):
                if self.graph.matrix[i][j] != 0:
                    net.add_edge(i, j, weight=self.graph.matrix[i][j], label=str(self.graph.matrix[i][j]), color="#00C8FF")
        net.save_graph(r"..\bin\graph.html")
        self.webEngineView.setVisible(True)
        self.webEngineView.load(QtCore.QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r"\..\bin\graph.html"))

        self.comboBox1.addItems([str(i) for i in range(self.graph.nodes)])
        self.comboBox2.addItems([str(i) for i in range(self.graph.nodes)])

        self.button2.setEnabled(True)
        self.button2.clicked.connect(lambda: self.findClicked())
    

    # Event handler for the FIND Button
    def findClicked(self):
        print("find button clicked")
        start = self.comboBox1.currentText()
        end = self.comboBox2.currentText()

        if start == "" or end == "":
            self.errorMessage.setText("Please select a source and destination node.")
            self.errorMessage.setIcon(QtWidgets.QMessageBox.Information)
            self.errorMessage.exec_()
            return
        if start not in [str(i) for i in range(self.graph.nodes)] or end not in [str(i) for i in range(self.graph.nodes)]:
            self.errorMessage.setText("Please enter a valid source and destination node.")
            self.errorMessage.setIcon(QtWidgets.QMessageBox.Information)
            self.errorMessage.exec_()
            return
        if not self.fileAvailable:
            self.errorMessage.setText("Please select a file first.")
            self.errorMessage.setIcon(QtWidgets.QMessageBox.Information)
            self.errorMessage.exec_()
            return

        time = timeit.default_timer()
        dijkstra = dj.Dijkstra(self.graph, int(start), int(end))
        time = timeit.default_timer() - time
        
        self.tableWidget.setRowCount(dijkstra.iterate)
        for i in range(dijkstra.iterate):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(dijkstra.get_step_info(i)))
        self.tableWidget.resizeRowsToContents()
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.item(i, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.item(i, j).setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        net = Network(height="700px", width="800", bgcolor="#222222", font_color="black", directed=True)
        for i in range(self.graph.nodes):
            if (i in dijkstra.path):
                net.add_node(i, label=str(i), title=str(i), shape="circle", color="yellow", labelHighlightedBold=True)
            else:
                net.add_node(i, label=str(i), title=str(i), shape="circle", color="#3DFF94", labelHighlightedBold=True)
        for i in range(self.graph.nodes):
            for j in range(self.graph.nodes):
                if self.graph.matrix[i][j] != 0:
                    if (str(i)+str(j)) in ("".join(str(e) for e in dijkstra.path)):
                        net.add_edge(i, j, weight=self.graph.matrix[i][j], label=str(self.graph.matrix[i][j]), color="red", width=4)
                    else:
                        net.add_edge(i, j, weight=self.graph.matrix[i][j], label=str(self.graph.matrix[i][j]), color="#00C8FF")
        net.save_graph(r"..\bin\graph.html")
        self.webEngineView.setVisible(True)
        self.webEngineView.load(QtCore.QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r"\..\bin\graph.html"))

        self.label0.setVisible(True)
        self.label0.setText("Path from Source to Destination : " + ("Unreachable!" if dijkstra.distance == sys.maxsize else dijkstra.get_path_str()))
        self.label1.setVisible(True)
        self.label1.setText("Distance = " + ("-" if dijkstra.distance == sys.maxsize else str(dijkstra.distance)))
        self.label2.setVisible(True)
        self.label2.setText("Iteration = " + str(dijkstra.iterate))
        self.label3.setVisible(True)
        self.label3.setText("Elapsed Time = " + "{:.3f} ms".format(time*1000))
    

    # Function to clear all the I/O fields
    def reset(self):
        self.label0.setVisible(False)
        self.label1.setVisible(False)
        self.label2.setVisible(False)
        self.label3.setVisible(False)
        self.label0.setText("")
        self.label1.setText("")
        self.label2.setText("")
        self.label3.setText("")
        self.tableWidget.setRowCount(0)
        self.webEngineView.setVisible(False)
        self.comboBox1.clear()
        self.comboBox2.clear()


### MAIN PROGRAM ###
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.main()
    MainWindow.show()
    sys.exit(app.exec_())