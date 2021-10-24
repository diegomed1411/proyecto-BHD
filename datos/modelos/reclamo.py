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
    fechaModificado = datetime.now()
    modificar_reclamo_sql = f"""
        UPDATE RECLAMOS
        SET DESCRIPCION='{datosReclamo["descripcion"]}', FECHA='{fechaModificado}', ESTADO='{datosReclamo["estado"]}'
        WHERE ID_RECLAMO='{idReclamo}'
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_reclamo_sql)


def obtener_reclamos():
    obtener_reclamos_sql = f"""
        SELECT ID_RECLAMO, DESCRIPCION, ID_INMUEBLE, ID_UNIDAD, ID_USUARIO, ID_SERVICIO, FECHA, ESTADO
        FROM RECLAMOS
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "descripcion": registro[1],
             "id_inmueble": registro[2],
             "id_unidad": registro[3],
             "id_usuario": registro[4],
             "id_servicio": registro[5],
             "fecha": registro[6],
             "estado": registro[7],
             } for registro in bd.ejecutar_sql(obtener_reclamos_sql)]

def obtener_reclamo(id_reclamo):
    obtener_reclamos_sql = f"""
        SELECT ID_RECLAMO, DESCRIPCION, ID_INMUEBLE, ID_UNIDAD, ID_USUARIO, ID_SERVICIO, FECHA, ESTADO
        FROM RECLAMOS
        WHERE ID_RECLAMO = '{id_reclamo}'
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "descripcion": registro[1],
             "id_inmueble": registro[2],
             "id_unidad": registro[3],
             "id_usuario": registro[4],
             "id_servicio": registro[5],
             "fecha": registro[6],
             "estado": registro[7],
             } for registro in bd.ejecutar_sql(obtener_reclamos_sql)]

def borrar_reclamo(id_reclamo):
    obtener_reclamos_sql = f"""
        DELETE
        FROM RECLAMOS
        WHERE ID_RECLAMO = '{id_reclamo}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_reclamos_sql)