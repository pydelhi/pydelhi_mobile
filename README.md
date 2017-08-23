PyCon India 2017 Application 
=======
> Mobile App for PyConIndia

## Requirements:
### Kivy Installation:
-   https://kivy.org/docs/installation/installation.html

WIP
====

### To test install kivy and run the following::

    $ python eventsapp/main.py -m screen:droid2,portrait -m inspector

### Help on screens
- https://kivy.org/docs/api-kivy.modules.screen.html

## To change images in app
   - Paste/change the image in PyCon-Mobile-App/tools/theming
   - Change your directory to PyCon-Mobile-App
   - Run command ``make theming`` 

This command will aggregate all the png images in your file to one atlas
from which the images are loaded.

## to make apk **prefer linux**

1. Install buildozer: pip install buildozer
2. Edit the buildozer.spec to specify if you have android ndk and sdk,
   if not they will be automatically be downloaded by the next step.
3. Connect your mobile, enable usb debugging, Then goto PyConIndia
   folder and type `make apk`

Link to a existing vm that can be re-used will be added for convenience.

## to make ipa for ios **

1. Install XCode with latest updates & latest command line tools
2. pip install buildozer
3. goto the app folder and do `buildozer init`
4. edit the buildoze.spec and add details for ios
5. run `buildozer ios debug`

** Release Notes **

TBD

***   Enjoy   ***
