#  Spark + Jupyter + Cassandra (externo)

Este entorno Docker te permite trabajar con Apache Spark y Jupyter Notebook, conectándote a una instancia de Cassandra **que ya tienes ejecutando por separado** (fuera del `docker-compose`).

---

## 📁 Estructura

```
spark-jupyter-cassandra/
├── docker-compose.yml
├── Dockerfile
└── notebooks/
    └── estudiantes_spark.ipynb
```

---

## 🚀 Cómo usar

### 1. Requisitos previos

- Tener Docker y Docker Compose instalados
- Tener Cassandra corriendo en tu máquina (puerto 9042)

> ⚠️ Si usas Linux, asegúrate de que tu Cassandra local acepte conexiones desde Docker. Si tienes problemas, puedes editar `spark.cassandra.connection.host` en el notebook y usar tu IP local en vez de `host.docker.internal`.

---

### 2. Levantar el entorno

```bash
docker compose up --build
```

Esto levantará:
- Apache Spark (master)
- Jupyter Notebook (con PySpark + conector Cassandra)
- Spark UI accesible en http://localhost:4040

---

### 3. Acceder a Jupyter
Si es la primer vez que te conectas:
- Una vez que tengas los contenedores corriendo (`docker compose up`), ejecuta:
```bash
docker logs jupyter 2>&1 | grep token
```

obtendras algo como:
```bash
http://127.0.0.1:8888/lab?token=db654e9757573e7406fb1acf5887c7315757786414a6cf30
```
copia y pega esa URL y accederás directamente. Si No es la primera vez: [http://localhost:8888](http://localhost:8888)

Encuentra el notebook `estudiantes_spark.ipynb` dentro de la carpeta `work/`.

---

### 4. Notebook de ejemplo

El notebook realiza lo siguiente:

- Se conecta a Cassandra (`host.docker.internal`)
- Lee la tabla `estudiantes` del keyspace `bbdd2`
- Muestra las 10 primeras filas
- Agrupa por carrera y cuenta estudiantes

Puedes modificarlo para hacer análisis más avanzados.

---

## ✅ Extras

- Si quieres guardar resultados en CSV:
```python
df.write.csv("/home/jovyan/work/estudiantes_output.csv", header=True)
```

- Si quieres hacer gráficos, puedes usar `matplotlib` o `pandas` después de `df.toPandas()`.

---

¡Feliz análisis! ✨
