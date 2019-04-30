#!/usr/bin/env python3

## import the shutil function
import shutil

## import the os function
import os

## change to the mycode directory
os.chdir("/home/student/mycode/")

## move raynor.obj to the ceph_storage directory
shutil.move("raynor.obj", "ceph_storage/")

## prompt the user for the new name of the kerrigan.obj file
xname = input("What is the new name for the kerrigan.obj? ")

## Rename the kerrigan.obj file
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)
