from datos.base_de_datos import BaseDeDatos

def crear_reclamo(idReclamo, descripcion, idInmueble, idUnidad, idUsuario, idServicio, fecha):
    crear_reclamo_sql = f"""
    INSERT INTO RECLAMOS(ID_RECLAMO, DESCRIPCION, ID_INMUEBLE, ID_UNIDAD, ID_USUARIO, ID_SERVICIO, FECHA, ESTADO)
    VALUES('{idReclamo}', '{descripcion}', '{idInmueble}', '{idUnidad}', '{idUsuario}', '{idServicio}', '{fecha}', 'pendiente' )
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_reclamo_sql)



#def modificar_reclamo(idReclamo, datosReclamo):
#    modificar_reclamo_sql = f"""
#        UPDATE RECLAMOS
#        SET DESCRIPCION='{datosReclamo["Problema Solucionado"]}',
#        WHERE ID_RECLAMO='{idReclamo}'
#    """
#
#    bd = BaseDeDatos()
#    bd.ejecutar_sql(modificar_reclamo_sql)