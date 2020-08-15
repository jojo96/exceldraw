## Importing modules
import exceldraw
from exceldraw import edraw
## You need opencv, numpy, pandas, easygui, unicodedata


dd,ee = edraw.excelDraw() #excelDraw function returns 2 dataframes
#This would prompt a dialog box and you need to select an image. The image has to be colored.

#Converting data frames to csv. Pass dataFrameName.to_csv(Output_path)
dd.to_csv(r'C:\Users\admin\Desktop\Computational Neuroscience\dist_alx\dds.csv')
ee.to_csv(r'C:\Users\admin\Desktop\Computational Neuroscience\dist_alx\eds.csv')
