import sys
from PySide6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QListWidget, QVBoxLayout
from PySide6.QtCore import Qt

class AppListaTarefa(QWidget):
    def __init__(self):
        super().__init__()

        self.tarefas = []

        #Configuração da janela principal
        self.setWindowTitle('To do List')
        self.setGeometry(100, 100, 400, 600)

        #Widgets da interface
        self.txt_tarefa = QLineEdit()
        self.btn_adicionar = QPushButton('Adicionar')
        self.btn_adicionar.setStyleSheet("background-color: lightgreen;"
                                         "border-radius: 5px;"
                                         "border: 2px solid green;"
                                         )
        self.btn_concluir = QPushButton('Concluir')
        self.btn_concluir.setStyleSheet("background-color: lightblue;"
                                         "border-radius: 5px;"
                                         "border: 2px solid blue;"
                                         )
        self.btn_editar = QPushButton('Editar')
        self.btn_editar.setStyleSheet("background-color: #F1EB9C;"
                                         "border-radius: 5px;"
                                         "border: 2px solid orange;"
                                         )
        self.btn_remover = QPushButton('Remover')
        self.btn_remover.setStyleSheet("background-color: #FFA8A8;"
                                         "border-radius: 5px;"
                                         "border: 2px solid red;"
                                         )
        self.lst_tarefa = QListWidget()

        #Configuração do layout
        layout = QVBoxLayout()
        layout.addWidget(self.txt_tarefa)
        layout.addWidget(self.btn_adicionar)
        layout.addWidget(self.btn_concluir)
        layout.addWidget(self.btn_editar)
        layout.addWidget(self.btn_remover)
        layout.addWidget(self.lst_tarefa)

        self.setLayout(layout)

    def adicionar_tarefa(self):
        #Função para adicionar tarea à lista QList
        tarefa = self.txt_tarefa.text()
        if tarefa:
            self.lst_tarefa.addItem(tarefa)
            self.txt_tarefa.clear()

    def concluir_tarefa(self):
        #Função para marcar o checkbox como checado e desativar a edição de checkbox
        item_selecionado = self.lst_tarefa.currentItem()
        if item_selecionado:
            item_selecionado.setFlags(item_selecionado.flags()| Qt.ItemIsUserCheckable)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppListaTarefa()
    window.show()
    sys.exit(app.exec())