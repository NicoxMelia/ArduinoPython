import serial
import serial.tools.list_ports
from state import NormalState, MoonState, SaturnoState, ErrorState
import time
import os


class Loader():
    def __init__(self, container):
        self.ports = list(serial.tools.list_ports.comports())
        self.arduino = None
        for arduinoPort in self.ports:
            print("puerto elegido", arduinoPort.name)
            try:
                print("PROBANDO VERSION LINUX...")
                os.system("sudo chmod a+rw /dev/ttyACM0")
                self.arduino = serial.Serial(port="/dev/" + arduinoPort.name, baudrate=9600, timeout=0.1)
                time.sleep(2)
                self.arduino.write(b'k')
                if(self.arduino.readline() == "OK"):
                    break
            except Exception:
                print("PROBANDO VERSION WINDOWS...")
                self.arduino = serial.Serial(port=arduinoPort.name, baudrate=9600, timeout=0.1)
                time.sleep(2)
                self.arduino.write(b'k')
                if(self.arduino.readline() == "OK"):
                    break

        
        
        self.container = container
        print(self.arduino)
        match self.arduino:
            case None:
                self.changeState(ErrorState.ErrorState())
                self.draw()
            case _:
                self.changeState(NormalState.NormalState())
                self.draw()
        
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
            self.changeState(ErrorState.ErrorState())
            self.draw()

    def leave(self):
        self.arduino.close()
    def changeState(self, newState):
        self.state = newState
    def draw(self):
        self.state.drawPicture(self.container)
    

