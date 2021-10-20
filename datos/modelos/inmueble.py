from datos.base_de_datos import BaseDeDatos

def crear_inmueble(idInmueble, nombreInmueble, direccion, cantidadUnidades, servicios, identificadorCocheras, actas, unidadesActivas, listaAmenities):
    crear_inmueble_sql = f"""
    INSERT INTO INMUEBLES(ID_INMUEBLE, NOMBRE_DE_INMUEBLE, DIRECCION, CANTIAD_DE_UNIDADES, SERVICIOS, ID_COCHERA, REGLAMENTO_Y_ACTAS, UNIDADES_ACTIVAS, ID_AMENITIE)
    VALUES('{idInmueble}', '{nombreInmueble}', '{direccion}', '{cantidadUnidades}', '{servicios}', '{identificadorCocheras}', '{actas}', '{unidadesActivas}', '{listaAmenities}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_inmueble_sql)

