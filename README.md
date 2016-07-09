PyCon India 2016 Application 
=======
> Mobile App for PyConIndia

## Kivy Installation:
- https://kivy.org/docs/installation/installation.html

### To test install kivy and run the following::

    $ python main.py -m screen:droid2,portrait -m inspector

### Help on screens
- https://kivy.org/docs/api-kivy.modules.screen.html

## to make apk **prefer linux**

1. Install buildozer: pip install buildozer
2. Edit the buildozer.spec to specify if you have android ndk and sdk,
   if not they will be automatically be downloaded by the next step.
3. Connect your mobile, enable usb debugging, Then goto PyDelhiMobile
   folder and type `make apk`


***   Enjoy   ***
