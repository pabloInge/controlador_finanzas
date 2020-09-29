from PyQt5 import QtCore

from vista.ingreso_egreso import VentanaIngreso, TipoCategoriaDTO
from modelo.ingreso import (
    ServiceIngreso,
    IngresoDTO,
    MontoError,
    TipoError,
    CategoriaError,
)
from modelo.tipo_transaccion import ServiceTipoTransaccion as TipoTransaccion
from modelo.categoria_ingreso import ServiceCategoriaIngreso as CategoriaIngreso


class ControladorIngreso(QtCore.QObject):
    actualizar_balance = QtCore.pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.__modelo = ServiceIngreso()
        self.__vista = VentanaIngreso(parent)
        self.__vista.registrar.connect(self.__on_registrar)

    def __on_registrar(self):
        ingreso = self.__vista.obtener_transaccion()
        try:
            self.__modelo.registrar_ingreso(
                IngresoDTO(
                    ingreso.monto,
                    ingreso.id_tipo_transaccion,
                    ingreso.id_categoria,
                    ingreso.descripcion,
                    ingreso.fecha,
                )
            )
            self.actualizar_balance.emit()
            self.__vista.close()
        except (MontoError, TipoError, CategoriaError) as error:
            self.__vista.mostrar_error(error)

    def __actualizar_tipos_categorias(self):
        self.__vista.actualizar_tipos_transaccion(TipoTransaccion().obtener_tipos())
        self.__vista.actualizar_categorias(CategoriaIngreso().obtener_cat_ingreso())

    def show_vista(self):
        self.__actualizar_tipos_categorias()
        self.__vista.show()
