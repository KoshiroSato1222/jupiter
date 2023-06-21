import matplotlib.pyplot as plt
import requests, lxml.html, io
from PIL import Image

res = requests.get("https://paiza.hatenablog.com/entry/paizacloud_jupyter_notebook/2017/12/27")
root = lxml.html.fromstring(res.text).getroottree()
for imgElement in root.xpath("//img")[0:10]:
    url = imgElement.attrib["src"]
    res = requests.get(url)
    image = Image.open(io.BytesIO(res.content))
    plt.figure(figsize=(2, 2))
    plt.imshow(image)
plt.show()