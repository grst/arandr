#!/usr/bin/bash

#####################################################
# udev wrapper script was created with help from
# https://tyler.vc/auto-monitor-detection-on-linux
#####################################################


# udev will wait for our script to finish before the monitor is available
# for use, so we will use the `at` command to run our command again as
# another user:
echo "$(dirname $0)/arandr-auto load" | at now
