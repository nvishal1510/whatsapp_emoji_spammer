# Whatsapp Emoji Spammer
This is tiny python script which makes use of the amazing Selenium library. The script spams whatsapp of your friend (or whomever you give the name of) with emojis. The script uses the list of emojis from [this](https://github.com/amurani/unicode-emoji-list/blob/master/simple-emoji-list.json) file<br>
Try not to spam any official group or person :stuck_out_tongue:.

## Installation
### 1. Install python. 
If you already have a python installation, skip this step. You can download python from [here](https://www.python.org/downloads) and add it to PATH.<br>
### 2. Install selenium and webdriver-manager python modules
You can use the following commands. If you don't know what I mean, just execute the following command in cmd or terminal (depending on your OS).
```
pip install selenium
pip install webdriver-manager
```
### 3. Download the script
Download the source code using git or click the green button "Code" and then "download ZIP". Extract the contents into a new folder.

## Usage
1. Open cmd or terminal in the directory that contents of zip were extracted to and execute the following command.
```
python whatsapp_spammer.py
```
2. The program will open whatsapp webpage in a Chrome window. Log into your whatsapp by scanning the QR code.
3. The command line interface (cmd or terminal) will ask you the contact name. Enter the name of the contact whom you want to spam. 
The name may be incomplete but when you search the name in the whatsapp search window, the required contact should be the first on the list.
4. Then enter the no of emojis you want to spam them. If do not enter any value and press enter it will assume the default value of 15. Although there is no upper limit on the no of emojis, 
I would recommend that do not enter more than 80.
