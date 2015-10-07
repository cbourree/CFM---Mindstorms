

class Moteur ():
    _ports_used = []
    
    def __init__(self, port):
        self._port = port
        Moteur._ports_used.append(port)

    def getPort(self):
        return self._port

    def getPortsUsed(self):
        return Moteur._ports_used

    def setPort(self, port):
        if port in Moteur._ports_used:
            return -1
        else:
            Moteur._ports_used.remove(self.getPort())
            self._port = port
            Moteur._ports_used.append(port)
        
    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Moteur sur le port {}" . format(self._port)

    def __del__(self):
        print ("Destruction du moteur sur le port {}" . format(self._port))
        Moteur._ports_used.remove(self.getPort())
