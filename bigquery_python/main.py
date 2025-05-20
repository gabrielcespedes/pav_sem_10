import config

from extract import extract_from_bigquery
from transform import add_discount
from load import load_to_bigquery

#consulta a ejecutar
query ="""
SELECT * FROM `analog-button-435120-c7.id_data_raw.sales_table`
"""

#parámetros de carga
project_id = "analog-button-435120-c7"
table_id = "id_data_raw.sales_table"

#Proceso ETL
df = extract_from_bigquery(query)
df_transformed = add_discount(df)
load_to_bigquery(df_transformed, table_id, project_id)

print("Proceso ETL finalizado.")