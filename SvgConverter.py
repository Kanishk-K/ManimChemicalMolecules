from xml.dom import minidom
import xml.dom
import sys

#If the user doesn't provide a filename in the arguement.
try :
    filename = sys.argv[1]
except:
    raise NameError('No file name was provided.')

document = minidom.parse(filename)
#create/access a new file where the content will be stored, if the file exists already clear content.
new_file = open(f"manim_{filename}","w")
root = document.getElementsByTagName("svg")[0]
styles = root.getElementsByTagName("style")
chemical_tags = root.getElementsByTagName("chemical:x-mdl-molfile")
texts = root.getElementsByTagName("text")
circles = root.getElementsByTagName("circle")
lines = root.getElementsByTagName("line")
print("removing style tags")
for style in styles:
    root.removeChild(style)
print("removing chemical mol-file tag")
for chemical_tag in chemical_tags:
    root.removeChild(chemical_tag)
print("removing non-atom text tags, manim doesn't recognize text in svgs.")
for text in texts:
    if text.getAttribute("fill") == "rgb(160,0,0)":
        root.removeChild(text)
print("removing cirlce tags, molecules will display with massive cirlces everywhere without this.")
for circle in circles:
    root.removeChild(circle)
print("replacing line tags with polylines so that manim can read it.")
for line in lines:
    if line.getAttribute("id") != "":
        root.removeChild(line)
    else:
        polyline = document.createElement("polyline")
        polyline.setAttribute("style",line.getAttribute("style"))
        polyline.setAttribute("points",f"{line.getAttribute('x1')},{line.getAttribute('y1')} {line.getAttribute('x2')},{line.getAttribute('y2')}")
        root.replaceChild(polyline,line)
#write new content into the file.
new_file.write(document.toxml())
print("file generated")
#close the new file.
new_file.close()