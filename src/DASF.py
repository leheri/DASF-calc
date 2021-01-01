# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:14:20 2020

@author: Lea Richter
"""

import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
from scipy.signal import find_peaks


def calc_dasf(m) : 
    spectrum = pd.read_csv(m, sep = "\t", thousands=',')
    
    # Defines the data for x and y axis
    wavelength = spectrum.iloc[:,0]
    absorption = spectrum.iloc[:,1]
    
    # Customization of the absorption plot appearance
    plt.xlabel("wavelength [nm]")
    plt.ylabel("A")
    plt.grid(True, alpha = 0.9, linestyle="dotted")

    # Plots and saves the absorption plot
    xrange = wavelength
    yrange = absorption
    plt.plot(xrange, yrange)
    plt.savefig(os.path.join("results", str(file)+"_absorption.png"), bbox_inches='tight', dpi=300)
    plt.clf()
    
    # Calculates 1/lambda and stores it in a column named "1/lambda"
    spectrum["1/lambda"] = 1/wavelength
    
    # Calculates ln(alpha/lambda) and stores it in column "ln(alpha/lambda)"
    division = absorption / wavelength
    spectrum["ln(alpha/lambda)"] = np.log2(division)
    
    # Stores derivative dln(alpha/lambda) / d1/lambda in column
    spectrum_diff = spectrum.diff()
    spectrum["diff"] = spectrum_diff.loc[:,"ln(alpha/lambda)"] / spectrum_diff.loc[:,"1/lambda"]
    
    # Calculates energy in eV and stores it in column
    spectrum["energy [eV]"] = 1240.0 / wavelength
    
    # Determines maximum (corresponding to Eg)
    band_gap = find_peaks(spectrum.loc[:,"diff"],width = 2, height = 1.5*spectrum.loc[:,"diff"].mean())
    
    # Plots the energy against derivative
    plt.plot(spectrum.loc[:,"energy [eV]"], spectrum.loc[:,"diff"])
    
    # Draws a line in the plot for maxima (Eg) and stores them in Data Frame
    bg_list = []
    files_list = []    
    
    for i in band_gap[0] :
        bg_value = spectrum.loc[i, "energy [eV]"]
        bg_diff = spectrum.loc[i,"diff"]
        plt.vlines(bg_value, 
                   0.9*bg_diff, 
                   1.05*bg_diff)
        plt.text(bg_value, 
                 0.9*bg_diff,
                 bg_value.round(3),
                 rotation = "vertical",
                 va = "top",
                 ha = "center")
        bg_list.append(bg_value.round(3))
        files_list.append(str(file))
                                          
    df_bg = pd.DataFrame(list(zip(files_list , bg_list)), 
                         columns = ['files', 'band-gaps'])     
       
    # Plots the DASF graph
    plt.xlabel("energy [eV]") 
    plt.yticks([])
    plt.tick_params(axis = "y", length = 0)
    
    # Saves graphs and files
    spectrum.to_csv(os.path.join("results",str(file)+"_calc.txt"), sep = "\t")
    plt.savefig(os.path.join("results", str(file)+"_DASF.png"), bbox_inches='tight', dpi=300)
    plt.clf()
    
    # returns Data Frame with band-gaps of this data file
    return df_bg


df_bg_all = pd.DataFrame(columns =['files', 'band-gaps']) 

# Generates directory "results" if it does not exist
if not os.path.exists("results") :
    os.mkdir("results")

# Executes above defined function for all .txt and .csv files in the folder
files = os.listdir(".")
for file in files : 
    if not (file.endswith(".txt") or file.endswith(".csv")) :
        continue
    df_bg_local = calc_dasf(file)
    df_bg_all = df_bg_all.append(df_bg_local, ignore_index = True)

# Saves the band-gaps of each data file in a file    
df_bg_all.to_csv(os.path.join("results","band-gaps.txt"), sep = "\t")
   
    

