import serial
import serial.tools.list_ports
from state import NormalState, MoonState


class Loader():
    def __init__(self, container):
        self.ports = list(serial.tools.list_ports.comports())
        self.puerto = self.ports[0].name
        print("puerto elegido", self.puerto)
        self.arduino = serial.Serial(port="/dev/" + self.puerto, baudrate=9600, timeout=1)
        self.container = container
        self.state = NormalState.NormalState()
        self.state.drawPicture(self.container)
        
    def read(self):
        try:
            while(True):
                dato = self.arduino.readline()
                print(dato)
                match dato:
                    case "moon":
                        self.changeState(MoonState.Moonstate())
                        self.draw()
                        
        except Exception:
            print("Arduino desconectado")

    def leave(self):
        self.arduino.close()
    def changeState(self, newState):
        self.state = newState
    def draw(self):
        self.state.drawPicture(self.container);
    

