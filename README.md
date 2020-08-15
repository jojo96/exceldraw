# exceldraw

### Table of Contents

1. [Installation](#installation)
2. [Motivation](#motivation)
3. [Example](#example)
4. [Licensing](#licensing)

## Installation <a name="installation"></a>
The repository contains a zipped file of my Python package excel draw and should be installed via pip.<br/>
Instalation procedure: pip install exceldraw

## Motivation <a name="Motivation"></a>
The package is intended as a simple drawing tool.<br/>
The user will upload an image. The image has to be a colored image(preferably a headshot). The image should have a nice contrast for proper output.<br/>
The package contains the function excelDraw() <br/>

## Example <a name="Example"></a>
This is the way to run the module:

#import the module
import exceldraw
from exceldraw import edraw
csv1,csv2 = edraw.excelDraw()#This would prompt a dialog box and you should select the image
dd.to_csv(r'C:\Users\admin\Desktop\Computational Neuroscience\dist_alx\dds.csv')
ee.to_csv(r'C:\Users\admin\Desktop\Computational Neuroscience\dist_alx\eds.csv')
#'C:\Users\admin\Desktop\Computational Neuroscience\dist_alx\' is the output directory
#In the output directory, you will have two excel file containing the images.


## Licensing <a name="Licensing"></a>

Copyright <2020><br/> Ujjayanta Bhaumik <br/>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
