# dmo
Digital Media Organizer (dmo)

The dmo consolidates digital media files that you may have accumalated over the years while transitioning through various applications, devices, computers, and backups.

dmo.py is an old-fashioned python script that will take your preferences from a well-commented dmo.ini file, and exectute accordingly.  It will take two directories as input:  MASTER and TARGET, and compare every single file in TARGET with all files in MASTER -- and take actions accordingly, as specified in the dmo.ini file.

Main goal is to make sure all digital media of interest (according to user preferences in dmo.ini file) in TARGET directory exists in MASTER directory, so the TARGET directory can be deleted safely, without loss of any data.
