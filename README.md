# KobukiFollow

En el proyecto final se espera integrar, mediante ROS noetic, dos bases Kobuki, un sensor RPLidar y un control de joystick. El propósito es mover una de las bases por medio de un control inalámbrico. La segunda base, haciendo uso de las lecturas del Lidar colocado sobre él, deberá intentar seguir la base teleoperada.

## Objetivos

- Actualizar paquetes del robot Kobuki para funcionar bajo ROS noetic.
- Teleoperar una base Kobuki a través de un control remoto de Xbox 360.
- Controlar el movimiento lineal y la rotación de una base Kobuki para mantenerse a una distancia fija de un obstáculo a través de un sensor RPLidar 360.
- Acoplar las dos bases Kobuki en un mismo proyecto, de manera que la segunda base Kobuki intente seguir la primera base teleoperada en un espacio controlado.

***

**Nota**: El espacio debe ser un área controlada, de menos de 15 metros de largo en cualquier dirección, sin obstáculos, y de una superficie plana. De este modo las condiciones serán las necesarias para que el Lidar pueda tomar adecuadamente los datos.

***

## Instrucciones para ejecutar el proyecto

Aquí se muestran los cuatro paquetes utilizados en el proyecto, éstos se pueden copiar a un workspace. 

Para un uso sencillo, se recomiendan los siguientes pasos:

**1.** Instalar ubuntu 20.04

**2.** Instalar ROS noetic

Para instalar ROS noetic colocque en la terminal el siguiente código:

```
wget -c https://raw.githubusercontent.com/qboticslabs/ros_install_noetic/master/ros_install_noetic.sh && chmod +x ./ros_install_noetic.sh && ./ros_install_noetic.sh
```

**3.** Llevar repositorio git como paquetes a un src en un workspace.

**4.** Realizar un catkin_make clean.

**5.** Instalar liborocos

```
sudo apt install liborocos-kdl-dev
```

**6.** Desde el directorio de workspace, hacer un rosdep:

```
rosdep install --from-paths src --ignore-src -r -y
```

**7.** Ejecutar el catkin_make:

```
catkin_make
```

**8.** Ahora, el proyecto puede ser ejecutado de forma diferente dependiendo de si se quiere una base seguidora, o teleoperada. En cualquiera de los dos casos, debe iniciarse el nodo de kobuki.

```
roslaunch kobuki_node minimal.launch
```

**9.** Si se quiere el modo teleoperado, deben colocarse los siguientes comandos:


```
ls /dev/input/
ls -l /dev/input/js0
sudo chmod a+rw /dev/input/js0
roslaunch kobuki_teleop_joy turtle_joy.launch
```

Y debe verificarse que el control esté conectado a js0.

**10.** Si se quiere el modo seguidor, los comandos son:

```
ls -l /dev |grep ttyUSB
sudo chmod 666 /dev/ttyUSB0
roslaunch rplidar_ros view_rplidar.launch
```
Y nuevamente asegurando que el Lidar fue conectado al puerto USB0.

***

## Resultados

### Configuración

La configuración del Kobuki teleoperado a tráves de un control inalámbrico se muestra a continuación

<p align="center">
<image
  src="/ImagenesFRM/Control.jpg"
  alt="Control inalambrico"
  caption="Control inalambrico">
<image
  src="/ImagenesFRM/Configuracion1.jpg"
  alt="Configuracion Kobuki teleoperado"
  caption="Configuracion Kobuki teleoperado">
</p>

Por otro lado, la configuración del Kobuki con sensor RPLidar es la siguiente

<p align="center">
<image
  src="/ImagenesFRM/Configuracion2.jpg"
  alt="Configuración Kobuki con sensor RPLidar"
  caption="Configuración Kobuki con sensor RPLidar">
</p>

Finalmente, la configuración completa es

<p align="center">
<image
  src="/ImagenesFRM/Configuracion_final.jpg"
  alt="Configuración final"
  caption="Configuración final">
</p>


### Videos

Los siguientes videos muestran el funcionamiento de los dos módulos de manera independiente (Hacer click en las imágenes para la redirección a Youtube)

[![Comprehensive Markdown Crash Course](https://img.youtube.com/vi/Ak0MeOStrAI/mqdefault.jpg)](https://youtube.com/shorts/Ak0MeOStrAI "Video Kobuki teleoperado")
[![Comprehensive Markdown Crash Course](https://img.youtube.com/vi/rHeH8-x1-Hg/mqdefault.jpg)](https://youtu.be/rHeH8-x1-Hg "Video Kobuki con sensor RPLidar")

El siguiente video muestra la integración de los módulos

[![Comprehensive Markdown Crash Course](https://img.youtube.com/vi/0k3onq1sAHE/mqdefault.jpg)](https://youtu.be/0k3onq1sAHE "Video proyecto completo")


### Integración con la Raspberry PI

Una vez el proyecto está totalmente en funcionamiento, deberíamos tener cuatro terminales activas. Dos con los nodos del Kobuki, las terminales de teleoperación y del RPLidar. 

<p align="center">
<image
  src="/ImagenesFRM/Terminales.jpg"
  alt="Terminales"
  caption="Terminales">
</p>

Para la implementación en este caso, el segundo Kobuki ejecutaba los comandos desde una Raspberry PI 4b. Para ello fue necesario hacer uso del protocolo SSH, que permitía ejecutar dos terminales de la Raspberry, pero desde la pantalla del computador. 

Para esto, tanto el computador como la Raspberry se conectaron a una misma red wifi, cuyas credenciales fueron guardadas al editar el archivo de conexión a redes de la Raspberry:

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

Y desde el computador buscamos la IP correspondiente a la Raspberry (por ejemplo a través de comandos nmap) y ejecutamos el siguiente comando (para este caso la Raspberry tenía como nombre "unal"):

```
ssh unal@<IP>
```

Una vez ingresada la contraseña de la Raspberry, la terminal utilizada en el computador debería funcionar como consola de la Raspberry.

### RVIZ

El nodo de RPLidar ejecutaba también una vista desde RVIZ de lo observado por el sensor. Al correr el archivo launch correspondiente, se logra ver en tiempo real los puntos detectados en la pantalla del computador.

<p align="center">
<image
  src="/ImagenesFRM/RVIZ.jpg"
  alt="RVIZ"
  caption="RVIZ">
</p>
