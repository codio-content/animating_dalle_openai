import os
import subprocess
import sys

sys.path.insert(1, '/home/codio/workspace')


# Check if the well_seasons.gif exists
assert os.path.exists("well_seasons.gif"), "well_seasons.gif was not created."

print("Test passed! The well_seasons.gif file was successfully created.")