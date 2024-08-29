# Skin-Cancer-Diagnosis-with-YOLOv8

![Alt text](https://github.com/Eminkorkut/Skin-Cancer-Diagnosis-with-YOLOv8-/blob/main/files/mainPhoto.png)

## What is the purpose of the project?
> Skin cancer is a common and serious disease and can be fatal if left untreated. However, when skin cancer is detected early and correctly, the chances of treatment success are high. Therefore, it is important to use effective methods to diagnose skin cancer. Dermatoscopic images are an important source for the diagnosis of skin cancer, and computer-aided diagnosis systems with deep learning models that process these images can be a helpful tool for doctors to diagnose skin cancer early and accurately. For this purpose, a program with a user interface and deep learning models was developed using the Python programming language. By entering dermatoscopic images to be analyzed into this program, the program detects the types of skin cancer in the image entered by the program and compares the accuracy rate of the detection success for each type as a percentage, the type with the highest accuracy rate is notified to the user and an important tool that can help for diagnosis is presented. Artificial intelligence is applied in the health sector and many other fields today. Deep learning, which gives very successful results especially in image processing, is preferred in the processing and interpretation of medical images. Among the deep learning algorithms, the YOLO (You Only Look Once) algorithm and the Darknet model provide more FPS and clearer results thanks to its higher processing speed compared to other algorithms. Therefore, YOLO algorithm is preferred in this study.

## Method Used

<p align="center">  
  <img src="https://github.com/Eminkorkut/Skin-Cancer-Diagnosis-with-YOLOv8-/blob/main/files/PyQt-Logo.wine.png" alt="PyQt Logo" width="100"/>
  <img src="https://github.com/Eminkorkut/Skin-Cancer-Diagnosis-with-YOLOv8-/blob/main/files/Pardus_logo.svg.png" alt="Pardus Logo" width="100"/>
  <img src="https://github.com/Eminkorkut/Skin-Cancer-Diagnosis-with-YOLOv8-/blob/main/files/Python-Symbol.png" alt="Python Symbol" width="100"/>
</p>

> Dermatoscopic images are an important source of data for detecting skin cancer. These images show the symptoms of skin cancer and thus skin cancer can be detected. In deep learning models, the detection success of the model is directly proportional to the number of data used to train the model. That is, the more data used to train the model, the better the detection success of the model. For this reason, the HAM10000 (https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000) dataset, which contains a total of nearly 10,000 dermatoscopic images from different patients, was deemed suitable for this project. The skin cancer images from this dataset were converted into the YOLO format required for training the YOLOv5 object detection model.
> 
> Google Colab cloud service was used to train the YOLOv5 object detection model. Google Colab offers free GPU (Graphics Proccesing Unit) and TPU (Tensor Proccesing Unit) facilities that facilitate the training of models of deep learning based algorithms. Using Google Colab reduces training time compared to personal computers. This means that model training can be completed faster and the project can be ready for use sooner. Success graphs of the trained models are presented in the Model performances section. Once the models were trained, a GUI (Graphical User Interface) was designed to make the project user-friendly and easy to use. PyQt5 (https://www.riverbankcomputing.com/static/Docs/PyQt5/), the Python port of the cross-platform GUI toolkit Qt, was used to create the GUI. In this way, the user interface was created and the project was ready for use. This interface is a completely local work. It is aimed to make a work whose intellectual property rights belong to us. Figure 3 shows the main screen image


## App Images & How to Use it
> After the program runs, you enter your 11 digit number where it says “Please enter your Turkish ID number with 11 digits.” Select the new patient or old patient option and select the image to be examined

> [!WARNING]
> “Old Patient” entry only works for numbers that have already been logged.

> ![Alt text](https://github.com/Eminkorkut/Skin-Cancer-Diagnosis-with-YOLOv8-/blob/main/files/ss1.png)


## Model Training Performances
### Melanoma
![Alt text](https://github.com/Eminkorkut/Skin-Cancer-Diagnosis-with-YOLOv8-/blob/main/files/melanoma_results.png)
### Basal
![Alt text](https://github.com/Eminkorkut/Skin-Cancer-Diagnosis-with-YOLOv8-/blob/main/files/basal_results.png)
### Dermatofibroma
![Alt text](https://github.com/Eminkorkut/Skin-Cancer-Diagnosis-with-YOLOv8-/blob/main/files/dermatofibroma_results.png)
