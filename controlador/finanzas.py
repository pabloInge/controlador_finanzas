import sys
from PyQt5 import QtWidgets
sys.path.append("..")
from modelo.finanzas import *
from vista.finanzas import *

class Controlador:
    def set_model(self, modelo: Service):
        self.__modelo = modelo

    def set_view(self, vista: Vista):
        self.__vista = vista
        self.__vista.calcular_balance.connect(self.__on_calcular_balance)
        self.__vista.calcular_balance.emit()
        #self.__vista.agregar_ingreso.connect()
        #self.__vista.agregar_egreso.connect()

    def __on_calcular_balance(self):
        self.__vista.actualizar_balance(self.__modelo.calcular_balance())

    def show_vista(self):
        self.__vista.show()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    modelo = Service()
    vista = Vista()
    controlador = Controlador()

    controlador.set_model(modelo)
    controlador.set_view(vista)
    controlador.show_vista()

    app.exec()
