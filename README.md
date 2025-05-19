# 🛰️ Serverless Data Pipeline (API → Storage → Dashboard)

This project demonstrates how to build a fully serverless data analytics pipeline on AWS — from ingesting sensor data to visualizing it in a dashboard using QuickSight.

---

## 📌 Overview

| Component       | Service         |
|----------------|-----------------|
| Ingest API      | API Gateway + Lambda |
| Storage         | DynamoDB + S3   |
| Query Engine    | Athena          |
| Visualization   | QuickSight      |

---

## 🏗️ Architecture

```
API Gateway
   ↓
Lambda (store to DynamoDB)
   ↓
DynamoDB
   ↓ (Scheduled Lambda)
Lambda (export to S3)
   ↓
Amazon S3 (JSON)
   ↓
Athena
   ↓
QuickSight Dashboard
```

---

## ⚙️ Services Used

- **AWS Lambda** (Python)  
- **Amazon API Gateway**  
- **Amazon DynamoDB**  
- **Amazon S3**  
- **Amazon Athena**  
- **Amazon QuickSight**

---

## 📁 Project Structure

```
serverless-data-pipeline/
├── lambda_store_data/        # Lambda function to ingest data via API
│   └── lambda_function.py
├── lambda_export_to_s3/      # Scheduled Lambda to export data to S3
│   └── lambda_function.py
├── athena/                   # SQL script to define Athena table
│   └── create_table.sql
├── api-test/                 # curl command to test API
│   └── curl_command.txt
├── sample-output/            # Screenshots and exported sample JSON
│   ├── exported-data.json
│   ├── api-success.png
│   ├── s3-export.png
│   ├── athena-query.png
│   └── quicksight-chart.png
└── README.md
```

---

## 🧪 Sample curl Command

```bash
curl -X POST https://<api-id>.execute-api.us-east-1.amazonaws.com/StoreSensorData \
  -H "Content-Type: application/json" \
  -d '{"temperature": 72, "humidity": 45}'
```

Replace `<api-id>` with your actual API Gateway ID.

---

## 🔍 Athena Table DDL

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS sensordb.sensor_data (
  id string,
  timestamp string,
  temperature double,
  humidity double
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://sensor-data-export-ma/'
TBLPROPERTIES ('has_encrypted_data'='false');
```

---

## 📊 Dashboard Sample (QuickSight)

See Screenshots folder

---

## 🧹 Cleanup Checklist (To Avoid Charges)

- [ ] Delete Lambda functions
- [ ] Delete API Gateway stages
- [ ] Delete DynamoDB table
- [ ] Delete S3 bucket (if not needed)
- [ ] Delete Athena table (optional)
- [ ] Delete QuickSight dataset (optional)
- [ ] Optionally disable QuickSight in account settings

---

## 💡 Use Cases

- IoT data collection & reporting  
- Real-time analytics pipelines  
- Lightweight dashboards without EC2 or containers

---

## 📬 Contact

**Author**: Madhu (AWS Certified Cloud & DevOps Engineer)  
**Location**: St. Louis, Missouri  
**GitHub**: https://github.com/madhusudhan-anand

---

## ⭐️ If you liked this project...

Give it a ⭐️ on GitHub and connect with me on LinkedIn:www.linkedin.com/in/madhusudhananand !

