### 1  Skeleton

- bin

- doc

- tpsautomation下    common、module、operation、module、utils

- report (static generate)   (bottle  / PyH / jinja2)

- tpsautomation\testcases    testcases

- tpsautomation\test      unittest

- report 

- logs

- other

- pytest.ini  /  logger.conf  / conf.ini  / README.md

  


### 2  Requirements

- use some application to check your app backend (win32 or uia) under gui-inspect-tool folder

- python 3.6.5

- python lib

  - pytest (pytest-html、pytest-rerunfailures)
  - pywinauto
  - pyautogui
  - autopep8  (format py code     vscode -> setting.json --> "python.formatting.provider": "autopep8")      ( other format lib yapf / black)
  - pylint   (use .pylintrc to static check py)   (other lint lib flake8 / mypy / pep8 / prospector / pydocstyle / pylama)
  - virtualenv and  mkvirtualenv  

- vscode plugin

  - rope、python

- add  PYTHONPATH=C:\Users\xxxxxx\Desktop\tpsautomation to path (so can find custom module and use pytest)

  ```
  # locate to rootdir of pytest, this also is root of project
  # then find test.py to excute
  PS C:\Users\XXX\Desktop\tpsautomation> pytest .\tpsautomation\test\utils\test_dictutils.py
  ```



### 3  Specification  

1. 包名、模块名、局部变量名、函数名 (全小写+下划线)

   example：this_is_var

2. 全局变量 (全大写+下划线)

   example：GLOBAL_VAR

3. 类名 (首字母大写式驼峰)

   example：ClassName()



### 4 TPS  requirement

1. desktop monitor resolution (1920 * 1080)
2. Win 7 professional 32/64 bit
3. font size (system recommend), can not be changed
4. unnormal alert box (like user has login, unnormal exit confirm)
5. can not use two monitor, the display location of app is weird



### 5 Note

1.  input method default is  english language

2.  UI can not be changed because locate with coordinate

3.  app UI must at the top of screen, so can click it

4.  can not popup any box to change the focus (like update system/software、usb alert popup) 

5.  screen can not be locked

      

### 5 Transfer

1.  install python (maybe more than one version)
    - add to path
    - install virtualenv and virtualenvwrapper-win
    - create mkvirtualenv  for project and install third lib

2.  install vscode 
    -   copy extensions
    -   copy and change setting.json、launch.json (point to virtualenv) for this project

3.  install Typora ( change max-width)    

4.  install node、git if needed

  ​    

    ```
    git config --global user.name "xxxx" 
    git config --global user.email "xxxx@yyy.com"
    git config --global credential.helper store   //在Git Bash输入这个命令就可以了
    ```
    ```
    //new project
    mkdir wap
    cd wap
    git init
    type nul>xxx
    git add xxx
    git commit -m "first commit"
    git remote add origin https://xxxxxxxxxxxxxx/package.git
    git push -u origin master
    
    //exist project
    cd existing_git_repo
    git remote add origin https://xxxxxxxxxxxxxx/package.git
    git push -u origin master
    
    //clone
    git clone https://xxxxxxxxxxxxxxxxxxxx.git
    
    //when local is not sync with remote
    1 git pull origin master
    2 there ways to do
    	git reset --hard origin/master   //sync remote to local, override local
    	git add filename ->  git commit -m "message" --> git push -u origin master //sync local to remote
    	git reset --hard HEAD // back to before merge
    
    //find each HEAD to reset
    git reflot
    git reset --hard  version
    ```

5.  change project

    -   change C:\Users\computer_name  to  new computer_name in project file  (*.py  .ini)

    -   change TPS location in project files (.ini)

    -   pylint ./tpsautomation/   +  .pylintrc

    -   pytest ./tpsautomation/test + pytest.ini   

        pytest ./tpsautomation/test/ --html=C:/Users/XXXX\Desktop/tpsautomation/tpsautomation/test/log/result.html

    -   create a shortcut of tps.bat file (adjust the window location property)

        

### 6 Problem

1.  can not get return value from subprocess

2.  can not pass global param to subprocess

3.  can not create break point in subprocess while running main.py

4.  can not catch real exception from  mouse click or type write use pyguiauto

    

### 7 TODO

1.  integrate with jenkens (create slave, item, invoke main.py)
2.  abstract exception
3.  wrapper a context object
4.  hanle any unnormal tps popup box













