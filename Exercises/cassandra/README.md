# Objetivos

El objetivo de este ejercicio es familiarizarse con las operaciones
básicas de Cassandra, incluyendo la creación de keyspaces, tablas,
inserción, actualización y borrado de datos utilizando CQL (Cassandra
Query Language).

## Pre-requisitos

- Tener Docker y Docker Compose instalados,
- Contar con conocimientos básicos de bases de datos NoSQL y Cassandra,
- Entender el funcionamiento básico de contenedores Docker.

## 1. Configuración del entorno

1. **Inicio del clúster de Cassandra**. Utiliza el archivo `compose.yml`
    proporcionado para iniciar tu clúster de Cassandra
2. **Verifica el estado del clúster**. Asegúrate de que todos los nodos
    estén funcionando correctamente mediante `nodetool` (quizá tarde un
    poco).
3. **Acceso a Cassandra**. Conéctate al clúster de Cassandra usando
    `cqlsh` a través del primer nodo.

## 2. Creación de un Keyspace y Tablas

1. **Creación de un _keyspace_**: Crea un keyspace llamado `bbdd2` con
    la estrategia de replicación `SimpleStrategy` y un factor de
    replicación de 3.
2. **Uso del _keyspace_**: Cambia al keyspace universidad para que todas
    las operaciones posteriores se realicen en este keyspace.
3. **Creación de una tabla**: Crea una tabla `estudiantes` con campos
    para el `id` del estudiante, `nombre`, `edad` y `carrera`.

## 3: Inserción y consulta de datos

1. **Carga de datos**: Carga los datos relativos a los estudiantes en la
    tabla `estudiantes`.
2. **Consulta de datos**: Realiza una consulta para verificar que la
    inserción se realizó correctamente.

## 4: Actualización y borrado de datos

1. **Actualización de datos**: Actualiza la edad de un estudiante.
2. **Borrado de datos**: Elimina un registro de estudiante.

## 5: Limpieza y finalización

1. **Borrado de la tabla**. Elimina la tabla `estudiantes`.
2. **Borrado del _keyspace_**. Elimina el keyspace `bbdd2`.
