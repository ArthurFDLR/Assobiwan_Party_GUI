# Ajout de la modification de la taille d'ecran

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer


## APPLICATION DE CONTROLE HORS INTERFACE (REGARDEZ ICI LES TREZ ET LES RESPOS COCKTAILS) ##

# AFFICHE LE TOTALE DES VENTES EN EURO
def Print_vente():
    fichier_data = open('res/Data_All.txt',"r")
    data = fichier_data.readlines()
    sum=0
    for line in data:
        Prix1,Prix2 = line.split(';')
        sum += round(float(Prix1),2) + round(float(Prix2[:len(Prix2)-1]),2)
    print(round(sum,2))
    
# REINITIALISE UNE PARTIE
# ATTENTION, RETOUR IMPOSSIBLE !!!!!!
def Reinitialisation():
    ui.Click_Reset()
    print("REINITIALISATION REUSSIE")





TAILLE_FENETRE = 1 # Permet de retrecir la fenetre si depasse de l'ecran





## Application externes
# Nbr_verre_lutte = variable variant de -5 a 5 : +1 si achat des Jedi, -1 si achat des sith, modification des prix si atteint +5 ou -5

def Get_Nbr_verre_lutte():
    fichier_data = open('res/Data_Current.txt',"r") # Data_All : Nbr_verre_lutte ; Prix_Jedi ; Prix_Sith
    data = fichier_data.readlines()
    Nbr_verre_lutte = data[0].split(";")[0]
    fichier_data.close()
    return int(Nbr_verre_lutte)

def Get_Prix_verre():
    fichier_data = open('res/Data_Current.txt',"r")
    data = fichier_data.readlines()
    Prix_Jedi = data[0].split(";")[1]
    Prix_Sith = data[0].split(";")[2]
    fichier_data.close()
    return float(Prix_Jedi),float(Prix_Sith)
    
def Set_Nbr_verre_lutte(Nbr_verre_lutte):
    line = [Nbr_verre_lutte]
    line.append(Get_Prix_verre()[0])
    line.append(Get_Prix_verre()[1])
    line.append(Get_Val_BarProgress())
    fichier_data = open('res/Data_Current.txt',"w")
    fichier_data.write('{};{};{};{}\n'.format(str(line[0]),str(line[1]),str(line[2]),str(line[3])))
    fichier_data.close()
    
def Set_Prix_verre(prix_Jedi, prix_Sith):
    line = [Get_Nbr_verre_lutte()]
    line.append(prix_Jedi)
    line.append(prix_Sith)
    line.append(Get_Val_BarProgress())
    fichier_data = open('res/Data_Current.txt',"w")
    fichier_data.write('{};{};{};{}\n'.format(str(line[0]),str(round(line[1],2)),str(round(line[2],2)),str(line[3])))
    fichier_data.close()

def Get_Val_BarProgress(): # Varie entre 0 et 80 : 0 -> Jedi 100; Sith 20 et 80 ->Jedi 20; Sith 100  #### 2 points par achat de verre
    fichier_data = open('res/Data_Current.txt',"r")
    data = fichier_data.readlines()
    Val_Bar = data[0].split(";")[3][0:len(data[0].split(";")[3])-1]
    fichier_data.close()
    return int(Val_Bar)

def Set_Val_BarProgress(Val_Bar):
    line = [Get_Nbr_verre_lutte()]
    line.append(Get_Prix_verre()[0])
    line.append(Get_Prix_verre()[1])
    line.append(Val_Bar)
    fichier_data = open('res/Data_Current.txt',"w")
    fichier_data.write('{};{};{};{}\n'.format(str(line[0]),str(round(line[1],2)),str(round(line[2],2)),str(line[3])))
    fichier_data.close()
    

