
# Tensorflow Setting Guide

v1.0 2022.08.01 First release

For Machine learning, we need to use Python and Tensorflow which is most popular programing language and deep learning algorithm.
Here, I am going to explain from the beginng of installing python to Tensorflow  package in the GPU environment. Futher understanding of python langauage, tensorflow, GPU driver installation and so on, learn from online by yourself.

See the overview of this document.
1. Version Compatibility Check
2. Install Python
3. Install Graphic Driver
4. Install CUDA(if GPU is available)
5. Install VScode
6. Run deep learning example
7. Error history during setting

Appendix. 
1. Restrictions
Only consider Window OS not linux or Mac.
2. Terms and condition.
3. Reference


# 1. Version compatibility
Unfortunately, the new version is not the best solution for python and tensorflow. You need to consider the compatible version of python, tensorflow, GPU drvier, CUDA and Ansys, too.
See below site for the reference.

First of all, you need to select GPU driver for your purpose. If you only consider tensorflow not like Ansys, CST, you can just skip select GPU driver. Also, if you don't have GPU card or not consider GPU accelation, you don't need to consider GPU and CUDA, cuDNN.
But, the GPU and CUDA option accelate much in ML.


### 1)  Ansys GPU Acceleator Capabilities

https://www.ansys.com/content/dam/it-solutions/platform-support/gpu-accelerator-capabilities-2022-r1.pdf


### 2) CST GPU Computing Guide

https://www.readkong.com/page/cst-studio-suite-r-2021-gpu-computing-guide-9158500


According to the their recommendation, check the proper graphic card and driver version.

Because different GPU driver version may generate unknown issues in some cases, the GPU driver version should be checked by personally. 

In my case, my system is only affordable with 442.xx for CST and Ansys.


### 3) CUDA version check

Then, you have to choose the CUDA version.

CUDA is a parallel computing platform and programming model created by NVIDIA. With more than 20 million downloads to date, CUDA helps developers speed up their applications by harnessing the power of GPU accelerators.

https://blogs.nvidia.com/blog/2012/09/10/what-is-cuda-2/

CUDA Toolkit and Corresponding Driver Versions is like below.

https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html

| CUDA Toolkit                                      | Toolkit Driver Version (Linux) | Toolkit Driver Version (Windows) |
|---------------------------------------------------|--------------------------------|----------------------------------|
| CUDA 11.7 GA                                      | >=515.43.04                    | >=516.01                         |
| CUDA 11.6 Update 2                                | >=510.47.03                    | >=511.65                         |
| CUDA 11.6 Update 1                                | >=510.47.03                    | >=511.65                         |
| CUDA 11.6 GA                                      | >=510.39.01                    | >=511.23                         |
| CUDA 11.5 Update 2                                | >=495.29.05                    | >=496.13                         |
| CUDA 11.5 Update 1                                | >=495.29.05                    | >=496.13                         |
| CUDA 11.5 GA                                      | >=495.29.05                    | >=496.04                         |
| CUDA 11.4 Update 4                                | >=470.82.01                    | >=472.50                         |
| CUDA 11.4 Update 3                                | >=470.82.01                    | >=472.50                         |
| CUDA 11.4 Update 2                                | >=470.57.02                    | >=471.41                         |
| CUDA 11.4 Update 1                                | >=470.57.02                    | >=471.41                         |
| CUDA 11.4.0 GA                                    | >=470.42.01                    | >=471.11                         |
| CUDA 11.3.1 Update 1                              | >=465.19.01                    | >=465.89                         |
| CUDA 11.3.0 GA                                    | >=465.19.01                    | >=465.89                         |
| CUDA 11.2.2 Update 2                              | >=460.32.03                    | >=461.33                         |
| CUDA 11.2.1 Update 1                              | >=460.32.03                    | >=461.09                         |
| CUDA 11.2.0 GA                                    | >=460.27.03                    | >=460.82                         |
| CUDA 11.1.1 Update 1                              | >=455.32                       | >=456.81                         |
| CUDA 11.1 GA                                      | >=455.23                       | >=456.38                         |
| CUDA 11.0.3 Update 1                              | >= 450.51.06                   | >= 451.82                        |
| CUDA 11.0.2 GA                                    | >= 450.51.05                   | >= 451.48                        |
| CUDA 11.0.1 RC                                    | >= 450.36.06                   | >= 451.22                        |
| CUDA 10.2.89                                      | >= 440.33                      | >= 441.22                        |
| CUDA 10.1 (10.1.105 general release, and updates) | >= 418.39                      | >= 418.96                        |
| CUDA 10.0.130                                     | >= 410.48                      | >= 411.31                        |
| CUDA 9.2 (9.2.148 Update 1)                       | >= 396.37                      | >= 398.26                        |
| CUDA 9.2 (9.2.88)                                 | >= 396.26                      | >= 397.44                        |
| CUDA 9.1 (9.1.85)                                 | >= 390.46                      | >= 391.29                        |
| CUDA 9.0 (9.0.76)                                 | >= 384.81                      | >= 385.54                        |
| CUDA 8.0 (8.0.61 GA2)                             | >= 375.26                      | >= 376.51                        |
| CUDA 8.0 (8.0.44)                                 | >= 367.48                      | >= 369.30                        |
| CUDA 7.5 (7.5.16)                                 | >= 352.31                      | >= 353.66                        |
| CUDA 7.0 (7.0.28)                                 | >= 346.46                      | >= 347.62                        |


