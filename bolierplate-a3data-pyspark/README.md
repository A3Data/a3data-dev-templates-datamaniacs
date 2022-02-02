![img](https://github.com/A3Data/a3data-dev-templates-datamaniacs/blob/main/bolierplate-a3data-pyspark/docs/img/tools.png)

<h3 align="center"> Boilerplate Apache Spark - A3Data</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## 📝 Table of Contents

- [About](#about)
- [Usage](#usage)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This is a design pattern, for development using spark locally, with dependency management using poetry, automating commands with Makefile, automated testing with Pytest, data processing with Spark and container using Docker.


### Prerequisites

Apache Spark : [Docker Download](https://spark.apache.org/) \
Poetry: [Poetry Download](https://python-poetry.org/docs/) \
Docker : [Docker Download](https://www.docker.com/products/docker-desktop) \
Docker-compose: [Docker Compose Download](https://docs.docker.com/compose/install/)


## 🎈 Usage <a name="usage"></a>

- First clone the project
```bash
git clone git@github.com:A3Data/a3data-dev-templates-datamaniacs.git

cd bolierplate-a3data-pyspark
```
- Run commands
```bash
make package
make build-docker
make run
make test-docker
```

## ✍️ Authors <a name = "authors"></a>

- [@carlosbpy](https://github.com/carlosbpy)