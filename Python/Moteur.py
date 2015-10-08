
class MoteurExistError(Exception):
    #Un moteur est déjà initialisé sur ce port
    pass

class MoteurPortError(Exception):
    #Le port demandé n'existe pas
    pass

class MoteurVitesseError(Exception):
    #La vitesse n'est pas comprises entre -100 et 100
    pass
 
class Moteur:
 
    _MOTEURS = {} #Liste des ports utilisé
    _PORTS = "ABC" #Liste des ports disponibles
    
    def __new__(cls, port, vitesse = 0):
        if port in cls._MOTEURS:
            raise MoteurExistError
        if port not in Moteur._PORTS:
            raise MoteurPortError
        if vitesse < -100 or vitesse > 100:
            raise MoteurVitesseError
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
            raise MoteurExistError
        if port not in Moteur._PORTS:
            raise MoteurPortError
        del Moteur._MOTEURS[self._port]
        self._port = port
        self._MOTEURS[port] = self

    def setVitesse(self, vitesse):
        if vitesse < -100 or vitesse > 100:
            raise MoteurVitesseError
        self._vitesse = vitesse
            
    def __repr__(self):
        #Quand on entre notre objet dans l'interpréteur
        return "Moteur sur le port {}\n\tVitesse : {}" . format(self._port, self._vitesse)
    
    def __del__(self):
        del Moteur._MOTEURS[self.port]
