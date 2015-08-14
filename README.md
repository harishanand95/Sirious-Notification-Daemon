# Sirious-Notification
###UPDATE:
Currently a better user friendly version is under development. The name of the project will be changed.
  1. The newer version will have voice commands
  2. Search feature - clipboard search feature also included
  3. Personal Assistant - community driven entity and intents using supervised ML.  
  4. It wont be using the Dbus notification.
  5. Cinnamon bugs will be fixed.

Future version: 
![alt tag](https://docs.google.com/uc?authuser=0&id=0B_MVpqqghjpia0t4WGJaOWxrUnM&export=download)
The above pic is only a representation of currently developing app.The actual app can be different.

###Sirious-Notification-Daemon
Sirious is a linux application that lets you search for any selected content (primary clipboard content) on DuckDuckGo and gives its best result as a notification.
Sirious can be given as keyboard shortcut and thus it becomes easier to search content.


###How it works! 
1. Once installed, Sirious will be a terminal command
2. Give Sirious a keyboard Shortcut in System > Preferences(Settings) > Keyboard > Keyboard Shortcuts say Alt+x
3. Now Select any text and press Alt+x and you will see a popup notification showing the DuckDuckGo search result.

##Search result types:
  1. If the search term has a wiki page, wiki link and its short summary is provided as notification.
  2. If the search is a category like Simpson Characters, all the results are provided as results.
  3. If the search term is ambigious then top most search result is provided.
  4. If its a calculation or ipaddress etc Sirious tries to find meaning out of it.
  5. Results that are restricted by DuckDuckGo wont be shown.

##Installation:

From the downloaded directory type

```python
sudo python setup.py 
```

It will ask for sudo password to place Sirious in /usr/bin.

##Setting up Keyboard Shortcut:

GNOME:

1. Go to System > Preferences(just Settings) > Keyboard >Keyboard Shortcuts

2. Click the Add button or Custom Shortcuts (a plus sign)

3. Choose a Name for your shortcut (can be just about anything)

4. Give command as Sirious 

5. Like other key binded provide a key by clicking on disabled and now it shows the name and its key-bind

You can use any other method to create a key-bind for Sirious command.
http://askubuntu.com/questions/597395/how-to-set-custom-keyboard-shortcuts-from-terminal