### 4) Tensorflow version check

Tensorflow corresponding CUDA/cuDNN version compatibility from Tensorflow official site.

https://www.tensorflow.org/install/source#gpu

- GPU

| Version            | Python version | Compiler  | Build tools  | cuDNN | CUDA  |
|--------------------|----------------|-----------|--------------|-------|-------|
| tensorflow-2.9.0   | 3.7-3.10       | GCC 9.3.1 | Bazel 5.0.0  | 8.1   | 11.2  |
| tensorflow-2.8.0   | 3.7-3.10       | GCC 7.3.1 | Bazel 4.2.1  | 8.1   | 11.2  |
| tensorflow-2.7.0   | 3.7-3.9        | GCC 7.3.1 | Bazel 3.7.2  | 8.1   | 11.2  |
| tensorflow-2.6.0   | 3.6-3.9        | GCC 7.3.1 | Bazel 3.7.2  | 8.1   | 11.2  |
| tensorflow-2.5.0   | 3.6-3.9        | GCC 7.3.1 | Bazel 3.7.2  | 8.1   | 11.2  |
| tensorflow-2.4.0   | 3.6-3.8        | GCC 7.3.1 | Bazel 3.1.0  | 8.0   | 11.0  |
| tensorflow-2.3.0   | 3.5-3.8        | GCC 7.3.1 | Bazel 3.1.0  | 7.6   | 10.1  |
| tensorflow-2.2.0   | 3.5-3.8        | GCC 7.3.1 | Bazel 2.0.0  | 7.6   | 10.1  |
| tensorflow-2.1.0   | 2.7, 3.5-3.7   | GCC 7.3.1 | Bazel 0.27.1 | 7.6   | 10.1  |

With all consideration of compatibility in my system, I chose GPU driver 442.xx, Tensoflow 2.3.0, Python 3.8, CUDA 10.2, cuDNN 7.6.


|Tensorflow|CUDA|cuDNN|GPU Driver|Python|
|-|-|-|-|-|
|2.3.0|10.2.89|7.6.5.32|442.92|3.8.10|

My system is like below.
|Item|Details|
|----|----|
|CPU|Intel(R) Xeon(R) Gold 6254 CPU @ 3.10GHz   3.09 GHz  (2 processors)|
|Memory|512GB|
|Storage|2TB for C, 5.5TB for D,E, 256GB for F|
|GPU for Accelation|NVIDIA RTX 8000x2|
|GPU for monitor|NVIDIA P2000|
|OS|Windows 10 Pro for Workstation|


# 2. Install Graphic driver and CUDA

After Tensorflow version 2, it can handle CPU and GPU both. If you use older tensorflow version, you should install tensorflow-gpu package. If you have Graphic driver from NVIDIA(not AMD), it's better enabling GPU option. 

All the files used in this document kept in below path.

\\MDSD000P9012824\전설1팀_Temp\Util\EMC Tool install files\GPU driver\


## 2.1 GPU Driver

Although RTX 8000 originally supports CUDA 11.0, 442.xx is installed and 442.xx is supported till CUDA 10.2.



