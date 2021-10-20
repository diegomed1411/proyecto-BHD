from datos.base_de_datos import BaseDeDatos

def crear_unidades(idUnidad, numeroUnidad, usuariosUnidad, gastosUnidad, idInmueble):
    crear_unidades_sql = f"""
    INSERT INTO UNIDADES(ID_UNIDAD, NUMERO_DE_UNIDAD, USUARIOS_DE_UNIDAD, GASTOS_DE_UNIDAD, ID_INMUEBLE)
    VALUES('{idUnidad}', '{numeroUnidad}', '{usuariosUnidad}', '{gastosUnidad}', '{idInmueble}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_unidades_sql)