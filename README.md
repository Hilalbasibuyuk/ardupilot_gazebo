Teknofest savaşan iha yarışmasındaki görev isterlerini simüle etmek için Gazebo simülasyonu ve ArduPilot SITL simülasyonu kullanımı //
Using Gazebo simulation and ArduPilot SITL simulation to simulate mission demands in the Teknofest Fixed Wing UAV competition


Sanal makine olarak VMware Workstation 17 Player indirebilirsiniz. // You can download VMware Workstation 17 Player as a virtual machine. 

Ubuntu 20.04 versiyonunu kullanmanız lazım. Aksi takdirde bu repo sizin için uygun olmayabilir.  //  You must be running Ubuntu version 20.04, otherwise this repo may not be suitable for you.


Sanal makinenizi ve ubuntu işletim sisteminizi hazır hale getirdikten sonra aşağıdakileri sırasıyla terminale yazarak indirmelerinizi yapabilirsiniz.   // After making your virtual machine and ubuntu operating system ready, you can make your downloads by typing the following into the terminal respectively.

## Git Kurulumu  //  Git Setup

sudo apt-get update

sudo apt-get upgrade


sudo apt-get install git

sudo apt-get install gitk git-gui


## Ardupilot Dosyalarını Git Üzerinden Bilgisayarımıza İndiriyoruz  //  We Download Ardupilot Files to Our Computer via Git

git clone https://github.com/ArduPilot/ardupilot.git


## Gerekli Bileşenlerin Yüklenmesi  //  Installing Required Components 

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





## MAVProxy Kurulumu  //  MAVProxy Setup


sudo pip install future pymavlink MAVProxy


## Ardupilot SITL Çalıştırılması  //  Running Ardupilot SITL

cd ~/ardupilot/ArduCopter


../Tools/autotest/sim_vehicle.py -w --console --map


## Gazebo 11 Kurulumu  //  Gazebo 11 Setup


sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'




wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -



sudo apt-get update


sudo apt-get install gazebo11


sudo apt-get install libgazebo11-dev




## Gazebo Ardupilot Eklentisi Kurulumu  //  Gazebo Ardupilot Plugin Installation

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




## Python Paketlerinin Kurulumu  //  Installing Python Packages


sudo apt-get install python-pip python-dev python3-pip python3-dev



sudo apt-get install python3-dev python3-opencv python3-pip python3-matplotlib python3-pygame python3-lxml python3-yaml



## Dronekit Kurulumu  //  Dronekit Setup

pip install dronekit


pip3 install dronekit


pip install dronekit-sitl


pip3 install dronekit-sitl



### !!! Gazebo sanal makinede hata verirse aşağıdaki kodu terminalde çalıştırarak hatayı giderebilirsiniz.  //  !!! If Gazebo gives an error in the virtual machine, you can fix it by running the following code in the terminal.

export SVGA_VGPU10=0


echo "export SVGA_VGPU10=0" >> ~/.bashrc


## ***ROS Noetic: Gazebo 11.x
### ROS ile uçak ayarlamalarını içerir  //  Includes plane adjustments with ROS

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros-latest.list'


sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654


sudo apt-get update


sudo apt-get install ros-noetic-desktop-full


echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc


source ~/.bashrc


mkdir -p ~/catkin_ws/src


cd ~/catkin_ws/


catkin_make


source devel/setup.bash


sudo apt-get install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential


sudo rosdep init



rosdep update


cd ~/catkin_ws/src


git clone https://github.com/byu-magicc/ardupilot_sim.git


## ArduPlane SITL Ortamının Kurulması ve Açılması  //   Installing and Opening the ArduPlane SITL Environment 

cd ~/catkin_ws


catkin_make


source devel/setup.bash


cd $HOME/ardupilot



git apply $HOME/catkin_ws/src/ardupilot_sim/patches/Zephyr-Params.patch



roslaunch ardupilot_sim plane.launch  


### "roscore" komutunu 1. terminal ekranına yazınız ve çalıştırınız. Ardından "ArduPlane SITL Ortamının Kurulması ve Açılması" kısmını 2. terminal ekranında çalıştırınız. Bunu her açtığınızda yapmalısınız.  //  Type the command “roscore” in the 1st terminal screen and run it. Then run “Installing and Opening the ArduPlane SITL Environment” on the 2nd terminal screen. You should do this every time you turn it on.


### ardupilot_sim reposunda kamera eklentisi eklenmiş halde değildir. Dosyalarda cessna.xacro dosyasını bu repodaki cessna.xacro dosyası ile aynı yaparsanız kamera eklenecektir  //   This ardupilot_sim repo does not have the camera plugin added. If you make the cessna.xacro file in the files the same as the cessna.xacro file in this repo, the camera will be added  

### kamera.py dosyasını uçak dünyası açıkken bir terminalde çalıştırırsanız kamera görüntüsünü alacaksınız.  //  If you run the kamera.py file in a terminal with airplane world on, you will get the camera image.
