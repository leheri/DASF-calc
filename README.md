# Calculation of band-gaps with the DASF method

This script calculates the band-gap of a material from its absorption spectrum data. A derivation of the absorption spectrum fitting (DASF) method is used according to Souri and Tahan [1]. 

## How does the script work?

Generates the absorption spectrum for all `.csv` and `.txt` files (data-files) within the directory. Additionaly, the data is processed according to the DASF method and plotted. Furthermore, a `.csv` -file of the calculations is generated as well as a file that contains the band-gap for all data files within the directory.

## Execution of the script

The file `test-DASF.py` should be in the directory of the files to be used on. You should have Python installed as well as the packages pandas, matplotlib, scipy and os. If you do not work with code frequently, you have the option to additionaly download the `DASF.batch` -file into the same directory. You can then execute the code by simply clicking on the `DASF.batch` file. The execution will take place in your terminal (You still need to have installed python and the packages).

#### How to run the script - step by step

1. Check if you have python installed and install it if not. A beginners guide can be found [here](https://wiki.python.org/moin/BeginnersGuide/Download)
1. Create a directory and copy all data that you want to have analyzed in that folder. The files should be `.csv` or `.txt`
1. Download `test-DASF.py` and `DASF.batch` from `\src` in this repository and save it in the same directoy
1. Run the script by either
  	1. clicking on `DASF.batch` - the script will be executed in the terminal or
  	1. by running `test-DASF.py` in an IDE or the terminal
1. Obtain the outcome files in the `results` folder

#### Installing python packages using pip install

If you downloaded and installed python you can easily install the packages in your terminal by executing
```
pip install matplotlib
```
```
pip install pandas
```
```
pip install numpy
```
```
pip install scipy
```

## Input data

You can name the data files as you like. They should be in `.csv` or a `.txt` format. In the first column should be the wavlength and in the second the absorption seperated by a tabulator. The first row should contain the header (column names can be chosen by you). This format is depicted here:

```python
"wavelength" "absorption"
w1  a1
w2  a2
...
```

## Outcome

The script will generate a new directory `\results` (if it does not exist already) containing
* for each data file: the absorption spectrum `filename_absorption.png`
* for each data file: the spectrum of the DASF with band-gaps indicated by lines `filename_DASF.png`
* for each data file: a file containing the conducted calculations if you want to plot it differently `filename_calc.csv`
* for all files: a file containing the name of the respective data file and the caluclated band-gaps from that file `band-gaps.csv`


## Reference

[1] [Souri, D. & Tahan, Z. E. A new method for the determination of optical band gap and the nature of optical transitions in semiconductors. Appl. Phys. B Lasers Opt. 119, 273–279 (2015).](https://link.springer.com/article/10.1007%2Fs00340-015-6053-9)
