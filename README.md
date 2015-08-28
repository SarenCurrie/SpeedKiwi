# SpeedKiwi
The best SE 306 2015 - Project 1

![Speedkiwi logo](https://slack-files.com/files-tmb/T07SHFSC9-F07UAGSS0-65ae73cfb5/hipsterlogogenerator_1437460156998_360.png)

## Installation
```
git clone https://github.com/SarenCurrie/SpeedKiwi.git
cd SpeedKiwi/catkin_ws
sudo apt-get install python-pip
./install.sh
catkin_make
```

## Running
```
# Make sure you're in the catkin_ws
java -jar SpeedKiwi.jar
# Then select Default/Configured/Test World from the GUI
```

## Controlling a person
With the project already running execute this command in a seperate terminal tab
```
python src/speedkiwi_core/src/person_controller.py 
```

## Debugging dashboard
With the project running open http://127.0.0.1:1337 in your browser


## Trouble Shooting
```
Is SpeedKiwi.jar not running?

Make sure that:
1. "SpeedKiwi.jar" is executable
2. "./run.sh" is executable
3. "src/speedkiwi_core/world/Generated_World/WorldConfiguration.py" is executable
```
