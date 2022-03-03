class Detector():
    ```recebe secao de choque```
    def __init__(self, xsec):
        self.xsec = xsec

    ```calcula secao de choque em funcao da energia```
    def getXsec(self, energy):
        return self.xsec