# Projekt TS 2021
## Temat: Proces sprawdzania i oznaczania obiektów przez UAV
## Członkowie grupy:
- Łukasz Kozak
## Schemat procesu:
![Schemat](img/Schemat.png)
## Środowisko:
- Implementacja maszyny stanów: python-statemachine
- Wizualizacja maszyny stanów: NetworkX
- Autopilot & SITL: Ardupilot
- Wizualizacja UAV: FlightGear 3D
- Komunikacja z Ardupilot: DroneKit
## Instalacja:
```
cd ~/catkin_ws/src
git clone https://github.com/ArduPilot/ardupilot.git
ardupilot/Tools/environment_install/install-prereqs-ubuntu.sh -y
pip3 install --upgrade pymavlink MAVProxy --user dronekit networkx 
git clone https://github.com/justkozi/ProjektTS2021.git
sudo apt-get install flightgear
```
https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html
### Uruchamianie:
Terminal 1 (Uruchomienie SITL):
```
cd ~/catkin_ws/src/ardupilot/Arducopter
sim_vehicle.py -v ArduCopter --console --map -L KSFO
```
Terminal 2 (Uruchomienie wizualizacji 3D):
```
cd ~/catkin_ws/src/ardupilot/Tools/autotest
./fg_quad_view.sh
```
Terminal 3 (Uruchomienie State Machine):
```
~/catkin_ws/src/ProjektTS2021/src
python3 stateMachine.py
```

[comment]: <> (### ToDo)

[comment]: <> (- [x] Python state machine - konsolowo - przeskakiwanie po stanach )

[comment]: <> (- [x] Znaleźć projekt z symulacją UAV - https://ardupilot.org/dev/docs/ros-gazebo.html)

[comment]: <> (- [ ] Stałe ze StateMAchine.py do YAML-a )

[comment]: <> (- [x] plt.figure - przekazywać AX &#40;na nowo ładowane grafu&#41;)
