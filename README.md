# 🏥 Real-Time Patient Flow Analytics on Azure  

## 📑 Table of Contents  
- [📌 Project Overview](#-project-overview)  
- [🎯 Objectives](#-objectives)  
- [📂 Project Structure](#-project-structure)  
- [🛠️ Tools & Technologies](#-tools--technologies)  
- [📐 Data Architecture](#-data-architecture)  
- [⭐ Star Schema Design](#-star-schema-design)  
- [⚙️ Step-by-Step Implementation](#-step-by-step-implementation)  
- [📊 Data Analytics](#-data-analytics)  
- [✅ Key Outcomes](#-key-outcomes)  
- [📜 License](#-license)  

---
## 📌 Project Overview  
This project demonstrates a **real-time data engineering pipeline for healthcare**, designed to analyze **patient flow across hospital departments** using **Azure cloud services**.  

The pipeline ingests **streaming patient events**, processes them in **Azure Databricks (PySpark)**, and stores curated data into **Azure Synapse SQL Pool** for **analytics and visualization with Power BI**.  

**Workflow:**  
1. Real-time ingestion via Event Hub.  
2. Transformation and cleansing in Databricks (Bronze → Silver → Gold).  
3. Load into Synapse SQL Pool.  
4. Build dashboards in Power BI.  

---
## 🎯 Objectives  
- Collect **real-time patient data** via Azure Event Hub.  
- Process and cleanse data using **Databricks (PySpark)**.  
- Organize curated datasets into a **Star Schema** in Synapse.  
- Enable **version control** with Git.  
- Visualize **hospital KPIs** in **Power BI**.  

---

## 📂 Project Structure  
```bash
real-time-patient-flow-azure/
│
├── databricks-notebooks/        # Transformation notebooks
│   ├── 01_bronze_rawdata.py
│   ├── 02_silver_cleandata.py
│   └── 03_gold_transform.py
│
├── simulator/                   # Data simulation scripts
│   └── patient_flow_generator.py
│
├── sqlpool-queries/             # SQL scripts for Synapse
│   └── SQL_pool_queries.sql
│
├── git_commands/                # Git version control commands
└── README.md                    # Project documentation

🛠️ Tools & Technologies

Azure Event Hub → Real-time data ingestion

Azure Databricks → PySpark-based ETL processing

Azure Data Lake Storage (ADLS Gen2) → Data lake (Bronze, Silver, Gold)

Azure Synapse SQL Pool → Data warehouse for analytics

Power BI → Dashboarding & reporting

Python 3.9+ → Data simulation

Git → Version control

📐 Data Architecture

The solution follows a multi-layered lakehouse architecture:

Bronze Layer → Raw JSON data from Event Hub.

Silver Layer → Cleaned & structured data (type validation, null handling).

Gold Layer → Aggregated & transformed data ready for BI consumption.
