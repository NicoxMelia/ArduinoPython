import serial
import serial.tools.list_ports
from state import NormalState, Tarjeta1State, Tarjeta2State, ErrorState
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
                if(arduinoPort.manufacturer == "Arduino (www.arduino.cc)" or arduinoPort.manufacturer == "Arduino LLC (www.arduino.cc)"):
                    self.arduino = serial.Serial(port="/dev/" + arduinoPort.name, baudrate=9600, timeout=0.1)
                    time.sleep(2)
                    self.arduino.write(b'k')
            except Exception:
                print("PROBANDO VERSION WINDOWS...")
                if(arduinoPort.manufacturer == "Arduino (www.arduino.cc)" or arduinoPort.manufacturer == "Arduino LLC (www.arduino.cc)"):
                    self.arduino = serial.Serial(port= arduinoPort.name, baudrate=9600, timeout=0.1)
                    time.sleep(2)
                    self.arduino.write(b'k')
        
        
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
                    case "b'411322588'":
                        self.changeState(Tarjeta1State.Tarjeta1State())
                        self.draw()
                        
                    case "b'24524331161'":
                        self.changeState(Tarjeta2State.Tarjeta2State())
                        self.draw()
                    case "b'5123617912'":
                        self.changeState()#cambiar
                        self.draw()
                    case "b'41150255238'":
                        self.changeState()#cambiar
                        self.draw()
                    case "b'13524232180'":
                        self.changeState()#cambiar
                        self.draw()
                
                        
        except TypeError:
            print("Arduino desconectado")
        except (serial.SerialException or AttributeError):
            self.changeState(ErrorState.ErrorState())
            self.draw()
        except AttributeError:
            self.changeState(ErrorState.ErrorState())
            self.draw()

    def leave(self):
        try:
            self.arduino.write(b'd')
            time.sleep(2)
            self.arduino.close()
        except AttributeError:
            print("ERROR, THERE ARENT ANY PORTS BEING USED")
    def changeState(self, newState):
        self.state = newState
    def draw(self):
        self.state.drawPicture(self.container)
    

