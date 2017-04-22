Personal Stock Alerts and DataViz
=========================

This is a work-in-progress


The Project
------------

All the things:
- ElasticSearch single-node on AWS EC2 (medium, I think)
- Kibana running on the same instance
- AWS loadbalancer instance
- AWS RDS PostgreSQL instance
- Python 3 scripts running on cron jobs:
  - Fetch data from a finance API
  - Run data through risk model and price/dividend alert filters
  - Email and text message notifications on alerts
  - Store raw data and some computed data in ES and Postgres

Notes:
------------
- Running an ElasticSearch cluster on AWS is expensive.  I initially had a three-node ES cluster.  I have since reduced it to one to save costs and it is still quite expensive.  I might remove the ES stuff and add my own dataviz dashboard later unless I find a good way to turn off ES processes and reliably turn them back on when I request the site.
- Risk model will not be made public.

