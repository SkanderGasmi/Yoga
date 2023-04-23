# Yoga Class Analysis using Human pose estimation

This is a lab project for the Deep Learning course of the Data Science program. The goal of the project is to develop a model that can automatically classify images of people doing yoga poses into different categories using human pose estimation.

## Business Understanding

The yoga pose image classification problem involves automatically classifying images of people doing yoga poses into different categories. This is an image recognition problem that belongs to the field of deep learning specifically computer vision.

## Data Requirements & Data Collection

The dataset used for this project can be downloaded directly from the script. The script automatically downloads the dataset from a Google Drive link and extracts the contents to the `data/extracted` folder in the project's directory. The dataset contains images of people doing various yoga poses.

The script also creates a backup of the dataset in the `data/backup` folder in case the extracted dataset is modified or corrupted in the preprocessing phase or deleted accidentally.

## Environment Setup

To run the code, you need to set up a virtual environment and install the required packages. Follow these steps to set up your environment:

1. Clone the repository to your local machine.

    ```
    git clone https://github.com/SkanderGasmi/Yoga
    ```

2. Create a virtual environment by running the following command:

    ```
    python -m venv venv
    ```

3. Activate the virtual environment by running:

    - On Windows: 
        ```
        venv\Scripts\activate
        ```
    - On Linux/MacOS: 
        ```
        source venv/bin/activate
        ```

4. Install the required packages by running:

    ```
    pip install -r requirements.txt
    ```


## Data Understanding & Data Preparation

TODO

## Data Modeling & Model Evaluation

TODO
