CREATE EXTERNAL TABLE IF NOT EXISTS sensordb.sensor_data (
  id string,
  timestamp string,
  temperature double,
  humidity double
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://sensor-data-export-ma/'
TBLPROPERTIES ('has_encrypted_data'='false');

