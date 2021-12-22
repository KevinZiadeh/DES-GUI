# DES-GUI
> University Project (EECE 455 @ AUB) where we implement DES and tripleDES encryption and decryption with a GUI

## Requirements
  To be able to run this program, the following is needed
```
* Python 3.7 or BELOW. Kivy does not work with python 3.8+
* Kivy 1.11.1
```

## Overview
The project consists of implementing DES encryption and decryption with all necessary functions and computations, and output the ciphertext/plaintext with all the steps taken in each round.
The input and output are in hexadecimal. To get more in depth information on each round, you can click on the "Round x-y" button on the right.
We have also added hexadecimal to binary and binary to hexadecimal converter. This converter converts each byte by itself:
```
1F => bin(1)+bin(F) => 0001 1111 => 00011111
1011101 => 101 1001 => 0101 1001 => 5D
```

## Usage
```
$ git clone https://github.com/KevinZiadeh/DES-GUI.git
$ cd DES-GUI
$ pip install -r requirements.txt
```

## Run
In order to run this application, make sure you have the correct python and kivy version installed then run
```
$ python main.py
```

![](res/1.PNG?raw=true)
---
![](res/2.PNG?raw=true)
---
![](res/3.PNG?raw=true)
---
![](res/4.PNG?raw=true)
---
![](res/5.PNG?raw=true)