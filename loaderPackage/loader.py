import serial
import serial.tools.list_ports
from state import NormalState, MoonState


class Loader():
    def __init__(self, container):
        self.ports = list(serial.tools.list_ports.comports())
        self.puerto = self.ports[1].name
        print("puerto elegido", self.puerto)
        try:
            print("PROBANDO VERSION LINUX...")
            self.arduino = serial.Serial(port="/dev/" + self.puerto, baudrate=9600, timeout=1)
        except Exception:
            print("PROBANDO VERSION WINDOWS...")
            self.arduino = serial.Serial(port=self.puerto, baudrate=9600, timeout=1)
        
        self.container = container
        self.state = NormalState.NormalState()
        self.state.drawPicture(self.container)
        # self.imagen = tkinter.PhotoImage(file="moon3.png")
        # tkinter.Label(self.container, image=self.imagen).place(x="0", y="0")
        
    def read(self):
        try:
            while(True):
                dato = str(self.arduino.readline().strip())
                print(dato)
                match dato:
                    case "b'moon'":
                        self.changeState(MoonState.MoonState())
                        self.draw()
                        
        except Exception:
            print("Arduino desconectado")

    def leave(self):
        self.arduino.close()
    def changeState(self, newState):
        self.state = newState
    def draw(self):
        self.state.drawPicture(self.container)
    

