from screenlayout.xrandr import XRandR
from screenlayout.store import ConfigStore
import pkg_resources
import tempfile


def test_save_and_retrieve():
    xr1 = XRandR()
    xr2 = XRandR()
    store_save = ConfigStore()
    store_load = ConfigStore()
    with tempfile.NamedTemporaryFile() as config_file:
        xr1.load_from_x(pkg_resources.resource_string(__name__, 'files/xrandr_verbose01.txt'))
        xr2.load_from_x(pkg_resources.resource_string(__name__, 'files/xrandr_verbose02.txt'))
        cl_args1 = xr1.configuration.commandlineargs()
        cl_args2 = xr2.configuration.commandlineargs()

        store_save.add_config(xr1.state, xr1.configuration)
        store_save.add_config(xr2.state, xr2.configuration)

        store_save.save_config_store(config_file.name)
        config_file.flush()

        store_load.load_config_store(config_file.name)

        assert store_load.store == store_save.store, "saving and loading creates an identical object"

        assert cl_args1 == store_load.get_configuration(xr1.state), "object is correctly retrieved"
        assert cl_args2 == store_load.get_configuration(xr2.state), "object is correctly retrieved"
        assert store_load.get_configuration(XRandR.State()) is None, "unknown state returns None"

