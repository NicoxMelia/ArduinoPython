import serial
import serial.tools.list_ports
from state import NormalState, MoonState, SaturnoState


class Loader():
    def __init__(self, container):
        self.ports = list(serial.tools.list_ports.comports())
        for arduinoPort in self.ports:
            print("puerto elegido", arduinoPort.name)
            try:
                print("PROBANDO VERSION LINUX...")
                self.arduino = serial.Serial(port="/dev/" + self.ports[0].name, baudrate=9600, timeout=1)
                self.arduino.write(b'k')
                
            except Exception:
                print("PROBANDO VERSION WINDOWS...")
                self.arduino = serial.Serial(port=arduinoPort.name, baudrate=9600, timeout=1)
                self.arduino.write(b'k')

        
        
        self.container = container
        self.state = NormalState.NormalState()
        self.state.drawPicture(self.container)
        
    def read(self):
        try:
            while(True):
                dato = str(self.arduino.readline().strip())
                print(dato)
                match dato:
                    case "b'moon'":
                        self.changeState(MoonState.MoonState())
                        self.draw()
                        
                    case "b'saturno'":
                        self.changeState(SaturnoState.SaturnoState())
                        self.draw()
                
                        
        except Exception:
            print("Arduino desconectado")

    def leave(self):
        self.arduino.close()
    def changeState(self, newState):
        self.state = newState
    def draw(self):
        self.state.drawPicture(self.container)
    

