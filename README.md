# 🎤 J-Pop Idol Data Platform

![Postgres](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?logo=python)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Status](https://img.shields.io/badge/status-in%20progress-orange)

A relational data platform that models **Japanese idol groups, agencies, and career histories**, focusing on STARTO Entertainment and EBiDAN.

The system transforms fragmented public information into a **structured, queryable dataset for temporal and relational analysis**.


## 🧠 System Purpose

Public idol data is scattered, inconsistent, and not structured for analysis.

This project builds a unified data layer that enables:

* Group membership evolution over time
* Idol career progression tracking
* Agency-level structural analysis
* Historical reconstruction of idol group lineups


## 🏗️ System Architecture

```text id="s1"
External Sources
      ↓
Ingestion Layer (planned)
      ↓
PostgreSQL (core storage)
      ↓
SQL Analytics Layer
      ↓
API / Dashboard (planned)
```


## 🧱 Data Model Overview

```text id="s2"
Agencies ───< Groups ───< Memberships >─── Idols
                             │
                             ├── Career Events
                             └── Works ───< Idol Works
```

#### Core Concepts

* **Idols**: Individual performers
* **Groups**: Idol groups under agencies
* **Memberships**: Time-based group participation (core fact table)
* **Career Events**: Milestones (debut, hiatus, etc.)
* **Works**: Songs, albums, media appearances


## ⚙️ Tech Stack

* Python (data pipeline + backend logic)
* PostgreSQL (relational storage)
* SQL (schema + analytics queries)
* SQLAlchemy (database interface)
* Docker (environment management)


## 🗂️ Project Structure

```text id="s3"
sql/        → schema migrations
src/
  core/     → database infrastructure
  ingestion/→ ETL pipelines (planned)
  api/      → future service layer

data/       → raw & processed datasets
notebooks/  → exploration & analysis
```


## 📊 Key Design Principles

* **Normalization-first design** to avoid redundancy
* **Temporal modeling** for group membership history
* **Event-based structure** for career milestones
* **Query-driven schema design** for analytics use cases


## 🔍 Example Questions Enabled

* Who was in a group at a specific point in time?
* How do idol careers progress across groups?
* Which agency produces the most stable groups?
* What are the most active periods in an idol’s career?


## 🐳 Containerized Development

The project now ships with a VS Code dev container and a Docker Compose setup for the app plus PostgreSQL.

On a Windows machine, the workflow is:

1. Install Docker Desktop and VS Code.
2. Open this folder in VS Code.
3. Use the command to reopen the folder in the dev container.

That gives you the same Python environment, dependencies, and database service without installing Python or PostgreSQL locally.

To run the pipeline inside the container, use the integrated terminal and launch the same module command you already use, for example:

```bash
PYTHONPATH=./src python -m ingestion.pipelines.group_pipeline
```

## 🚀 Future Work

### Data Engineering

* Build ingestion pipelines for STARTO and EBiDAN data
* Integrate external sources (wikis, official announcements)
* Automate cleaning, validation, and updates

### Event & Calendar Layer

* Unified event system for releases, birthdays, debuts, and milestones
* Derived calendar views over relational data
* Support for upcoming activities and historical timelines

### Analytics Layer

* Cohort and generation analysis
* Group stability and turnover metrics
* Career trajectory modeling

### Product Layer

* REST API for idol and group queries
* Calendar endpoint for events and releases
* Dashboard for timeline visualization


## 🧠 Key Insight

This project demonstrates how **fragmented cultural data can be transformed into a structured, time-aware analytical system using data engineering principles.**
