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
