import json
from screenlayout.xrandr import XRandR
import warnings
import os
from config import config
from time import sleep

DEFAULT_CONFIG_FILE = os.path.expanduser(config['SCREEN_CONFIG_FILE'])


class ConfigStore(object):
    def __init__(self):
        self.store = {}

    def load_config_store(self, config_file=DEFAULT_CONFIG_FILE):
        """load the configuration file. Overwrites current config store. """
        with open(config_file, 'r') as f:
            self.store = json.load(f)

    def save_config_store(self, config_file=DEFAULT_CONFIG_FILE):
        """Write the curent config store to a json-file. """
        with open(config_file, 'w') as f:
            json.dump(self.store, f)

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
    tmp_config = store.get_configuration(xr.state)
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
        warnings.warn("Could not load configuration file. Will use empty configuration store. ")
    xr = XRandR()
    xr.load_from_x()
    store.add_config(xr.state, xr.configuration)
    store.save_config_store()