def Achat_verre_Sith():
    Prix_Jedi,Prix_Sith = Get_Prix_verre()
    print("+1 Sith à {}€".format(round(Prix_Sith,2)))
    Set_Nbr_verre_lutte(Get_Nbr_verre_lutte() - 1)
    if Get_Nbr_verre_lutte() == -5:
        Set_Nbr_verre_lutte(0)
        Prix_Jedi,Prix_Sith = Get_Prix_verre()
        if Prix_Sith>0.80:
            Prix_Sith -= 0.05
            Prix_Jedi += 0.05
        Set_Prix_verre(Prix_Jedi, Prix_Sith)
    if Get_Val_BarProgress()<80 and not (Get_Val_BarProgress() == 0 and Get_Nbr_verre_lutte()>0):
        Set_Val_BarProgress(Get_Val_BarProgress() + 2)
    
def Achat_verre_Jedi():
    Prix_Jedi,Prix_Sith = Get_Prix_verre()
    print("+1 Jedi à {}€".format(round(Prix_Jedi,2)))
    Set_Nbr_verre_lutte(Get_Nbr_verre_lutte() + 1)
    if Get_Nbr_verre_lutte() == 5:
        Set_Nbr_verre_lutte(0)
        Prix_Jedi,Prix_Sith = Get_Prix_verre()
        if Prix_Jedi>0.80:
            Prix_Sith += 0.05
            Prix_Jedi -= 0.05
        Set_Prix_verre(Prix_Jedi, Prix_Sith)
    if Get_Val_BarProgress()>0 and not (Get_Val_BarProgress() == 80 and Get_Nbr_verre_lutte()<0):
        Set_Val_BarProgress(Get_Val_BarProgress() - 2)

def Ajout_vente(equipe, prix):
    fichier_data = open('res/Data_All.txt',"a")
    
    if equipe=="Jedi":
        fichier_data.write("{};0\n".format(prix))
    if equipe=="Sith":
        fichier_data.write("0;{}\n".format(prix))
    
    fichier_data.close()

def Reset_Partie():
    fichier_data = open('res/Data_Current.txt',"w")
    fichier_data.write('0;1.0;1.0;40\n')
    fichier_data.close()
    
