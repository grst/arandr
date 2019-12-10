import json
from screenlayout.xrandr import XRandR
import warnings
import os
from config import config
from time import sleep

DEFAULT_CONFIG_FILE = os.path.expanduser(config["SCREEN_CONFIG_FILE"])


def intermediate_config_workaround(store):
    """
    There is a bug in xrandr that does not allow certain screen configurations to be applied at once.
    In my case, I cannot apply the configuration with two external display port monitors plus
    my laptop screen in a single step. Instead, I first need to add the first monitor, then the second.

    This workaround does exactly that if it identifies a screen combination listed below.
    """
    # Dict: Offending configuration -> configuration to load first
    FIX_CONFIGS = {
        (
            (
                "DP2-2",
                "00ffffffffffff0022f04c280101010116140104a5342078229ec5a6564b9a25135054210800814081809500a940b300d1c001010101283c80a070b023403020360006442100001a000000fd00323f184c11000a202020202020000000fc004c41323430350a202020202020000000ff00434e34303232304e5a590a20200039",
            ),
            (
                "DP2-3",
                "00ffffffffffff0022f04b28010101011114010380342078ee9ec5a6564b9a25135054210800814081809500a940b300d1c001010101283c80a070b023403020360006442100001a000000fd00323f184c11000a202020202020000000fc004c41323430350a202020202020000000ff00434e34303137303346560a202000c7",
            ),
            (
                "eDP1",
                "00ffffffffffff000daef21400000000161c0104a51f117802ee95a3544c99260f505400000001010101010101010101010101010101363680a0703820402e1e240035ad10000018000000fe004e3134304843472d4751320a20000000fe00434d4e0a202020202020202020000000fe004e3134304843472d4751320a2000bb",
            ),
        ): (
            (
                "DP2-2",
                "00ffffffffffff0022f04c280101010116140104a5342078229ec5a6564b9a25135054210800814081809500a940b300d1c001010101283c80a070b023403020360006442100001a000000fd00323f184c11000a202020202020000000fc004c41323430350a202020202020000000ff00434e34303232304e5a590a20200039",
            ),
            (
                "eDP1",
                "00ffffffffffff000daef21400000000161c0104a51f117802ee95a3544c99260f505400000001010101010101010101010101010101363680a0703820402e1e240035ad10000018000000fe004e3134304843472d4751320a20000000fe00434d4e0a202020202020202020000000fe004e3134304843472d4751320a2000bb",
            ),
        )
    }
    try:
        xr = XRandR()
        xr.load_from_x()
        intermediate_config_hash = FIX_CONFIGS[xr.state.hash]
        n_active_screens = sum(x.active for x in xr.configuration.outputs.values())

        # only execute this, if not all three screens are active yet.
        # This rule might get triggered through udev at some point
        # and would lead to the third screen being removed just
        # to be re-added two seconds later.
        if n_active_screens < len(xr.state.hash):
            intermediate_config = store.store[str(intermediate_config_hash)]
            xr.load_from_commandlineargs(intermediate_config)
            xr.save_to_x()
            sleep(2)
    except KeyError:
        print("Key error")
        pass


class ConfigStore(object):
    def __init__(self):
        self.store = {}

    def load_config_store(self, config_file=DEFAULT_CONFIG_FILE):
        """load the configuration file. Overwrites current config store. """
        with open(config_file, "r") as f:
            self.store = json.load(f)

    def save_config_store(self, config_file=DEFAULT_CONFIG_FILE):
        """Write the curent config store to a json-file. """
        with open(config_file, "w") as f:
            json.dump(self.store, f, indent=4)

    def add_config(self, state, config):
        """
        save a given configuration object.

        Args:
            state (State): xrandr State object
            config (Configuration): xrandr Configuration object
        """
        self.store[str(state.hash)] = "xrandr " + " ".join(config.commandlineargs())

    def get_configuration(self, state):
        """load a configuration as command line args given a monitor state"""
        return self.store.get(str(state.hash), None)


def load(*args):
    """load configuration given current state, if available, and apply to X"""
    store = ConfigStore()
    store.load_config_store()
    xr = XRandR()
    xr.load_from_x()
    intermediate_config_workaround(store)
    tmp_config = store.get_configuration(xr.state)
    print(tmp_config)
    if tmp_config is not None:
        xr.load_from_commandlineargs(tmp_config)
        xr.save_to_x()
    else:
        # apply some sensible default configuration.
        pass


def save(*args):
    """save current screen configuration."""
    config_file_path = os.path.dirname(os.path.abspath(DEFAULT_CONFIG_FILE))
    if not os.path.isdir(config_file_path):
        os.makedirs(config_file_path)

    store = ConfigStore()
    try:
        store.load_config_store()
    except IOError:
        warnings.warn(
            "Could not load configuration file. Will use empty configuration store. "
        )
    xr = XRandR()
    xr.load_from_x()
    store.add_config(xr.state, xr.configuration)
    store.save_config_store()
