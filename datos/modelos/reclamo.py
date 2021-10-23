from datos.base_de_datos import BaseDeDatos
from datetime import datetime

def crear_reclamo(idReclamo, descripcion, idInmueble, idUnidad, idUsuario, idServicio):
    ahora = datetime.now()
    crear_reclamo_sql = f"""
    INSERT INTO RECLAMOS(ID_RECLAMO, DESCRIPCION, ID_INMUEBLE, ID_UNIDAD, ID_USUARIO, ID_SERVICIO, FECHA, ESTADO)
    VALUES('{idReclamo}', '{descripcion}', '{idInmueble}', '{idUnidad}', '{idUsuario}', '{idServicio}', '{ahora}', 'pendiente' )
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_reclamo_sql)



def modificar_reclamo(idReclamo, datosReclamo):
    #fechaModificado = datetime.now()
    modificar_reclamo_sql = f"""
        UPDATE RECLAMOS
        SET DESCRIPCION='{datosReclamo["descripcion"]}', FECHA = '{datosReclamo['{datosReclamo["descripcion"]}']}', ESTADO = '{datosReclamo["estado"]}'
        WHERE ID_RECLAMO='{idReclamo}'
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_reclamo_sql)
