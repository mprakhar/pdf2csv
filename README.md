This repository aims to provide modules and notebooks for conversion of reports generated in .pdf to .csv to aid in analysis and modelling. 

Following is the list of notebooks and their intended function:


-------
*1*
-------
E01 Read_PPEnergy.ipynb 
-- reads the daily energy consumption of power plants across India (downloaded from https://posoco.in/reports/daily-reports/ using download manager) into .csv format.
-- INPUT: assign the folder path of the downloaded .pdf reports to pdf2csv/helpers/fn_readPOSOCOpdf.py (Line 125). e.g.  "Data", "Emission", "DailyPower", "daily*.pdf". 
-- OUTPUT: converted .csv files will be saved in the root directory itself. 
pdfFileObj = open(" E:\OneDrive - 総合地球環境学研究所\AQM_Research\Data\Raw\PowerGeneration\POSOCO_NRLDC\daily010520.pdf", 'rb')


