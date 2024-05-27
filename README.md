## Instructions for running PoCs programs

[1. Standard Guide](#przewodnik-standardowy) <br />
[2. Docker Guide (Linux Host)](#przewodnik-docker-linux-host) <br />
[3. Docker Guide (Windows Host)](#przewodnik-docker-windows-host) <br />

### Standard Guide

It requires GIT and Python3 installed.
##### Step 1: Download the source code

Clone the repository and navigate to the root directory

```bash
git clone https://github.com/Bembnias/AmbientGuide.git
cd AmbientGuide
```

##### Step 2: Select branch PoC

Switch to the branch `PoC` containing the current Proof of Concepts.

```bash
git checkout PoC
```

##### Step 3: Create a virtual environment

Create a virtual environment to isolate the project.

```bash
python3 -m venv agpoc
source venv/bin/activate  # Na systemach Linux/MacOS
venv\Scripts\activate  # Na systemach Windows
```

##### Step 4: PoC selection

Navigate to the directory with the selected PoC, such as: "DistanceMeasurement_2":

```bash
cd DistanceMeasurement_2
```

##### Step 5: Install dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

##### Step 6: Run the PoC

After installing all the dependencies, you can run the selected Proof of Concept:

```bash
python main.py
```

### Docker Guide (Linux Host)

It requires GIT and Docker installed.

##### Step 1: Download the source code

Clone the repository and navigate to the root directory

```bash
git clone https://github.com/Bembnias/AmbientGuide.git
cd AmbientGuide
```

##### Step 2: Select branch PoC

Switch to the branch `PoC` containing the current Proof of Concepts.

```bash
git checkout PoC
```

##### Step 3: PoC selection

Navigate to the directory with the selected PoC, such as: "DistanceMeasurement_2":

```bash
cd DistanceMeasurement_2
```

##### Step 4: Find the correct path to the camera

Docker will require you to grant permissions to use your laptop's camera, or one plugged in via USB.
Camera devices may have different paths depending on how they are recognized by the system. To check the available camera devices, you can use the ls command in terminal:

```bash
ls /dev/video*
```

If the system finds any camera, it should display something like this: `/dev/video0`, or `/dev/video1` depending on how many cameras are plugged in.

##### Step 5: Build the docker image

With docker installed and being in the PoC directory of your choice, type:

```bash
docker build -t nazwa-poc .
```

##### Step 6: Start the docker image

Once the image is built correctly and you know the path to the cameo, you can run the image (here, for example, the path to the cameo is: `dev/video`).

```bash
docker run --device /dev/video0:/dev/video0 -it nazwa-poc
```

### Docker Guide (Windows Host)

Since Windows doesn't provide a path to the camera as it does on Linux, running one is problematic. A workaround might be to run the application in docker on a virtualized Linux machine via Virtual Box.

##### Step 1: Install VirtualBox

Go to the VirtualBox developers' website and download and then install the program.

[Link to VirtualBox website](https://www.virtualbox.org/wiki/Downloads)

##### Step 2: Install Guest Add-ons in VirtualBox

To ensure USB support, make sure you install Guest Additions on your Linux VM. They are usually installed from the VM appliance menu in VirtualBox.

##### Step 3: Configure USB Forwarding in VirtualBox

1. with the VM closed (the VM must not be running during this setup), open the VM settings in VirtualBox.
2. Go to the "USB" section.
3. select the option that allows you to pass USB 2.0 or USB 3.0, depending on what your VM supports (USB 3.0 requires VirtualBox Extension Pack).
4. click the icon with the plus symbol (+) on the right to add a new USB device to the filter list. This should open a window with a list of available USB devices. Select your camera from the list.
5. confirm your changes and close the VM settings.

##### Step 4: Start the VM with Linux

Start the virtual machine with Linux installed, then follow the guide: [Docker Guide (Linux Host)](#przewodnik-docker-linux-host).
