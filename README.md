PyCon India 2016 Application 
=======
> Mobile App for PyConIndia

## Requirements:
### Kivy Installation:
-  `https://kivy.org/docs/installation/installation.html`

### Junction Client Installation:
- `pip install git+git://github.com/pythonindia/junction-client.git --user`

### To test install kivy and run the following::

    $ python pyconindia/main.py -m screen:droid2,portrait -m inspector

### Help on screens
- https://kivy.org/docs/api-kivy.modules.screen.html

## To change image
   - Paste/change the image in PyCon-Mobile-App/tools/theming
   - Change your directory to PyCon-Mobile-App
   - Run command ``make theming`` 
     this command will aggregate all the png images in your file to one.

## to make apk **prefer linux**

1. Install buildozer: pip install buildozer
2. Edit the buildozer.spec to specify if you have android ndk and sdk,
   if not they will be automatically be downloaded by the next step.
3. Connect your mobile, enable usb debugging, Then goto PyDelhiMobile
   folder and type `make apk`


***   Enjoy   ***
