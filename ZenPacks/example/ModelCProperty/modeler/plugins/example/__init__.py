from Products.ZenUtils.Utils import monkeypatch


@monkeypatch('Products.ZenModel.Device.Device')
def getWindowsDomain(self):
    """Return current Windows domain for device."""
    return self.cWindowsDomain


@monkeypatch('Products.ZenModel.Device.Device')
def setWindowsDomain(self, value):
    """Set Windows domain on device to value."""
    self.setZenProperty('cWindowsDomain', value)
