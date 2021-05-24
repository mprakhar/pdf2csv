# __author__ = 'Prakhar MISRA'
# Created 05/14/2020
# Last edit 05/14/2020
'''
#Purpose:
#-----------------
1. TO read coal poewr platn generation from POSOCO pdf file into csv file 

Reference:


# EDIT History


#Output expected:
#-----------------
# excel files


#Terminology used:
#-----------------
#       
#       
'''

# ref 
# https://medium.com/@umerfarooq_26378/python-for-pdf-ef0fac2808b0
import tabula
from  glob import glob
import pandas as pd
import os.path

def getEnergy(fileName, dict_PP, PPName):
    # read the pdf
    # NOTE # this is valid for reports generated after 2018 08 30. Previous reports had another format
    officialName = dict_PP[PPName][1]
    fieldNameEnergy = dict_PP[PPName][2]
    
    try:
        # read the pdf as df
        page = dict_PP[PPName][0]
        df = tabula.read_pdf(fileName,multiple_tables=True, pages = page)[0]
        #print(df)
        # get the name of the first column
        fieldNamePP = df.columns[0]
        # print the value 
        energyMU = df[df[fieldNamePP]== officialName][fieldNameEnergy].values[0]
        #print(df)
    
    # theremay be error because page ordering is not always consistent. experiment with the next page
    except (IndexError, KeyError): 
        print("error")
        
        try:
            # read the pdf as df
            page = dict_PP[PPName][0]+1
            df = tabula.read_pdf(fileName,multiple_tables=True, pages = page)[0]
            
            # get the name fo the first columns
            fieldNamePP = df.columns[0]
            # print the value 
            energyMU = df[df[fieldNamePP]== officialName][fieldNameEnergy].values[0]
            #print(df)
        except:
            print("error again")
            return "XXX"
        
    #print (energyMU)
    #df[df["3(B)Regional Entities Generation"]=="DADRI-IITPS( 2 * 490 )"]["Unnamed: 7"]
    
    return energyMU


def ParallelgetEnergy(fileName):
    
    date = "20" + fileName[-6:-4]+ "-" + fileName[-8:-6]+ "-" + fileName[-10:-8]
    
    if int(fileName[-6:-4]) >=19:
        # read the pdf
        # NOTE # this is valid for reports generated after 2018 08 30. Previous reports had another format
        officialName = dict_PP[PPName][1]
        fieldNameEnergy = dict_PP[PPName][2]

        try:
            # read the pdf as df
            page = dict_PP[PPName][0]
            df = tabula.read_pdf(fileName,multiple_tables=True, pages = page)[0]
            #print(df)
            # get the name of the first column
            fieldNamePP = df.columns[0]
            # print the value 
            energyMU = df[df[fieldNamePP]== officialName][fieldNameEnergy].values[0]
            #print(df)

        # theremay be error because page ordering is not always consistent. experiment with the next page
        except (IndexError, KeyError): 
            print("error")

            try:
                # read the pdf as df
                page = dict_PP[PPName][0]+1
                df = tabula.read_pdf(fileName,multiple_tables=True, pages = page)[0]

                # get the name fo the first columns
                fieldNamePP = df.columns[0]
                # print the value 
                energyMU = df[df[fieldNamePP]== officialName][fieldNameEnergy].values[0]
                #print(df)
            except:
                print("error again")
                return [date, "XXX"]


        #print (energyMU)
        #df[df["3(B)Regional Entities Generation"]=="DADRI-IITPS( 2 * 490 )"]["Unnamed: 7"]

        return [date, energyMU]
    else:
        return


#run for one pwer plant
def saveEnergycsv(PPName):
    ls = []
    for fileName in glob(os.path.join( "Data", "Emission", "DailyPower", "daily*.pdf")):
        date = "20" + fileName[-6:-4]+ "-" + fileName[-8:-6]+ "-" + fileName[-10:-8]
        #print(fileName)
        
        if int(fileName[-6:-4]) >=19:
            # only run for the data after 20190101
        
            energyMU = getEnergy(fileName, dict_PP, PPName)
            print(date, energyMU)
            ls.append([date, energyMU])

    df_PP = pd.DataFrame(ls, columns=["date", "energu(MU)"])
    df_PP.to_csv("DayEnergy_"+PPName + ".csv")
    # not needed currently
    # can also convert to excel csv 
    #abula.convert_into("daily210520.pdf", "offense_testing.csv", output_format="csv", pages = page)

def ParallelsaveEnergycsv():
    #pool = mp.Pool(processes=4)
    ls = []
    fileList = glob(os.path.join( "Data", "Emission", "DailyPower", "daily*.pdf"))
    ls = map(ParallelgetEnergy, fileList)
    df_PP = pd.DataFrame(ls, columns=["date", "energy(MU)"])
    df_PP.to_csv("DayEnergy_"+PPName + ".csv")