## Definition de l'interface
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1850, 950)
        MainWindow.setMinimumSize(QtCore.QSize(1850*TAILLE_FENETRE, 1000*TAILLE_FENETRE)) #Fixe la taille
        MainWindow.setMaximumSize(QtCore.QSize(1850*TAILLE_FENETRE, 1000*TAILLE_FENETRE))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)

        QtGui.QFontDatabase.addApplicationFont('res/Starjedi.ttf')

        ## Font star wars
        font = QtGui.QFont()
        font.setFamily("Star Jedi")
        MainWindow.setFont(font)
        
    ## BackGround
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
"QWidget#centralwidget{\n"
"    border-image: url(res/BackGroundV1.png) 0 0 0 0 stretch stretch\n"
"}")

    ## ProgressBar
        self.progressBar_Sith = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_Sith.setGeometry(QtCore.QRect(95*TAILLE_FENETRE, 630*TAILLE_FENETRE, 825*TAILLE_FENETRE, 120*TAILLE_FENETRE))
        self.progressBar_Sith.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar_Sith.setAutoFillBackground(False)
        self.progressBar_Sith.setStyleSheet(
"QProgressBar {\n"
"    border: 0px solid grey;\n"
"    border-radius: 2px;\n"
"    background-color: transparent;"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #00000000, stop: 0.25 #ccff5151, stop: 0.4 #ff0000, stop: 0.6 #ff0000, stop: 0.75 #ccff5151, stop: 1 #00ffffff);\n"
"    width: 2px;\n"
"}")
        self.progressBar_Sith.setProperty("value", 78)
        self.progressBar_Sith.setObjectName("progressBar_Sith")
        self.progressBar_Sith.setTextVisible(False)
        
        
        self.progressBar_Jedi = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_Jedi.setGeometry(QtCore.QRect(920*TAILLE_FENETRE, 630*TAILLE_FENETRE, 825*TAILLE_FENETRE, 120*TAILLE_FENETRE))
        self.progressBar_Jedi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_Jedi.setAutoFillBackground(False)
        self.progressBar_Jedi.setStyleSheet(
"QProgressBar {\n"
"    border: 0px solid grey;\n"
"    border-radius: 2px;\n"
"    background-color: transparent;"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #00000000, stop: 0.25 #cc54c6ff, stop: 0.4 #0067f7, stop: 0.6 #0067f7, stop: 0.75 #cc54c6ff, stop: 1 #00ffffff);\n"

"    width: 2px;\n"
"}")
        self.progressBar_Jedi.setProperty("value", 25)
        self.progressBar_Jedi.setObjectName("progressBar_Jedi")
        self.progressBar_Jedi.setTextVisible(False)
        
    ## Button
        self.JediButton = QtWidgets.QPushButton(self.centralwidget)
        self.JediButton.setGeometry(QtCore.QRect(1553*TAILLE_FENETRE, 774*TAILLE_FENETRE, 191*TAILLE_FENETRE, 192*TAILLE_FENETRE))
        self.JediButton.setStyleSheet(
"QPushButton {\n"
"    border-image: url(res/ButtonJedi.png) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent;"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-image: url(res/ButtonJedi_pressed.png) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent;"
"}")
        self.JediButton.setObjectName("JediButton")
        
        self.SithButton = QtWidgets.QPushButton(self.centralwidget)
        self.SithButton.setGeometry(QtCore.QRect(105*TAILLE_FENETRE, 757*TAILLE_FENETRE, 186*TAILLE_FENETRE, 215*TAILLE_FENETRE))
        self.SithButton.setStyleSheet(
"QPushButton {\n"
"    border-image: url(res/ButtonSith.png) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent;"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-image: url(res/ButtonSith_pressed.png) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent;"
"}")
        self.SithButton.setObjectName("SithButton")
        
        '''
        self.ResetButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetButton.setGeometry(QtCore.QRect(800, 770, 311, 131))
        self.ResetButton.setStyleSheet("background-image: url(logo.png)")
        self.ResetButton.setObjectName("ResetButton")
        self.ResetButton.clicked.connect(self.Click_Reset)
        '''
        
        self.JediButton.clicked.connect(self.Click_Jedi)
        self.SithButton.clicked.connect(self.Click_Sith)
        
    ## Scores
        self.ScoreSiths = QtWidgets.QLCDNumber(self.centralwidget)
        self.ScoreSiths.setGeometry(QtCore.QRect(-110*TAILLE_FENETRE, 280*TAILLE_FENETRE, 690*TAILLE_FENETRE, 330*TAILLE_FENETRE))
        self.ScoreSiths.setAutoFillBackground(False)
        self.ScoreSiths.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: transparent;")
        self.ScoreSiths.setSmallDecimalPoint(False)
        self.ScoreSiths.setDigitCount(5)
        self.ScoreSiths.setMode(QtWidgets.QLCDNumber.Dec)
        self.ScoreSiths.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ScoreSiths.setProperty("value", 0.85)
        self.ScoreSiths.setObjectName("ScoreSiths")
        
        self.ScoreJedis = QtWidgets.QLCDNumber(self.centralwidget)
        self.ScoreJedis.setGeometry(QtCore.QRect(1130*TAILLE_FENETRE, 280*TAILLE_FENETRE, 690*TAILLE_FENETRE, 330*TAILLE_FENETRE))
        self.ScoreJedis.setAutoFillBackground(False)
        self.ScoreJedis.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: transparent;")
        self.ScoreJedis.setSmallDecimalPoint(False)
        self.ScoreJedis.setDigitCount(5)
        self.ScoreJedis.setMode(QtWidgets.QLCDNumber.Dec)
        self.ScoreJedis.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.ScoreJedis.setProperty("value", 0.55)
        self.ScoreJedis.setObjectName("ScoreJedis")
        
    ## Appli
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1850, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ## Initialisation des prix et barres en coherence avec le fichier Data_current
    
        self.ScoreJedis.display(Get_Prix_verre()[0])
        self.ScoreSiths.display(Get_Prix_verre()[1])
        
        self.progressBar_Jedi.setValue(100 - Get_Val_BarProgress())
        self.progressBar_Sith.setValue(20 + Get_Val_BarProgress())
    
    ## Tableau d'honneur
    
        self.lineEdit_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nom.setGeometry(QtCore.QRect(50*TAILLE_FENETRE, 400*TAILLE_FENETRE, 113*TAILLE_FENETRE, 20*TAILLE_FENETRE))
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        
        self.comboBox_equipe = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_equipe.setGeometry(QtCore.QRect(50*TAILLE_FENETRE, 300*TAILLE_FENETRE, 69*TAILLE_FENETRE, 22*TAILLE_FENETRE))
        self.comboBox_equipe.setObjectName("comboBox_equipe")
        
        self.spinBox_verres = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_verres.setGeometry(QtCore.QRect(50*TAILLE_FENETRE, 350*TAILLE_FENETRE, 42*TAILLE_FENETRE, 22*TAILLE_FENETRE))
        self.spinBox_verres.setObjectName("spinBox_verres")
        
        self.lineEdit_nom.returnPressed.connect(self.Affiche_gagnant)
        self.comboBox_equipe.addItem("Jedi")
        self.comboBox_equipe.addItem("Sith")
        self.Nom_gagnant = QtWidgets.QLabel(self.centralwidget)
        self.Nom_gagnant.setGeometry(QtCore.QRect(0*TAILLE_FENETRE, 30*TAILLE_FENETRE, 1850*TAILLE_FENETRE, 120*TAILLE_FENETRE))
        self.Nom_gagnant.setObjectName("Nom_gagnant")
        self.Nom_gagnant.setStyleSheet("QLabel {\n"
        "background-color:transparent;\n"
        "color:#FFFF00;\n"
        "font:40px;\n"
        "}")
        self.Nom_gagnant.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def Affiche_gagnant(self):
        Nom=self.lineEdit_nom.text()
        Verre=self.spinBox_verres.value()
        Equipe=self.comboBox_equipe.currentText()
        self.Nom_gagnant.setText(Nom + " : " + "Maître combattant de l’équipe" + " " + Equipe + " avec " + str(Verre) + " verres")
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    ## Action Buttons
    
    def Click_Jedi(self):
        Prix_Jedi, Prix_Sith = Get_Prix_verre()
        Ajout_vente("Jedi", Prix_Jedi)
        Achat_verre_Jedi()
        Prix_Jedi, Prix_Sith = Get_Prix_verre()
        self.ScoreJedis.display(Prix_Jedi)
        self.ScoreSiths.display(Prix_Sith)
        
        self.progressBar_Jedi.setValue(100 - Get_Val_BarProgress())
        self.progressBar_Sith.setValue(20 + Get_Val_BarProgress())
        
    def Click_Sith(self):
        Prix_Jedi, Prix_Sith = Get_Prix_verre()
        Ajout_vente("Sith", Prix_Sith)
        Achat_verre_Sith()
        Prix_Jedi, Prix_Sith = Get_Prix_verre()
        self.ScoreJedis.display(Prix_Jedi)
        self.ScoreSiths.display(Prix_Sith)
        
        self.progressBar_Jedi.setValue(100 - Get_Val_BarProgress())
        self.progressBar_Sith.setValue(20 + Get_Val_BarProgress())
        
    def Click_Reset(self):
        Reset_Partie()
        Prix_Jedi, Prix_Sith = Get_Prix_verre()
        self.ScoreJedis.display(Prix_Jedi)
        self.ScoreSiths.display(Prix_Sith)
        
        self.progressBar_Jedi.setValue(100 - Get_Val_BarProgress())
        self.progressBar_Sith.setValue(20 + Get_Val_BarProgress())  

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

