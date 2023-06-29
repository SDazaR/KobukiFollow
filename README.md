# KobukiFollow
Proyecto de seguimiento de dos robots Kobuki a través de un control remoto y un sensor RPLidar. ROS noetic implementado.

Aquí se muestran los cuatro paquetes utilizados en el proyecto. Se pueden copiar a un workspace. 

Para un uso sencillo, se recomiendan los siguientes pasos:

1. Instalar ubuntu 20.04
2. Instalar ROS noetic
3. Llevar repositorio git como paquetes a un src en un workspace
4. Realizar un catkin_make clean.
5. Instalar liborocos

```
sudo apt install liborocos-kdl-dev

```

6. Desde el directorio de workspace, hacer un rosdep:

```
rosdep install --from-paths src --ignore-src -r -y

```

7. Ejecutar el catkin_make:

```
catkin_make

```

8. Ahora, el proyecto puede ser ejecutado de forma diferente dependiendo de si se quiere una base seguidora, o teleoperada. En cualquiera de los dos casos, debe iniciarse el nodo de kobuki.

```
roslaunch kobuki_node minimal.launch

```

9. Si se quiere el modo teleoperado, deben colocarse los siguientes comandos:


```

ls /dev/input/
ls -l /dev/input/js0
sudo chmod a+rw /dev/input/js0
roslaunch kobuki_teleop_joy turtle_joy.launch

```

Y debe verificarse que el control esté conectado a js0.

10. Si se quiere el modo seguidor, los comandos son:

```
ls -l /dev |grep ttyUSB
sudo chmod 666 /dev/ttyUSB0
roslaunch rplidar_ros view_rplidar.launch

```
Y nuevamente asegurando que el Lidar fue conectado al puerto USB0.


Se deberían entonces tener cuatro terminales corriendo los archivos launch. (El launch de kobuki_node corre el master)

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0k3onq1sAHE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

