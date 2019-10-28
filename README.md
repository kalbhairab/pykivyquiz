# PyKivyQuiz

Descripiton
This is a quiz app written with python3 and Kivy.

If you want to run app. Then download "main.py", "question_answer.py" and "test.ky".

#If you want to make any new type of app from this app then
1. Put txt file in "Put text file here" folder encoding should be utf-8 and pattern should be as text file put there
2. open "1. run first.py" and run.
	you will get "2. copy_paste.py" and "question_answer.py".
3. open "2. copy_paste.py" and copy the items as described in cmt in "main.py" and "test.kv" file.
4. run "main.py". If it says it cant find any thing run again and again for 3 to 5 times.
	I don't know this is bug or what but it worked in python2 well
5. copy "main.py", "question_answer.py" and "test.ky" in seperate folder for making full app.
6. for running in android using pydroid comment as "#Window.size = (340 ,550)" of main.py

Note:- make test.kv in small letter as linux is case sensitive

To make Apk
-----------

1. download oracle virtualbox
2. download ubuntu iso image
3. run ubuntu in virtualbox
4. download install-kivy-buildozer-dependencies.sh
5. open terminal in ubuntu where above file is located
6. paste these in terminal
####chmod +x install-kivy-buildozer-dependencies.sh
----------------------------------------------------
####./install-kivy-buildozer-dependencies.sh
------------------------------------------------
7. If Android dependencies are outdated execute:
#buildozer android update
