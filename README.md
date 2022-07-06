<br>

<h1 align="center"><img src="https://i.ibb.co/JKk0jcM/image.png" width='130'><br>opiTranslate</h1>

<p align="center"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"><img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"><img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"><img src="https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"></p>

<br>

## opiTranslate

Opground's platform was born to connect talent from all over the world. At first, they decided to go for Spanish and Latin American talent to connect them with Spanish companies. However, new companies from the United States and other countries have been using Opground and now expect to see interviews in English.

This is how opiTranslate was born, as a solution within the web site in which companies can translate the interviews of their candidates from any language preference to English or any other language. For this, a back-end was developed with Python and Flask that connects with the AWS Translate API service, and a front-end that preserves the Opground graphical interface. The DevOps pipeline was also implemented to automate the integration of basic software testing using Docker and GitHub Actions, as well as the automation of the application deployment with AWS EC2 and Nginx. You can visit the site at [opitranslate.holbie3815.tech](http://opitranslate.holbie3815.tech)

## Overview

The Holberton School teaches Computer Science Fundamentals with a project-based approach. This Capstone Project covers the high-level programming skills with emphasis on backend, frontend, cloud and devops acquired during the three trimesters of the program. It is developed under the guidance and supervision of the startup [Opground](https://opground.com/).

## Requirements

- [Python 3+](https://python.org/) installed on the system
- Able to write basic commands on a terminal window (macOS, Linux or Windows)

To run the app you'll need to download the code files by clicking [Download opiTranslate](https://github.com/mekona-hbtn/opiTranslate/archive/refs/heads/main.zip) or by cloning this repository with the following command in your command terminal. The result will be the same regardless of the option you choose.

```bash
~$ git clone https://github.com/mekona-hbtn/opiTranslate.git
~$ cd opiTranslate
```

### Creation of the virtual environment

Before running the application it is necessary to set up a virtual work environment. For our project, we follow the recommended procedure of working with [virtual environments](https://docs.python.org/3/tutorial/venv.html) with these simple steps.

- In a terminal window, execute the following commands to create and activate a virtual environment:

```bash
# macOS or Linux
~/opiTranslate$ python3 -m venv venv
~/opiTranslate$ source ./venv/bin/activate

# Windows
~\opiTranslate$ py -3 -m venv venv
~\opiTranslate$ .\\venv\\Scripts\\activate
```

- Finally, the dependency packages are installed inside the virtual environment:

```bash
# macOS, Linux or Windows
(venv) ~/opiTranslate$ pip install -r requirements.txt
```

### Linux-based environments

By default, opiTranslate is configured to run on a Linux-based environment such as `Ubuntu 20.04 LTS`. If this is your case, move to the `Invocation` section.

### Windows-based environments

Before running the application be sure to set the following environment variables:

```powershell
(venv) ~\opiTranslate$ env:FLASK_APP = "app"
(venv) ~\opiTranslate$ env:FLASK_ENV = "production"
```

## Invocation

Now we are ready to run opiTranslate typing the flask run command:

```bash
# macOS, Linux or PowerShell
(venv) ~/opiTranslate$ flask run
```

<br>

## Authors

Made with 💟 by the Holbies...

| [<img src="https://avatars.githubusercontent.com/u/87556519" width="110" style="border-radius: 50%"><br><sub>Johanna Alfonso<br><sup>@viajeradelaluz](https://github.com/viajeradelaluz) | [<img src="https://avatars.githubusercontent.com/u/91074465" width="110" style="border-radius: 50%"><br><sub>Ornella Russo<br><sup>@Ella711](https://github.com/Ella711) | [<img src="https://avatars.githubusercontent.com/u/91083840" width="110" style="border-radius: 50%"><br><sub>Alejandro Pineda<br><sup>@apinedas](https://github.com/Apinedas) | [<img src="https://avatars.githubusercontent.com/u/91047947" width="110" style="border-radius: 50%"><br><sub>Felipe Leon<br><sup>@pipeleon](https://github.com/pipeleon) |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------: |

## More information

[Opground](https://opground.com/) | [Holberton School](https://www.holbertonschool.com/)
