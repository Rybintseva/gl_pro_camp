# Welcome to the GL ProCamp project

## Description

The project contains UI and API tests for [CosmosID](https://www.cosmosid.com/)

##Instruments used:

* Selenium Webdriver

* Pytest

* Docker

## Requirements

* Python 3.6+

* Packages from requirements.txt

## How to run tests

* Clone the project

Before, make sure there is an [SSH key](https://gitlab.com/profile/keys)

`git clone git@github.com:Rybintseva/gl_pro_camp.git`

* Run tests in terminal

`pytest tests/tests_ui/test_mainpage.py`

## Tasks

* Framework
1. Create framework structure

1.1. It shall contain folders for configuration, application specific libraries/helpers, app api clients, page objects, tests
2. Create Config class

2.1. It shall be possible to set config variables via Environment variables

2.2. It shall be possible to set config variables via YAML file

2.3. It shall be possible to set config variables inside Config class
3. Create class for sending HTTP requests 

3.1. It shall be able to send GET, PUT, POST, DELETE requests

* Api tests
1. Create API web client 

1.1. Use CID specs from last tab in document
2. Create 2-4 API tests for each endpoint

2.1. Using fixtures/before/aftertests is mandatory
2.2. Tests shall not contain hardcode
   
* Selenium
1. Create base class
2. Create some pages
3. Create some tests

* Docker

### How to run tests from Docker

* Install **Docker**.

[Install Docker](https://docs.docker.com/engine/install/)

On **Linux**: [Create a Unix group called `docker` and add user to it.](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)

* Clone the project.

`git clone git@github.com:Rybintseva/gl_pro_camp.git`

* Run tests on **Linux**:

`bash run_docker.sh`

* Run tests on **Windows**:

`run_docker.cmd`

**Note:** Command should be run from the **project root folder**.

* Test Report

Open the **report.html** file to see the report.
