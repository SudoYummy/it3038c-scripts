# IT3038C - Lab 7

### Installation
Install the Pillow module by using pip.

```pip install --upgrade Pillow```


Note at the top of the .py file there are three imports:

```python
import PIL
from PIL import Image
from PIL import ImageFilter
```
### Usage
There is an image called <b>corgi.jpg</b> stored in the Lab7 folder. This is the example image for this program. This can be changed by putting any image in this folder and changing the following line to include your image.

```python
image = Image.open("corgi.jpg")
```
Simply run in Lab7 folder by typing <b>python .\lab7.py</b>

Each image should automatically open and display the changes to it. Be sure to close the image tabs or the program won't quit.
### Sources
https://pillow.readthedocs.io/en/stable/index.html

https://note.nkmk.me/en/python-pillow-concat-images/
