"""
Category: Structural pattern

Intent: This pattern allows objects with incompatible interfaces to collaborate.

Real-world analogy:
    Trying to plug a micro USB cable into a USB port is impossible as they are
    incompatible. We need an adapter, e.g. micro to USB adapter, so as to be
    able to use the micro USB cable with the usb port.
"""


class USBCable:
    def __init__(self):
        self.is_plugged = False

    def plug_usb(self):
        self.is_plugged = True


class MicroUSBCable:
    def __init__(self):
        self.is_plugged = False

    def plug_micro_usb(self):
        self.is_plugged = True


class USBPort:
    def __init__(self):
        self.port_available = True

    def plug(self, usb):
        if self.port_available:
            usb.plug_usb()
            self.port_available = False


class MicroToUSBAdapter(USBCable):
    def __init__(self, micro_USB_cable):
        self.micro_USB_cable = micro_USB_cable
        self.micro_USB_cable.plug_micro_usb()
