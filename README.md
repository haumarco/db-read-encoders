# DB-Cmd-Vels
This node reads encoder signals from the [Duckietown](https://www.duckietown.org/) Duckiebot using the [pigpio](https://github.com/joan2937/pigpio) library (v74).

Documentation for the Duckietown project can be found [here](https://docs.duckietown.org/daffy/).

---
## Note!
The encoder_ticks node in this package has been designed to work in conjunction with the [db-cmd-vels](https://github.com/mech-4640/db-read-encoders) node, but does not need the db-cmd-vels node running in order to function. 
**_If_** using the encoder_control node from the db-cmd-vels ROS package, 
this encoder_ticks node **must** be running first.


To install db-read-encoders, please run in terminal:

	$ cd ~/catkin_ws/src
	$ git clone https://github.com/mech-4640/db-read-encoders

To run the db-read-encoders node, please run:

	$ cd ~/catkin_ws/src/db-read-encoders
	$ dts devel build -f --arch arm32v7 -H islduckieXX.local
	$ docker -H islduckieXX.local run -it --rm --privileged --net=host duckietown/db-read-encoders:master-arm32v7

Note: Please replace the XX in `islduckieXX.local` in the command above with your Duckiebot number, or you may substitute this with the your Duckiebot's [hostname](https://docs.duckietown.org/DT19/opmanual_duckiebot/out/setup_duckiebot.html).

---

## Also Note!
This ROS node uses the [pigpio-v74 library](https://github.com/joan2937/pigpio) that can be pulled from [here](https://github.com/joan2937/pigpio).
Newer versions of the library may be available after this software is published, but it is at the discretion of the maintainer whether to use newer versions of the pigpio library.

As the docker container (built and run by the commands indicated above) starts, it will install the pigpio library locally on the Duckiebot. This may take approximate 1-2 minutes to install, but the container need only be run once after starting the Duckiebot.

For the db-read-encoders package to use the pigpio library's daemon, the docker container **must** be run with the `--privileged` argument to give the daemon access to raspberry pi's hardware, which exists outside the docker container.


---
	
## How to use it

### 1. Fork this repository (Encouraged)

Use the fork button in the top-right corner of the github page to fork this template repository.


### 2. Create a new repository (Encouraged)

Create a new repository on github.com while
specifying the newly forked template repository as
a template for your new repository.


### 3. Define dependencies (Optional)

List the dependencies in the files `dependencies-apt.txt` and
`dependencies-py.txt` (apt packages and pip packages respectively).


### 4. Place your code (Optional)

**Note:** This ROS package is designed to run independently as does not need to be modified in order to work.

Place your ROS packages in the directory `/packages` of
your new repository.

NOTE: Do not use absolute paths in your code,
the code you place under `/packages` will be copied to
a different location later.

For this part, the package `/packages/read_encoders` has already been created to house your code (should you chose to modify this package). For courses at [Dalhousie](https://www.dal.ca/faculty/engineering/mechanical.html) using this repository, you may need to modify the files `launch.sh`, `/packages/read_encoders/src/encoder_ticks_node.py` or the `encoder.launch`.


### 5. Setup the launchfile

Change the file `launch.sh` in your repository to launch your code.

---
## This code borrowed from the Duckietown ROS template
See [the template](https://github.com/duckietown/template-ros)
