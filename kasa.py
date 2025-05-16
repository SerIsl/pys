import os
import subprocess

def kasa():
    os.chdir("C:\\Users\\SERKAN\\Desktop\\gitproject\\MyWorkouts")
    subprocess.run(["python", "prep_casa.py"])