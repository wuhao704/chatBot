# chatBot

![image](https://img.shields.io/badge/python-3.6.3-blue.svg)![image](https://img.shields.io/badge/django-2.1.3-blue.svg)![image](https://img.shields.io/badge/tensorflow-1.12.0-brightgreen.svg)![image](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)

A robot that you can chat with him on the web page, but you might think he is stupid.

Table of Contents
=================

* [<a id="user\-content\-chatbot" href="\#chatbot"></a>chatBot](#chatbot)
  * [<a id="user\-content\-requirement" href="\#requirement"></a>Requirement](#requirement)
  * [<a id="user\-content\-screenshot" href="\#screenshot"></a>Screenshot](#screenshot)
  * [<a id="user\-content\-before\-you\-start" href="\#before\-you\-start"></a>Before you start](#before-you-start)
  * [<a id="user\-content\-start" href="\#start"></a>Start](#start)
  * [<a id="user\-content\-reference" href="\#reference"></a>Reference](#reference)
  * [<a id="user\-content\-license" href="\#license"></a>License](#license)



## Requirement

- Python: 3.6.3

- Django: 2.1.3

- Tensorflow: 1.12.0

## Screenshot

![image](https://github.com/wuhao704/chatBot/blob/master/screenshot.png)


## Before you start

Make sure your environment is correct. Especially the version of python, This project is not support the python 3.7.0 and later, and if your version of python is 3.7.0 or later, I suggest you use the [pyenv](https://github.com/pyenv/pyenv#installation) or [virtualenv](https://virtualenv.pypa.io/en/latest/installation/) to control version. The version of django and tensorflow is also significant.

If you are interested in the machine learning part of this project, like how it works and what model is based on, or other details, you can check in this link: https://github.com/bshao001/ChatLearner .

## Start

- Step 1:

  `git clone https://github.com/wuhao704/chatBot.git`

- Step 2:

  `cd chatBot/chatchat`

  Find the file named 'chatServer.py' and edit it, then you have to modify the path to your local path in line 19 and save it.

  `python3 chatServer.py`

  Don't worry if you see some errors after running that command, it might due to you have not installed some packages. Then you just use `pip3` to install package that the error pointed.

  You may wait a long time when you first run the command because it might download the nltk_data ([ NLTK: Natual Language Toolkit](https://www.nltk.org/)).

  After that, you have to keep the program running. Than you have to start a new session to run django server.

  ```shell
  cd chatBot
  python3 manage.py runserver 0.0.0.0:8081
  ```

  Note: the port 8081 is not important, you can change it to others. The default port is 8080.

- Step 3:

  Open your web browser and enter `127.0.0.1:8081/chatchat/` in the address bar. 

  If this project is in your virtual machine and you want to use it on the host machine, then you should modify the `127.0.0.1` to your VM's IP address.

- Step 4:

  Congratulations, you can chat with him on the web page. Enjoy it.

## Reference

The machine learning part: https://github.com/bshao001/ChatLearner

## License

[Apache License 2.0](https://github.com/wuhao704/chatBot/blob/master/LICENSE)









