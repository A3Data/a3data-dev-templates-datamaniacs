<p align="center">
  <a href="" rel="noopener">
 <img height=150px src="https://miro.medium.com/max/1024/0*SXvexwZvryFczrIG.png" alt="Project logo"></a>
</p>

<h3 align="center"> Template Apache Spark Notebook - A3Data</h3>

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

This apache spark template integrated with jupyter notebook, was developed to optimize the environment of our employees in relation to their local development environment.


### Prerequisites

Docker : [Docker Download](https://www.docker.com/products/docker-desktop)


## 🎈 Usage <a name="usage"></a>

- First clone the project
```bash
git clone git@github.com:A3Data/a3data-dev-templates-datamaniacs.git
```
- second go into the pyspark-notebook directory and run the command
```bash
docker-compose up -d
```
- finally, access your a3data-pyspark-notebook container logs and redeem your authentication token for the notebook
```bash
docker logs a3data-pyspark-notebook
```

## ✍️ Authors <a name = "authors"></a>

- [@carlosbpy](https://github.com/carlosbpy) - Idea & Initial work