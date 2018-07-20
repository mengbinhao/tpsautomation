### 1 skeleton

- bin

- doc

- tpsautomation下    common、module、operation、module、utils

- report (static generate)   (bottle  / PyH / jinja2)

- tpsautomation\testcases    testcases

- tpsautomation\test      unittest

  


### 2 requirements

- use some application to check your app backend (win32 or uia) under gui-inspect-tool folder

- python 3.6.5

- pytest (pytest-html、pytest-rerunfailures)

- pywinauto

- pyautogui

- add  PYTHONPATH=C:\Users\xxxxxx\Desktop\tpsautomation to path (so can find custom module and use pytest)

  ```
  # locate to rootdir of pytest, this also is root of project
  # then find test.py to excute
  PS C:\Users\XXX\Desktop\tpsautomation> pytest .\tpsautomation\test\utils\test_dictutils.py
  ```


### 3 specification  

1. 包名、模块名、局部变量名、函数名 (全小写+下划线)

   example：this_is_var

2. 全局变量 (全大写+下划线)

   example：GLOBAL_VAR

3. 类名 (首字母大写式驼峰)

   example：ClassName()


### 5 TPS  requirement

1. Win 7 professional 64 bit
2. font size (100%, system recommend)
3. monitor  resolution (1920 * 1080)
4. if locate with coordinate, software must not change UI
5. can not use two monitor, the display location of app is weird

### 6 Transfer

1.  install python (maybe more than one version)
    - add to path
    - install virtualenv and virtualenvwrapper-win
    - create mkvirtualenv  for project and install third lib

2.  install vscode 
    -   copy extensions
    -   copy and change setting.json、launch.json (point to virtualenv) for this project

3.  install Typora ( change max-width)    

4.  install node、git if needed

    

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
    git clone https://git.oschina.net/name/test.git
    ```

5.  change project
    -   change C:\Users\computer_name  to  new computer_name in project file  (*.py  .ini)

    -   change TPS location in project files (.ini)