## 2.2 CUDA Toolkit

Refer this https://kaen2891.tistory.com/20

To download, you need to make an account of NVIDIA developer.

Below chapters are about installing CUDA and cuDNN.


### 2.2.1 Available CUDA version check

To check available CUDA version, you can check it from command mode from Windows.

'win' + r, then 'cmd' enter.

![cmd open](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc1_cmd.JPG?raw=true)

From the command window, move the path and enter the nvidia-smi.

"nvidia-smi.exe" displays what drivers are installed and other information.
or "nvcc --version" also gives you the correct version of CUDA.

![nvcc version](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc2_nvcc%20version.JPG?raw=true)


Below is the example of usage of GPU.

```
C:> cd C:\Program Files\NVIDIA Corporation\NVSMI
C:\Program Files\NVIDIA Corporation\NVSMI > nvidia-smi

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 442.92       Driver Version: 442.92       CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name            TCC/WDDM | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Quadro RTX 8000     TCC  | 00000000:15:00.0 Off |                  Off |
| 33%   56C    P0    65W / 260W |      9MiB / 48767MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  Quadro RTX 8000     TCC  | 00000000:2D:00.0 Off |                  Off |
| 40%   64C    P0    69W / 260W |      9MiB / 48767MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   2  Quadro P2000       WDDM  | 00000000:99:00.0 Off |                  N/A |
| 46%   35C    P8     5W /  75W |   1178MiB /  5120MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    2      3416    C+G   Insufficient Permissions                   N/A      |
|    2      4184    C+G   ...hell.Experiences.TextInput.InputApp.exe N/A      |
|    2      5492      C   Insufficient Permissions                   N/A      |
|    2     11016    C+G   C:\Windows\explorer.exe                    N/A      |
|    2     12120    C+G   ...dows.Cortana_cw5n1h2txyewy\SearchUI.exe N/A      |
|    2     13124    C+G   ...t_cw5n1h2txyewy\ShellExperienceHost.exe N/A      |
|    2     14700    C+G   C:\Program Files\Typora\Typora.exe         N/A      |
|    2     15824    C+G   ...es\Google\Chrome\Application\chrome.exe N/A      |
|    2     38084    C+G   ...x64__8wekyb3d8bbwe\Microsoft.Photos.exe N/A      |
|    2     38216    C+G   Insufficient Permissions                   N/A      |
|    2     40140    C+G   Insufficient Permissions                   N/A      |
|    2     41696    C+G   ...es (x86)\Internet Explorer\iexplore.exe N/A      |
|    2     43072    C+G   Insufficient Permissions                   N/A      |
|    2     48284    C+G   ...rogram Files\Microsoft VS Code\Code.exe N/A      |
|    2     50388    C+G   ....117.0_x64__8wekyb3d8bbwe\YourPhone.exe N/A      |
+-----------------------------------------------------------------------------+
```

With 442.92 GPU driver, you are able to check the CUDA version 10.2.



### 2.2.2 CUDA Toolkit Install

Access this site to download the proper version of CUDA toolkit.

https://developer.nvidia.com/cuda-toolkit-archive

Download CUDA toolkit 10.2.

Excute the download file and install.




### 2.2.3 cuDNN install

NVIDIA CUDA Deep Neural Network (cuDNN) is a GPU-accelerated library of primitives for deep neural networks. It provides highly tuned implementations of routines arising frequently in DNN applications.

https://likecode.tistory.com/219

cuDNN installation official guide

https://docs.nvidia.com/deeplearning/cudnn/archives/cudnn_765/cudnn-install/index.html#prerequisites-windows

Just copy from cuDNN, to CUDA toolkit bin folder.

### 2.3 GPU Setting Change

Then, let's check nvidia-smi, again. It shows the driver status.

![nvidia-smi status new](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/nvidia-smi%20status%20new.JPG?raw=true)

There is TCC/WDDM and ECC whcih are the option for the core accelation.
TCC = Tesla Compute Cluster, It blocks to using GPU for monitor ouput,
WDDM = Windows Display Driver Model, it is for the display purpose model.
ECC = Error correction Code is to check error while using GPU. But it makes delay of processing, so it recommends to turn off this mode.


