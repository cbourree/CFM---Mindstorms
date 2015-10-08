
class MoteurExistError(Exception):
    pass

class MoteurPortError(Exception):
    pass

class MoteurVitesseError(Exception):
    pass
 
class Moteur:
 
    _MOTEURS = {}
 
    def __new__(cls, port, vitesse = 0):
        if port in cls._MOTEURS:
            raise MoteurExistError
        if port not in "ABC":
            raise MoteurPortError
        self = object.__new__(cls)
        self._port = port
        self._vitesse = vitesse
        cls._MOTEURS[port] = self
        return self

    def getPort(self):
        return self._port
    
    def getVitesse(self):
        return self._vitesse

    def setPort(self, port):
        if port in self._MOTEURS:
            return -1
        else:
            del Moteur._MOTEURS[self._port]
            self._port = port
            self._MOTEURS[port] = self

    def setVitesse(self, vitesse):
        self._vitesse = vitesse
            
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Moteur sur le port {}\n\tVitesse : {}" . format(self._port, self._vitesse)
    
    def __del__(self):
        del Moteur._MOTEURS[self.port]
