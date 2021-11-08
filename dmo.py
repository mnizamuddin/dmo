# ------------------------------------------------------------------------------------------
# -- import modules
# ------------------------------------------------------------------------------------------
import configparser
import logging
import os
import platform
import stat
import time
from logging.handlers import TimedRotatingFileHandler


# ------------------------------------------------------------------------------------------
# -- program information & paths
# ------------------------------------------------------------------------------------------
start_time = time.time()
app_name = "dmo"
app_desc = "Digital Media Organizer - compares two directories M(aster) and T(arget) and makes sure M has everything that T has, so T can be deleted safely."
app_conf = "dmo.ini"
app_log = app_name + ".log"

# ------------------------------------------------------------------------------------------
# -- setup logging
# ------------------------------------------------------------------------------------------
# -- define a rotating file handler for logging
formatter = logging.Formatter('%(asctime)s:%(lineno)-4s:%(name)-12s %(levelname)-8s %(message)s')
file_handler = TimedRotatingFileHandler(app_log, when='midnight', backupCount=5)
file_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

# -- set logging level:  CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logger.setLevel(logging.DEBUG)
# -- define a console handler which writes INFO messages or higher to the sys.stderr
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # -- change this for screen output
#console_handler.setLevel(logging.INFO)  # -- change this for screen output

# -- set a format which is simpler for console use
formatter = logging.Formatter('%(levelname)-8s %(message)s')
# -- tell the handler to use this format
console_handler.setFormatter(formatter)
# -- add the handler to the root logger
logger.addHandler(console_handler)


# ------------------------------------------------------------------------------------------
# -- SUBROUTINES / HELPER FUNCTIONS
# ------------------------------------------------------------------------------------------
def scan_path(path):
    sub_start_time = time.time()
    sub_ret_val = False

    logger.info("Scanning path: " + path)
    if os.path.isdir(path):
        logger.info("\tpath is a valid directory")
        totalFiles = 0
        totalDir = 0
        ext = {}

        for base, dirs, files in os.walk(path):
            #print('Searching in : ', base)
            for directories in dirs:
                totalDir += 1
            for Files in files:
                totalFiles += 1
                pathname, exten = os.path.splitext(Files)
                if exten in ext:
                    ext[exten] += 1
                else:
                    ext[exten] = 1

        print('Total number of files', totalFiles)
        print('Total Number of directories', totalDir)
        print('Total:', (totalDir + totalFiles))
        for k,v in sorted(ext.items()):
            print(k,v)  # or print(list(extensions)) if you want a list afterwards


        sub_ret_val = True
    else:
        logger.critical("\tpath is NOT a valid directory")
        sub_ret_val = False

    sub_end_time =  time.time()
    sub_ttl_time = sub_end_time - sub_start_time
    logger.info('\tsub execution time = %d seconds', sub_ttl_time)
    return sub_ret_val



# ******************************************************************************************
# ** MAIN PROGRAM
# ******************************************************************************************
def main():
    logger.info("==== STARTING:  Digital Media Organizer ======================================================")
    logger.debug('app_name:  ' + app_name)
    logger.debug('app_desc:  ' + app_desc)
    logger.debug('app_conf:  ' + app_conf)
    logger.debug('app_log:  ' + app_log)


    # -- load configuration file
    if os.path.isfile(app_conf):
        logger.debug("loading configuration file: " + app_conf)
        config = configparser.ConfigParser()
        config.read(app_conf)
        scan_path(config['master']['path'])
        scan_path(config['target']['path'])


    else:
        # -- configuration file not found
        logger.critical("failed to load " + app_conf + " -- configuration file not found!")


# ===============================================================================================================
# ===============================================================================================================
if (__name__ == "__main__"):
    main()
    # -- end of program
    end_time = time.time()
    ttl_time = end_time - start_time
    logger.info('main execution time = %d seconds', ttl_time)
    exit(0)
