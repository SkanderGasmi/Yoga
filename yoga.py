import os
import pandas as pd

# Get the absolute path of the directory containing the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the folder containing the pose folders
data_dir = os.path.join(script_dir, 'YOGA/content/cleaned/DATASET/TRAIN')
