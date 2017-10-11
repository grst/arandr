config = {
    "SCREEN_CONFIG_FILE": '/home/sturm/.screenlayout/config.json', # path to your config file (will be created)

    # the udev rule is run as root, so you need to specify how to connect to the X-Server
    "DISPLAY": ":0",
    "XAUTHORITY": '/home/sturm/.Xauthority'
}
