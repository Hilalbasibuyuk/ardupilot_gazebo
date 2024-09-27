Teknofest savaşan iha yarışmasındaki görev isterlerini simüle etmek için Gazebo simülasyonu ve ArduPilot SITL simülasyonu kullanımı //
Using Gazebo simulation and ArduPilot SITL simulation to simulate mission demands in the Teknofest Fixed Wing UAV competition


Sanal makine olarak VMware Workstation 17 Player indirebilirsiniz. 

Ubuntu 20.04 versiyonunu kullanmanız lazım. Aksi takdirde bu repo sizin için uygun olmayabilir.

Sanal makinenizi ve ubuntu işletim sisteminizi hazır hale getirdikten sonra aşağıdakileri sırasıyla terminale yazarak indirmelerinizi yapabilirsiniz.

# Git Kurulumu

sudo apt-get update

sudo apt-get upgrade


sudo apt-get install git

sudo apt-get install gitk git-gui


# Ardupilot Dosyalarını Git Üzerinden Bilgisayarımıza İndiriyoruz

git clone https://github.com/ArduPilot/ardupilot.git


# Gerekli Bileşenlerin Yüklenmesi *

cd ardupilot



git submodule update --init --recursive



Tools/environment_install/install-prereqs-ubuntu.sh -y



cd



sudo apt install python-wxtools



sudo apt install python-lxml



sudo apt install python-pexpect



. ~/.profile




git config --global url."https://".insteadOf git://




cd ardupilot/ArduCopter



sim_vehicle.py -w





# MAVProxy Kurulumu


sudo pip install future pymavlink MAVProxy


# Ardupilot SITL Çalıştırılması

cd ~/ardupilot/ArduCopter


../Tools/autotest/sim_vehicle.py -w --console --map


# Gazebo 11 Kurulumu


sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'




wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -



sudo apt-get update


sudo apt-get install gazebo11


sudo apt-get install libgazebo11-dev




# Gazebo Ardupilot Eklentisi Kurulumu

git clone https://github.com/khancyr/ardupilot_gazebo



cd ardupilot_gazebo



mkdir build


cd build


cmake ..


make -j4


sudo make install




echo 'source /usr/share/gazebo/setup.sh' >> ~/.bashrc


echo 'export GAZEBO_MODEL_PATH=~/ardupilot_gazebo/models' >> ~/.bashrc



. ~/.bashrc




# Python Paketlerinin Kurulumu


sudo apt-get install python-pip python-dev python3-pip python3-dev



sudo apt-get install python3-dev python3-opencv python3-pip python3-matplotlib python3-pygame python3-lxml python3-yaml



# Dronekit Kurulumu

pip install dronekit


pip3 install dronekit


pip install dronekit-sitl


pip3 install dronekit-sitl



# !!! Gazebo sanal makinede hata verirse aşağıdaki kodu terminalde çalıştırarak hatayı giderebilirsiniz.

export SVGA_VGPU10=0


echo "export SVGA_VGPU10=0" >> ~/.bashrc


# ***ROS Noetic: Gazebo 11.x
# ROS ile uçak ayarlamalarını içerir

