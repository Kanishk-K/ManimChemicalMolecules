# Manim Chemical Molecules
A program that can convert svg depictions of molecules into manim-compatible ones.

# Getting the initial svg file for conversion
- First, go to a website such as http://molview.org/ and select a molecule.
![Molview](https://user-images.githubusercontent.com/64181873/85631733-b0937180-b63b-11ea-930d-208eb562597e.PNG)

- Secondly, get the Isomeric Smile code by going to Tools > Information Card
![Isomeric](https://user-images.githubusercontent.com/64181873/85631939-049e5600-b63c-11ea-972a-7253c7a33a76.PNG)

- Thirdly, go to http://www.cheminfo.org/Chemistry/Cheminformatics/FormatConverter/index.html and paste in the Isomeric SMILES code into their editor.
![BabelPaste](https://user-images.githubusercontent.com/64181873/85632166-6e1e6480-b63c-11ea-8143-e1c528a94e31.PNG)

- Lastly, export the file as a svg once you're satisfied by how it looks. Make sure to add any sterochem or other modifications in the editor before
![BabelCopy](https://user-images.githubusercontent.com/64181873/85632630-4c71ad00-b63d-11ea-8e44-3363415d5405.PNG)

# Converting the svg to be manim_compatiable
- Begin by placing the initial svg file in the same directory as SvgConverter.py and typing the following into your command line.
- Syntax goes as follows `python SvgConverter.py [filename]`
![PythonConvert](https://user-images.githubusercontent.com/64181873/85633469-eb4ad900-b63e-11ea-81c5-fdd93d8f01b6.PNG)

- This should generate a file with the name `manim_[filename]`, you should move this to your manim's SVG directory.

# Using the file in manim.
- Once the file is in your directory test for the general shape by using the following code. Remember manim omits `<text/>` tags in svgs.
![Frame](https://user-images.githubusercontent.com/64181873/85634500-1f26fe00-b641-11ea-9fc1-9e649d6066c9.png)

- Finally, add non-carbon groups with color by using some relative positioning before putting the respective objects within a VGroup which you can call anytime.
![Complete](https://user-images.githubusercontent.com/64181873/85634989-75e10780-b642-11ea-91f1-33a11ecad4ff.png)
