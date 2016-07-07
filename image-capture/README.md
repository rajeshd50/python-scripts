## python scripts for capturing image from webcam
Install pygame then run

### For installing a new service and start at boot

1. copy the shell script in /etc/init.d/
2. create a directory named "mydir" or anything in /usr/local/bin/
3. copy the python script in that directory
4. in the shell script change the DIR, DEAMON and DEAMON_NAME
5. run the command in terminal as root
`update-rc.d {your service name} defaults`
6. Further instruction on adding/removing service on startup [Linux services] (https://help.ubuntu.com/community/UbuntuBootupHowto)
7. The script will then start at boot time :)
