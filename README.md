# About
mate-screenlock-dpms is an background utility which catch the screensaver signal and set DPMS to 1s suspend because MATE blank screensaver does not switch off the backlite.

# Install
```console
sudo cp -av mate-screenlock.dpms.py /usr/local/bin/
sudo cp mate-screenlock.dpms.desktop /usr/local/share/applications/
```
Then make symlink to autostart directory or something like that.
