**Proyecto: Automatización de Extracción e Ingesta de Datos de Ligas de Fútbol Europeas**

Este proyecto implementa un flujo de trabajo automatizado que extrae datos de ligas de fútbol europeas, los procesa y los ingesta en una tabla de Snowflake utilizando las siguientes tecnologías:

Airflow para la orquestación del flujo de trabajo.

Docker para la contenedorización y facilidad de despliegue.

Snowflake como almacén de datos en la nube.

**Características del Proyecto**

Extracción Automatizada: Los datos de ligas de fútbol se obtienen de una fuente especificada (archivo local, API o base de datos).

Transformación y Validación: Los datos son procesados para asegurar calidad y consistencia antes de la carga.

Ingesta a Snowflake: Los datos transformados se cargan en una tabla designada en Snowflake.

Escalabilidad: La configuración basada en Docker permite un despliegue fácil en cualquier entorno.

**Tecnologías Utilizadas**

Airflow:

Se utiliza para coordinar tareas mediante DAGs (Directed Acyclic Graphs).

Permite programar la extracción, transformación e ingesta de los datos.

Docker:

Contenedores para el despliegue del entorno Airflow.

Simplifica la configuración y garantiza consistencia entre entornos de desarrollo y producción.

Snowflake:

Base de datos en la nube utilizada para almacenar los datos transformados.

Permite realizar análisis de datos de manera escalable y eficiente.