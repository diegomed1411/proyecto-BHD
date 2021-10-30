from datos.base_de_datos import BaseDeDatos

def crear_unidades(idUnidad, numeroUnidad, usuariosUnidad, gastosUnidad, idInmueble):
    crear_unidades_sql = f"""
    INSERT INTO UNIDADES(ID_UNIDAD, NUMERO_DE_UNIDAD, USUARIOS_DE_UNIDAD, GASTOS_DE_UNIDAD, ID_INMUEBLE)
    VALUES('{idUnidad}', '{numeroUnidad}', '{usuariosUnidad}', '{gastosUnidad}', '{idInmueble}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_unidades_sql)

# -- obtener listado de unidades

def obtener_unidades():
    obtener_unidades_sql = f"""
        SELECT ID_UNIDAD, NUMERO_DE_UNIDAD, GASTOS_DE_UNIDAD, ID_INMUEBLE 
        FROM UNIDADES
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "numero": registro[1],
             "gastos": registro[2],
             "idInmueble": registro[3],
             } for registro in bd.ejecutar_sql(obtener_unidades_sql)]