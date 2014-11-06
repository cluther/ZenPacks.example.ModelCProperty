# ZenPacks.example.ModelCProperty

This is ZenPack that only serves as an example of how to have Zenoss automatically set the value of a customer property (cProperty) using a modeler plugin.

## Files

The only relevant files are:

 * ZenPacks/example/ModelCProperty/__init__.py
 * ZenPacks/example/ModelCProperty/modeler/plugins/example/CustomProperty.py

### __init__.py

Two methods are defined in this file: *getWindowsDomain* and *setWindowsDomain*. They are both monkeypatched onto the standard Zenoss device class, *Products.ZenModel.Device.Device*. This means these methods will now exist on all devices in the system.

### CustomProperty.py

This is the actual modeler plugin that should be assigned to the device(s) you want it to be run for. It runs a command on the server using SSH and uses the result of that command to set the *cWindowsDomain* custom property.

## Notes

You must restart Zenoss after installing this ZenPack. As with installing any ZenPack.
