####################################################################
# Dependency: Diagram As Code
# Link: https://diagrams.mingrammer.com/docs/getting-started/installation
# Install: `pip install diagrams`
# Create Diagram: `python IACDiagramAsCode.py`
####################################################################

from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.programming.language import Go, Nodejs, Csharp, Python
from diagrams.programming.framework import React, Vue, Spring
from diagrams.onprem.database import Postgresql, Mongodb
from diagrams.onprem.workflow import Airflow
from diagrams.onprem.analytics import Superset

with Diagram("InvestmentAsCode_Architecture", show=False):
    with Cluster("Frontend Web App"):
      frontend_group = [React("React App"),
                        Vue("Vue App")]

    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("MicroService Group"):

      with Cluster("Experience APIs"):
          user_app = Go("User App")
          admin_app = Go("Admin App")
          # exp_group = [user_app, admin_app]

      with Cluster("Services APIs"):
          asset_service = Nodejs("Asset Services")
          stock_service = Spring("Stock Services")
          crypto_service = Csharp("Crypto Services")
          # svc_group = [asset_service, stock_service, crypto_service]

    with Cluster("Asset Flow Platform"):

      with Cluster("Batch Job Processing"):
          airflow = Airflow("Airflow")
          batch_job = Python("Batch Jobs")

      with Cluster("Data Storage"):
          postgresql = Postgresql("Postgresql DB")
          mongodb = Mongodb("Mongo DB")
          db_group = [postgresql, mongodb]

      with Cluster("Data Analysis"):
          superset = Superset("Superset")

      dal = Spring("Data-Access-Layer")

    frontend_group >> dns
    frontend_group >> lb

    lb >> user_app
    lb >> admin_app

    user_app >> asset_service >> dal
    user_app >> stock_service >> dal
    user_app >> crypto_service >> dal

    admin_app >> asset_service >> dal
    admin_app >> stock_service >> dal
    admin_app >> crypto_service >> dal

    airflow >> batch_job >> db_group
    postgresql >> dal
    postgresql >> superset

