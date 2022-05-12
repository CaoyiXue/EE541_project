## EE541_project
### Data Prepare
1. 
Download data from [Google Drive](https://drive.google.com/file/d/1xJegrU82qZxjOIWu7CtHwWHVpiExpdSQ/view?usp=sharing), roughly 1.5GB
The structure for this folder is 
<p align="center"><img src="images/data_folder.png" alt="data_folder" width="300" /></p>

We run our code on GoogleColab. If you don't use colab, you can skip these code in the beginning.
```python
from google.colab import drive
drive.mount('/content/drive/', force_remount=True)
```
After downloading this data file, you need to modify this code to satisfy the root path where you store data file 
```python
path = "/content/drive/MyDrive/EE541_project/"
```
2. 
Please use [VerifyClass.ipynb](VerifyClass.ipynb) to verify pictures in one data folder corresponds to the class label (data folder name). For example, pictures in filder "A" should has "A" as the first letter of their name. If it doesn't plot error information, then it's safe to go next.
3. 
We use the HDF5 file to restore our data, so you need to run [BeforeTrain.ipynb](BeforeTrain.ipynb) to get ```data.hdf5```, only need to run "Store data to HDF5 file" part. As a result, you will get ```data.hdf5``` with keys ```train```, ```train_label```, ```test```, ```test_label```, ```test2```, ```test2_label```.
The rest code on it is calculating mean and standard deviation for our training data, and respectively plot sample pictures from [Kaggle](https://www.kaggle.com/datasets/grassknoted/asl-alphabet) and [Roboflow](https://public.roboflow.com/object-detection/american-sign-language-letters).
4. 
[Noise.ipynb](Noise.ipynb) just show how torchvision transforms and two noises we defined look like.

### Training
1. 
In [SimpleModel.ipynb](SimpleModel.ipynb), we test 4 simple model from Net(), NetDropout(), NetBatchnorm(). And use one simple approach to find the suitable learning rate. Finally, we plot corresponding results for analysis.
2. 
In [ResNet18.ipynb](ResNet18.ipynb), we use transfer learning with ResNet18 to find the suitable augmentation. In our experiments, the "best" one is augmentation 2 mentioned in [ResNet18.ipynb](ResNet18.ipynb).
3. 