1. Enable TCC mode
nvidia-smi -g {_GPU_ID_}  -dm {0|1} # 0 = WDDM, 1 = TCC
```
c: > nvidia-smi -g 0 -dm 1 # for GPU No.0
c: > nvidia-smi -g 1 -dm 1 # for GPU No.1

```

2. Disable ECC mode
 nvidia-smi -g {_GPU ID_} --ecc-config={0|1}
```
 c: > nvidia-smi -g 0 --ecc-config=0
 c: > nvidia-smi -g 1 --ecc-config=0
```
If there are error while changing TCC and ECC mode, re install GPU driver. In my case, it is the only solution. Also, you need to restart system after changing mode.

Finally check again from the nvidia-smi.


# 3. Install Python

Install Python from below link.

[https://www.python.org/downloads/windows/ ](https://www.python.org/downloads/windows/)

Currently, tensorflow is available with Python 3.5~3.8.

On my system, Python version 3.8.10 has been installed.


# 4.  Install VScode

VScode is the one of the popular editor tool for SW coding. VScode is free in commercial condition, so there is no restriction to using it.


## 4.1 Install VScode

Just download and install new version!

https://code.visualstudio.com/


## 4.2 Virtual Environment Setting

Virtual environment is useful for the separated development environment. 
For example, you are using only python 3.5 with tensorflow, on the other hand, for data processing, if you need the newest version of python with pandas, what do you have to do?
Are you going to install all these two different python versions and two different packages? If you are handing other more projects? 

The virtual environment supports these different version handling in the virtual environment. For these separated environment managing, it is defined with the different environment name.

This contents refers to https://mr-spock.tistory.com/19
Also, this youtube channel explains very simply, so please refer this for installing python and vscode.
https://youtu.be/e4n2VnhiI28

Below steps are simple steps to make the virual environment on VS code.


### 4.2.1 Generating a new project

At VS code, folder name represents a project. Let's make a new folder from file explorer.
Figuire:![Alt](file explorer.jpg)

```
D:\pythonProject\test_tensorflow\
```

If powershell shows error about the default execution policy, type this.

```
PS ... > Set-ExecutionPolicy Unrestricted
```
https://torbjorn.tistory.com/437

Open this folder from VScode.
> File > Open Folder...
> Select  the new folder for the project

'Ctrl + J' to  open Panel for terminal window if there is no terminal.

Now you can see this below.
```

Microsoft Windows [Version 10.0.19044.1645]
(c) Microsoft Corporation. All rights reserved.

D:\pythonProject\test_tensorflow>
```
### 4.2.2 Generate the new virtual environment
Form the terminal window,
```
> python -m venv venv_tf # python -m venv {venv name}
```
Then, you can see the venv_tf folder from left side bar which is generated on the folder together.

All the python modules are installed here.

> 'Ctrl+Shift+P'

'Select interpreter' on the Top search bar > Select 'Python' from c:\python\python38 which you installed on.

> 'Ctrl+Shift+P'

'Python: Select interpreter' > select python from venv_ts

> 'Ctrl+Shift+`'

This makes active the venv_ts, or you can type activate.bat from the terminal windows.

![venv enable](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc2_venv%20enable.JPG?raw=true)

This is the result of enabling venv.
```
(venv_ts) D:\pythonProject\test_tensorflow>
```
If there is PS(Powershell), you can change it
> 'Ctrl +Shift+P'
> 'Terminal:Select Default Profile'
> Select Command Prompt

![venv defualt profile](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc2_venv%20default%20profile.JPG?raw=true)


### 4.2.3 Install Tensorflow package

We are going to install tensorflow 2.3.0 using pip mode.

From the terminal in VS code venv,
Enter below command.
This command is to install the specific tensorflow version.
```
> pip install tensorflow==2.3.0
```
In this document, Only explans tensorflow package, but there are many useful package like Pandas, Numpy and so on. Please search more for easy coding.


### 4.2.4 Extensions Programs

VScode supports various extensions , so you can install them like this.
Below are for the tensorflow.

'Python' for Python
'C/C++' for run the C/C++ code
'C/C++ Complie Run' for running the C/C++ code compile
'WinGW' for compiling gcc, G++ in Windows

Also, these are the useful extensions.

![extensions](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc2_extensions.JPG?raw=true)





## 5. Run tensorflow example

Now, type the example on edit window.

```python
import tensorflow as tf 
tf.__version__
```
The result is...

```
Successfully opened dynamic library cudart64_101.dll
2.3.0
```

Let's do one more example.

```python
import  tensorflow  as  tf
tensor1  =  tf.constant(3)
print(tensor1)
```

```
~~
tf.Tensor(3, shape=(), dtype=int32)
~~
```

In addition to this, find and practice the following examples.

> Predict shoe size by height
> Distinguishing Images




## 5.4 Project Setting

The project in VS code configures with folder structure, so the folder name is the project name.

### 5.4.1. Generate Project(=folder)

From file tap, open folder,

![open folder](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc2_open%20folder.jpg?raw=true)


At a your own folder, select or generate project folder.

![own folder](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc2_own%20folder.jpg?raw=true)


### 5.4.2. Generate File

Generate New file

![img](https://blog.kakaocdn.net/dn/bU8Lo4/btqytsi1pMO/JkGnyT0U630iN25mknJPI0/img.png)

Generate Code file such as c, py, and etc.

![generate code](https://github.com/epsEMC/epsEMC/blob/main/imageTemp/doc2_generate%20code.jpg?raw=true)


Then, type your code and run.

This is the example tensorflow and result.
 ```
 import  tensorflow  as  tf

tensor1  =  tf.constant(3)

print(tensor1)
__________________________________________________________________________________________
(tensorflowTest) D:\pythonProject\test\ts_tuto_youtube> cmd /C "d:\pythonProject\tensorflowTest\Scripts\python.exe c:\Users\RDS_USER\.vscode\extensions\ms-python.python-2022.10.1\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher 60881 -- d:\pythonProject\test\ts_tuto_youtube\tensor_1.py "
2022-08-01 16:22:15.890306: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cudart64_101.dll
2022-08-01 16:22:30.813627: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library nvcuda.dll
2022-08-01 16:22:36.483818: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 0 with properties: 
pciBusID: 0000:15:00.0 name: Quadro RTX 8000 computeCapability: 7.5
coreClock: 1.77GHz coreCount: 72 deviceMemorySize: 47.62GiB deviceMemoryBandwidth: 625.94GiB/s
2022-08-01 16:22:36.496103: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 1 with properties: 
pciBusID: 0000:2d:00.0 name: Quadro RTX 8000 computeCapability: 7.5
coreClock: 1.77GHz coreCount: 72 deviceMemorySize: 47.62GiB deviceMemoryBandwidth: 625.94GiB/s
2022-08-01 16:22:36.507545: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 2 with properties: 
pciBusID: 0000:99:00.0 name: Quadro P2000 computeCapability: 6.1
coreClock: 1.4805GHz coreCount: 8 deviceMemorySize: 5.00GiB deviceMemoryBandwidth: 130.53GiB/s
2022-08-01 16:22:36.518390: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cudart64_101.dll
2022-08-01 16:22:36.564282: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cublas64_10.dll
2022-08-01 16:22:36.610259: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cufft64_10.dll
2022-08-01 16:22:36.624214: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library curand64_10.dll
2022-08-01 16:22:36.680354: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cusolver64_10.dll
2022-08-01 16:22:36.708059: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cusparse64_10.dll
2022-08-01 16:22:36.815197: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cudnn64_7.dll
2022-08-01 16:22:36.828806: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0, 1, 2
2022-08-01 16:22:36.863161: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  AVX2To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-08-01 16:22:37.246345: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x2990fedb470 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2022-08-01 16:22:37.254052: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2022-08-01 16:22:37.526397: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 0 with properties:
pciBusID: 0000:15:00.0 name: Quadro RTX 8000 computeCapability: 7.5
coreClock: 1.77GHz coreCount: 72 deviceMemorySize: 47.62GiB deviceMemoryBandwidth: 625.94GiB/s
2022-08-01 16:22:37.540164: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 1 with properties:
pciBusID: 0000:2d:00.0 name: Quadro RTX 8000 computeCapability: 7.5
coreClock: 1.77GHz coreCount: 72 deviceMemorySize: 47.62GiB deviceMemoryBandwidth: 625.94GiB/s
2022-08-01 16:22:37.551868: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 2 with properties:
pciBusID: 0000:99:00.0 name: Quadro P2000 computeCapability: 6.1
coreClock: 1.4805GHz coreCount: 8 deviceMemorySize: 5.00GiB deviceMemoryBandwidth: 130.53GiB/s
2022-08-01 16:22:37.564129: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cudart64_101.dll
2022-08-01 16:22:37.570662: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cublas64_10.dll
2022-08-01 16:22:37.575664: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cufft64_10.dll
2022-08-01 16:22:37.582541: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library curand64_10.dll
2022-08-01 16:22:37.588797: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cusolver64_10.dll
2022-08-01 16:22:37.594555: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cusparse64_10.dll
2022-08-01 16:22:37.600566: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cudnn64_7.dll
2022-08-01 16:22:37.614659: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0, 1, 2
2022-08-01 16:22:42.009773: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1257] Device interconnect StreamExecutor with strength 1 edge matrix:
2022-08-01 16:22:42.016647: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1263]      0 1 2
2022-08-01 16:22:42.021430: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1276] 0:   N Y N
2022-08-01 16:22:42.025214: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1276] 1:   Y N N
2022-08-01 16:22:42.030002: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1276] 2:   N N N
2022-08-01 16:22:42.062802: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1402] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 44532 MB memory) -> physical GPU (device: 0, name: Quadro RTX 8000, pci bus id: 0000:15:00.0, compute capability: 7.5)
2022-08-01 16:22:42.112865: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1402] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:1 with 44532 MB memory) -> physical GPU (device: 1, name: Quadro RTX 8000, pci bus id: 0000:2d:00.0, compute capability: 7.5)
2022-08-01 16:22:42.126436: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1402] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:2 with 3835 MB memory) -> physical GPU (device: 2, name: Quadro P2000, pci bus id: 0000:99:00.0, compute capability: 6.1)
2022-08-01 16:22:42.175126: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x2999ffa38e0 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2022-08-01 16:22:42.182641: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Quadro RTX 8000, Compute Capability 7.5
2022-08-01 16:22:42.188379: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (1): Quadro RTX 8000, Compute Capability 7.5
2022-08-01 16:22:42.194194: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (2): Quadro P2000, Compute Capability 6.1
tf.Tensor(3, shape=(), dtype=int32)

(tensorflowTest) D:\pythonProject\test\ts_tuto_youtube>
```


# 6. End

Machine Learning and Deep learning are tools for your idea.
All the results depend on your idea! Please keep think and extend your idea. Then, these tools make the best result.



# Reference

1. VS code installation
    : https://mickael-k.tistory.com/12?category=798523
 
2. VS code environment setting 
    : https://mickael-k.tistory.com/13
   
3.  VS code virtual environment setting
    : [Visual Studio Code 파이썬(Python) 가상개발환경(venv) 셋팅 (tistory.com)](https://mr-spock.tistory.com/19)

4. Tensorflow installation guide
   : https://www.tensorflow.org/install

5. VScode setting guide for Tensorflow from Youtube
   : https://youtu.be/e4n2VnhiI28

6. Tensorflow lecture from youtube
   : https://youtu.be/ivfp2wpPLzs

# Terms and conditions

|Terms|Definition|
|-|-|
|CUDA core|SStandard NVIDIA parallel processing unit.|
|ECC memory|Error Correcting Code (ECC) memory supports checking whether the read/write of the memory is error-free.|
|TCC|Tesla Computer Cluster (TCC) Driver Mode. High-performance drivers optimized for computational utilization of NVIDIA GPUs.|
|Tensor core|A full-precision, mixed-precision (ultimately integer math) parallel processing unit dedicated to matrix multiplication operations.|
|Tensor RT|NVIDIA framework that optimizes runtime performance of TensorFlow, Caffe and other standard framework networks running on GPUs with tensor cores (using low precision and integer math).|

> https://support.cognex.com/docs/vidi_341/web/KO/vidisuite/Content/ViDi_Topics/HowTo/nvidia_gpuglossary.htm?TocPath=ViDi%20%EC%84%B1%EB%8A%A5%20%EA%B0%80%EC%9D%B4%EB%93%9C%7CNVIDIA%20GPU%20%EC%84%A0%ED%83%9D%20%EB%B0%8F%20%EA%B5%AC%EC%84%B1%7C_____1



> Written with [StackEdit](https://stackedit.io/).
