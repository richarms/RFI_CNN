# RFI CNN

### Identification (/classification) of foreground radio interferers in astronomical radio data

### --

To build the project, run `docker-compose build`

## ETL - Train - Serve

![title](https://github.com/richarms/galaxyGAN/blob/master/images/ETL_Train_Serve.png)

## Airflow

In order to automate and monitor the full ETL - Train - Serve process, the airflow task manager is used, operating on Docker images directly. to set up airflow for the project, go into the airflow directory and edit the DAG template to point to the docker containers build above. Then, run `docker-compose up` in the airflow directory to launch airflow

![title](https://github.com/richarms/galaxyGAN/blob/master/images/airflow.png)

