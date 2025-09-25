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
````

---

## 🛠️ Tools & Technologies

* **Azure Event Hub** → Real-time data ingestion
* **Azure Databricks** → PySpark-based ETL processing
* **Azure Data Lake Storage (ADLS Gen2)** → Data lake (Bronze, Silver, Gold)
* **Azure Synapse SQL Pool** → Data warehouse for analytics
* **Power BI** → Dashboarding & reporting
* **Python 3.9+** → Data simulation
* **Git** → Version control

---

## 📐 Data Architecture

The solution follows a **multi-layered lakehouse architecture**:

* **Bronze Layer** → Raw JSON data from Event Hub.
* **Silver Layer** → Cleaned & structured data (type validation, null handling).
* **Gold Layer** → Aggregated & transformed data ready for BI consumption.

### 🔹 Architecture Diagram

![Data Engineering Pipeline](./199e1604-89eb-4301-b216-652c586b06e0.png)

---

## ⭐ Star Schema Design

The **Gold layer** in Synapse follows a **Star Schema**:

**Fact Table**

* `FactPatientFlow` → patient visits, timestamps, length of stay, bed usage

**Dimension Tables**

* `DimPatient` → patient demographics
* `DimDepartment` → hospital departments
* `DimTime` → calendar & time breakdown

---

## ⚙️ Step-by-Step Implementation

1. **Event Hub Setup**

   * Created Event Hub namespace & `patient-flow` hub.
   * Configured consumer groups for Databricks streaming.

2. **Data Simulation**

   * Python script `patient_flow_generator.py` simulates patient events (departments, admissions, discharges, wait times).

3. **Storage Setup**

   * Configured **ADLS Gen2** with `bronze/`, `silver/`, `gold/` containers.

4. **Databricks Processing**

   * **Bronze Notebook** → Reads raw JSON from Event Hub.
   * **Silver Notebook** → Cleans & validates schema.
   * **Gold Notebook** → Aggregates into fact & dimension tables.

5. **Synapse SQL Pool**

   * Created **dedicated SQL Pool**.
   * Implemented **fact/dimension schema** via SQL scripts.

6. **Version Control with Git**

   * All notebooks, scripts, and queries tracked in GitHub.

---

## 📊 Data Analytics

### 🔗 Synapse → Power BI Connection

* Connected **Azure Synapse SQL Pool** directly to **Power BI**.
* Imported **FactPatientFlow** + dimension tables.
* Established schema relationships.

### 📈 Dashboard Features

* **Bed Occupancy Rate** by department & gender.
* **Patient Flow Trends** (admissions, wait times).
* **Length of Stay Analysis**.
* **Interactive Filters & Slicers** (gender, department).

### 🔹 Power BI Dashboard

![Patient Flow Dashboard](./13f88a9c-8336-4ccc-bdf8-cb58b49cac1e.png)

---

## ✅ Key Outcomes

* **End-to-End Pipeline** → Real-time ingestion → ETL → Warehouse → BI.
* **Scalable Architecture** → Extensible for other hospital datasets.
* **Actionable Insights** → Hospital admins can monitor:

  * Bed usage rates
  * Patient admission trends
  * Department efficiency
* **Portfolio Project** → Demonstrates both **Data Engineering** + **Analytics** expertise.

---

## 
Author: Muhammad Afzal

LinkedIn: www.linkedin.com/in/muhammad-afzal-7594581a9

Contact: hmafzal@gmail.com
```
