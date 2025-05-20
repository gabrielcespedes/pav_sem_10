# **Proyecto Educativo: Integración de BigQuery y Amazon S3 con Python**

Este proyecto tiene como objetivo demostrar cómo conectar y trabajar con servicios de almancenamiento y análisis de datos en la nube utilizando Python. Se centra en la Extracción, Transformación y Carga (ETL) de datos entre Google BigQuery y Amazon S3, proporcionando una base práctica para quienes quieran familiarizarse con estos servicios.

## **Estructura del Proyecto**

pav_sem_10/ <br>
├── amazons3_python/ <br>
&nbsp; &nbsp;   ├── extract.py <br>
&nbsp; &nbsp;   ├── transform.py <br>
&nbsp; &nbsp;   ├── load.py <br>
&nbsp; &nbsp;   └── main.py <br>
├── bigquery_python/ <br>
&nbsp; &nbsp;   ├── extract.py <br>
&nbsp; &nbsp;   ├── transform.py <br>
&nbsp; &nbsp;   ├── load.py <br>
&nbsp; &nbsp;   └── main.py <br>
├── .gitignore <br>
└── README.md

```amazons3_python/```: contiene scripts para interactuar con Amazon S3

```bigquery_python```: contiene scripts para interactuar con Google Big Query

## **Requisitos**

- Python 3.7 o superior
- Bibliotecas de Python:
  - pandas
  - google-cloud-bigquery
  - boto3
- Credenciales de acceso para:
  - Google Cloud Platform (archivo JSON de cuenta de servicio)
  - Amazon Web Services (archivo CSV con claves de acceso)
- Dataset cargado en BigQuery y S3 con por lo menos columna ```Sales``` o ```total_sales```

## **Configuración**

1. Clonar el repositorio:
   ```
   git clone https://github.com/gabrielcespedes/pav_sem_10.git
   cd pav_sem_10   
   ```
2. Crear y activar un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   source venv/bin/activate # En Windows: venv/Scripts/activate
   ```
3. Instalar las dependencias:
   ```
   pip install pandas google-cloud-bigquery boto3 db-dtypes pandas-gbq   
   ```
4. Configurar las credenciales:
   - Google BigQuery:
     - Coloca el archivo JSON de la cuenta de servicio en una ubicación segura
     - Establece la variable de entorno ```GOOGLE_APPLICATION_CREDENTIALS``` con la ruta del archivo JSON
       ```export GOOGLE_APPLICATION_CREDENTIALES="/ruta/al/archivo.json"```
   - Amazon S3:
     - Coloca el archivo CSV con las claves de acceso en una ubicación segura
     - Configura las variables de entorno ```AWS_ACCESS_KEY_ID``` y ```AWS_SECRET_ACCESS_KEY``` con los valores correspondientes
       ```
       export AWS_ACCESS_KEY_ID="tu_access_key_id"
       export AWS_SECRET_ACCESS_KEY="tu_secret_access_key"
       ```
  **Asegúrate de que estos archivos de credenciales estén incluidos en ```.gitignore```**

## **Ejecución**

- BigQuery:
  ```
  cd bigquery_python
  python main.py
  ```
- AmazonS3:
  ```
  cd amazons3_python
  python main.py
  ```
Cada script ejecuta un flujo ETL: extracción de datos, transformación y carga al destino correspondiente.


