### 1 skeleton

- bin 可执行文件
- doc
- tpsautomation    src、module
- tpsautomation\test      test related
- report (static generate)   // static  / bottle  / PyH / jinja2


### 2 requirements

- use some application to check your app backend under gui-inspect-tool folder

- python 3.6.5

- pytest (pytest-html、pytest-rerunfailures)

- pywinauto

- pyautogui

- add path C:\Users\XXX\Desktop\tpsautomation for looking  project package

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
3. monitot  resolution (1920 * 1080)
4. if locate with coordinate, software must not change UI
5. can not use two monitor, the display location of app is weird

### 6 Transfer

1.  install python (maybe more than one version)
    - add to path
    - install virtualenv and virtualenvwrapper-win
    - create mkvirtualenv  for project and install third lib
2.  install vscode 
    -   copy extensions
    -   copy and change setting.json、launch.json (point to virtualenv)
3.  install Typora ( change max-width)    
4.  install node、git、GitHub Desktop if needed
5.  change project
    -   change C:\Users\computer_name  to  new computer_nme in project file

    -   change TPS location in project files

    -   add PYTHONPATH=C:\Users\xxxxxx\Desktop\tpsautomation to path (so can find custom module and use pytest)

        eg: pytest -s .\tpsautomation\test\model\test_case.py





