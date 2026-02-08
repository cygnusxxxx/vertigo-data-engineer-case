Vertigo – Data Engineer Case Study
Overview

This repository contains the solution for the Vertigo Games Data Engineer Case, consisting of two main parts:

Part 1: Backend API for clan management, deployed on Google Cloud Run

Part 2: Data modeling and visualization using BigQuery, dbt, and Looker Studio
The objective of this project is to transform raw user-level daily gameplay and monetization data into an aggregated analytics-ready model using dbt and Google BigQuery, and prepare it for business reporting and visualization.
 
This README documents the implementation steps, assumptions, and results.

Part 1 – Clan Management API

To run and test Part 1 locally, please read the following:
├── backend/
│   └── README.md

Description

A lightweight REST API was developed to manage clans in a game backend.
The API supports creating, listing, searching, and deleting clans.
All responses are returned in JSON format.

Each clan contains:

id (UUID)

name

region

created_at (UTC timestamp)

Tech Stack

Backend framework: Python (FastAPI)

API documentation: Swagger UI

Database: Cloud SQL (PostgreSQL / MySQL)

Deployment: Google Cloud Run

Containerization: Docker

API Endpoints
Method	Endpoint	Description

POST /clans → create clan

GET /clans → list clans

GET /clans/search?name= → contains + min 3 char

DELETE /clans/{id} → delete by UUID

 
Local Development & Testing
To run and test Part 1 locally, please read the following:
├── backend/
│   └── README.md

The project was developed and tested locally using VS Code.

 

Swagger UI

The API exposes a Swagger UI for interactive testing.

http://localhost:8080/docs


Using Swagger UI:

POST requests were used to create clans

GET requests were used to list and search clans

DELETE requests were used to remove clans by ID

Google Cloud Run Deployment

The API was containerized using Docker and deployed to Google Cloud Run.

Deployment steps:

Build Docker image

Push image to Google Artifact Registry

Deploy service to Cloud Run

Connect Cloud SQL instance to Cloud Run

After deployment, the API became publicly accessible via the Cloud Run service URL.

Example:

https://clan-api-xxxxxx.a.run.app


Swagger UI was also accessible via:

https://clan-api-xxxxxx.a.run.app/docs

Screenshots

Screenshots are included to demonstrate:

Swagger UI interface

Successful POST / GET / DELETE requests

Cloud Run service overview

<img width="1859" height="1000" alt="swagger" src="https://github.com/user-attachments/assets/362a6764-dccf-4c22-8cd8-3d85bf6385a5" />
 


Key Outcomes (Part 1)

Fully functional REST API

Cloud-native deployment using Google Cloud Run

Interactive API testing via Swagger

Clean, reproducible, and containerized setup


PART 2

Tech Stack

Google BigQuery – Data warehouse

dbt (dbt-bigquery) – Data modeling & transformations

Docker – Environment reproducibility

GitHub – Version control

Looker Studio – Visualization (covered in Part 2)

Project Structure
vertigo-data-engineer-case/
├── models/
│   └── daily_metrics.sql
├── models/sources.yml
├── dbt_project.yml
├── profiles.yml (local only, not committed)
├── Dockerfile
├── README.md

Data Source

Before modeling, basic data quality and anomaly checks were performed on the raw dataset.
These included duplicate user-day validation, null checks on key dimensions, negative value inspections on revenue and gameplay metrics, and logical consistency checks between match outcomes.
No critical data quality issues were identified.

The raw dataset consists of multiple .gz files containing user-level daily metrics, including:

user_id

event_date

install_date

platform (ANDROID / IOS)

country

gameplay metrics (sessions, matches, wins, defeats)

monetization metrics (iap_revenue, ad_revenue)

technical metrics (server_connection_error)

These files were uploaded to BigQuery into a raw dataset and exposed to dbt via a source configuration.

Data Quality & Initial Checks

Before modeling, basic sanity and quality checks were performed directly on the raw data in BigQuery, including:

Null checks on key dimensions (event_date, country, platform)

Validation of match-related metrics (e.g. match_end_count ≥ victory + defeat)

Revenue fields inspected for negative or unexpected values

Duplicate user-day records checked

These checks ensured the dataset was suitable for aggregation and business reporting.

DBT Model – daily_metrics

A single dbt model named daily_metrics was created to aggregate metrics by:

event_date

country

platform

Metrics Produced
Field	Description
event_date	Date of activity
country	User country
platform	User platform
dau	Daily Active Users
total_iap_revenue	Total in-app purchase revenue
total_ad_revenue	Total ad revenue
arpdau	(iap + ad) / dau
matches_started	Total matches started
match_per_dau	Matches started per DAU
win_ratio	victory_count / match_end_count
defeat_ratio	defeat_count / match_end_count
server_error_per_dau	server_connection_error / dau

The model is implemented as a view in BigQuery and serves as the foundation for downstream analytics and dashboards.

Dockerization

A Dockerfile is provided to ensure the dbt project is reproducible and environment-independent.

The Docker image installs Python and dbt-bigquery

Copies the dbt project into the container

Allows running dbt commands consistently across environments

Authentication to BigQuery is intentionally not baked into the Docker image for security reasons. Credentials are expected to be provided externally via mounted volumes or environment variables.

How to Run (Local)
dbt debug
dbt run

Visualization

A business-facing dashboard was built using Looker Studio, leveraging the daily_metrics model as the primary data source.

Screenshots and key insights are included below.

(Added in the next section)

Assumptions

Each user appears at most once per day

Revenue fields are already net and currency-consistent

Missing values in metrics are treated as zero where applicable

dbt models are intended for analytics/reporting, not transactional use

Versioning

The final version of this project is tagged as v1.0 in GitHub Releases.


SCREENSHOTS

 
PART 2 - VISUALIZATION

<img width="1504" height="683" alt="country" src="https://github.com/user-attachments/assets/c526f7cf-8241-4ce7-ae7f-acf4b22af153" />

<img width="1750" height="656" alt="country_win_ratio" src="https://github.com/user-attachments/assets/e350821e-6246-4ac5-a930-802f3ae2cb6b" />

<img width="1768" height="613" alt="country_defeat_winratio" src="https://github.com/user-attachments/assets/d6858d60-11cc-4ae2-a340-655665c3609b" />







