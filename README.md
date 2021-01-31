# CovidRecognizer &middot;

![version](https://img.shields.io/badge/tensorflow-v2.4.0-gold.svg)
![version](https://img.shields.io/badge/keras-v2.2.5-blue.svg)
![version](https://img.shields.io/badge/nibabel-v3.2.1-green.svg)

The colab notebooks of this project can be accessed from the models folder of this repository.

## AIM: 

Classifying whether the the patient is covid positive or negative based on their lung's CT Scan analysis. Performing lung and infection segmentation if the patient is covid positive.

## 

## DATASET:

[This](https://www.kaggle.com/andrewmvd/covid19-ct-scans) dataset contains 20 images of covid positive patients along with thier lung mask and infection mask in the Nifti format.
 
<img src="https://github.com/lostmartian/CovidRecognizer/blob/main/readme_files/final_images/dataset_img.png" align="middle" height="250" >

## DATA PREPROCESSING:

The data pre-processing step includes the contrast enhancement as well as cropping the CT-scan images such that they focus only on the lung part. To achieve this we used CLAHE enhancer for contrast improvements. To crop the images we first binarised the image and performed bio-medical imaging techniques such as erosion and dilation. Using K-means found clusters and drew bound box around it and cropped the CT-scan.
<p align="center">
<img src="https://github.com/lostmartian/CovidRecognizer/blob/main/readme_files/dataset_contrast.png" align="middle">
<br>
CLAHE Contrast enhancements
<br><br>
<img src="https://github.com/lostmartian/CovidRecognizer/blob/main/readme_files/dataset_kmeans.png" align="middle">
<br>
Dataset cropping process
<br><br>
<img src="https://github.com/lostmartian/CovidRecognizer/blob/main/readme_files/final_dataset.png" align="middle" height="250" width="500">
<br>
Final preprocessed dataset
</p>

## CLASSIFICATION:

The pre-processed 2d ct-scans are labeled as Covid-19 positive or negative based on their infection masks. The labeled dataset is then used
to train a CNN model which gives a value between 0 and 1. Threshold is decided using ROC curve and the prediction is converted to binary values.
A confusion matrix is created which is used to calculate precision, recall and F1 score.

<p align="center">
<img src="https://github.com/lostmartian/CovidRecognizer/blob/main/readme_files/final_images/classigraph.PNG" align="middle">
<br>
<img src="https://github.com/lostmartian/CovidRecognizer/blob/main/readme_files/final_images/classiss.PNG" align="middle">
<br>
</p>

## LUNG SEGMENTATION:

The pre-processed 2d ct-scans and the lung masks are used to train a CNN model which marks the lung area in the ct-scans. A U-net is implemented for this task.
Dice coefficient is used to judge the efficiency of the model. Exponential decay is used to change the learning rate during training.

<p align="center">
<img src="https://github.com/lostmartian/CovidRecognizer/blob/main/readme_files/final_images/lungseggraph.PNG" align="middle">
<br>
<img src="https://github.com/lostmartian/CovidRecognizer/blob/main/readme_files/final_images/lungsegss.PNG" align="middle">
<br>
</p>

## INFECTION SEGMENTATION:

We implemented a U-net with dice coefficient along with Cosine Annealing Learning Rate Schedule for state of the art segmentation achieving a dice-coefficient of 0.8217 and validation-dice-coefficient 0.7821.

<p align="center">
<img src="https://github.com/lostmartian/CovidRecognizer/blob/main/readme_files/final_images/infection_segmentation.png" align="middle" height="450" width="500">
<br>
Infection segmentation model accuracy and lose along with mask predictions
</p>

## ACKNOWLEDGEMENTS:

[1] - Paiva, O., 2020. CORONACASES.ORG - Helping Radiologists To Help People In More Than 100 Countries! Coronavirus Cases. See [here](https://coronacases.org/)

[2] - Kaggle dataset available [here](https://www.kaggle.com/andrewmvd/covid19-ct-scans)
