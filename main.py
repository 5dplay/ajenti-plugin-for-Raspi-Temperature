from jadi import component

from aj.plugins.dashboard.api import Widget

@component(Widget)
class RaspiTempWidget(Widget):
    id = 'raspi-temp'
    name = _('Raspi temperature')
    template = '/raspi-temp:resources/partial/raspi-temp.html'

    def __init__(self, context):
        Widget.__init__(self, context)

    def get_value(self, config):
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            temp = f.read().strip()
        val = float(temp)/1000.0

        return "%.1f 'C" % val