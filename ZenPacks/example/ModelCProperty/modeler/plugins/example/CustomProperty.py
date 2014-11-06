from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin


class CustomProperty(CommandPlugin):

    """Example of modeling a custom property (cProperty).

    This requires the following methods to be monkeypatched onto
    Products.ZenModel.Device.Device in the ZenPack's __init__.py.

    * getWindowsDomain
    * setWindowsDomain

    """

    command = "/bin/echo myvalue"

    def process(self, device, results, log):
        log.info(
            "Modeler %s processing data for device %s",
            self.name(), device.id)

        om = self.objectMap()

        for line in results.splitlines():
            if line:
                # Set Windows domain to first line of output.
                om.setWindowsDomain = line.strip()
                break

        return om
