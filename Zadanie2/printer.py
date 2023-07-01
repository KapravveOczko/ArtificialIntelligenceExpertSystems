import matplotlib.pyplot as plt
import numpy
import pandas
import os

'''
the goal of the printer.py file is to support program with creating graphs used by user to compare the data
'''

'''
aets data from file
'''
def getData():

    file_path = './data/f8_1p_prep.xlsx'
    x_cor=0
    y_cor=0
    x_ref=0
    y_ref=0

    if os.path.exists(file_path):

        excel_data = pandas.read_excel(file_path)
        print(excel_data)

        x_cor = excel_data.iloc[:, 0][0:].tolist()  #coordinates
        y_cor = excel_data.iloc[:, 1][0:].tolist()
        x_ref = excel_data.iloc[:, 2][0:].tolist()  #reference
        y_ref = excel_data.iloc[:, 3][0:].tolist()
        print(x_cor)
        print(y_cor)
        print(x_ref)
        print(y_ref)

    else:
        print("Plik nie istnieje.")

    return x_cor,y_cor,x_ref,y_ref

def printData(x_cor,y_cor,x_ref,y_ref):

    fig, ax = plt.subplots()
    ax.set_title('reference data to coordiantes plot')
    ax.plot(x_ref, y_ref, label='blue data')
    ax.plot(x_cor, y_cor, 'ro', label='coordinates')
    ax.legend(loc='upper center')
    plt.show()

    return True


