#! /bin/bash
if  echo -e "USB Command" >> /dev/ttyUSB0 ; then
    echo "Success"
else
    echo "Fail"
fi
