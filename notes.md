## concept
* from /sys/class/drm/card, get edid and status for each device. The edids of active devices
are used as a hash to identify a configuration
* If the udev rule is triggered, but the configuration (hash) has not changed; do nothing. 
* how to detect if xrandr configuration has changed? -> fork arandr instead
    -> implement 'save' subcommand to save a current configuration from command line. 
