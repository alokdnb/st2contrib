from pynos import device
from st2actions.runners.pythonrunner import Action

class interface_lacp_timeout(Action):
    def run(self, **kwargs):
        conn = (str(kwargs.pop('ip')), str(kwargs.pop('port')))
        auth = (str(kwargs.pop('username')), str(kwargs.pop('password')))
        with device.Device(conn=conn, auth=auth) as dev:
            kwargs['timeoute'] = kwargs.pop('lacp_timeout')
            dev.interface.lacp_timeout(**kwargs)
        return 0
