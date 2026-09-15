---
title: "Adding UML Diagrams to Doxygen documentation"
date: "2019-09-12"
layout: post
lang: en
---

If you are like me, you do not want to repeat yourself (DRY). In my working environment, we have to provide _traceability between design and code_ (according to ASpice process for SWE.2 and SWE.3). I want to combine the documentation of my code and my software design. My software design comprises algorithm documentation, class diagrams, behavioral diagrams, sketches and more. In addition I have interface documentation for all modules, which is mostly text directly attached to piece of code (e.g. documentation of a method, a data type, a class...). I also want to make sure that the SW detailed design and the code are in sync.

One possible approach to keep both the SW design and the code in sync is to model the SW detailed design in a model based engineering tool (e.g. Enterprise Architect) and document everything there, then generate the boilerplate code from there. However, EA is limited when it comes to specific C++ or C code. With C++, I find myself to be faster to work in a code editor, especially when defining templates. In my project, we also tried to create a C code generator plug-in for EA that covers everything, e.g. correct generation of defines, pointers to pointers, the ubiquitous const struct \* parameter etc., but in the end some thing were never generated quite correct and we also were faster with the text editor.

The other approach is to document your SW detailed design along with the code, and for that you usually use Doxygen in C/C++ development.

For me, a design cannot be communicated well without diagrams and pictures. Therefore, the most important Doxygen tag is the image tag.

## Including Images in Doxygen output

To include images in your design, you need to

- write the [_\\image_](http://doxygen.nl/manual/commands.html#cmdimage) tag in a Doxygen-parsed file to include images in-place into the documentation,
- add the folder containing the image(s) for your docu to the Doxygen config file (e.g. [IMAGE\_PATH](http://doxygen.nl/manual/config.html#cfg_image_path) = img/)
- add the images to the folder given above.

```
Example:
\image html "tic_stm_updateSyncState.png"
```

Doxygen will search through all directories given as paths (e.g. doc/img), and copy the images which the documentation references in the documentation output folder.

### Storing the images for the documentation in your project

If the images included by Doxygen are generated from some other source (e.g. your documentation build contains a pre-build step that does a graphics export from XML-based UML diagram files), you don't have to store them in your project.

But if you have binary graphics files you have created manually (either a snapshot or a a manual, baselined export of a diagram), I recomment storing them (and other detailed design artifacts used within the Doxygen docu) directly in your repository. Preferred image encoding format for design documentation is .svg, .png or .eps for LaTeX. Avoid bitmaps due to the large file size.

If you use git, you should use git LFS in your project to store binary files within the repository. To add the most common binary format image files to the git LFS tracking list, enter in each repo:

```
git lfs track '*.png' 
same for '*.gif', '*.jpg', '*.eps' ... (.svg is a text format).
```

see also: [https://github.com/git-lfs/git-lfs/wiki/Tutorial](https://github.com/git-lfs/git-lfs/wiki/Tutorial)

## Automatically Generated Diagrams

Doxygen can automatically generate some diagrams from the code:

- class diagrams
- include diagrams
- caller and call graph

The automatically generated class diagrams should be enabled by default, the others do not help too much in my opinion. The class diagram is a good start if you want to get some structural diagram, but it does not let you layout anything. For the diagrams, you need to install GraphWiz.

## Embedded text-based UML Diagrams with PlantUML

### About PlantUML

PlantUML is a diagram generator, which generates UML diagrams from a textual notation (similar to how LaTeX generates formatted documents from a textual markup language). PlantUML is a single Java archive file, which you need to reference in the Doxygen config file. Refer to the [PlantUML Download Page](http://plantuml.com/de/download) for download info.

Afterwards, edit the PLANTUML\_JAR\_PATH in the Doxyfile, set it to the location where you stored the plantuml.jar file, e.g. "C:\\TOOLS\\plantuml"

### Including PlantUML designs

Doxygen renders everything between a \\startuml and \\enduml command using PlantUML. Here's an example of PlantUML diagram embedded in a class documentation:

```
/** (...)
My component provides a globalTime API. This is how it works internally:

\startuml
Component_A -> MyComponent : getGlobalTime()
MyComponent -> D3_timeProvider: getGlobalTime()
MyComponent -> MyComponent:convertGlobalTimeToUS()
MyComponent --> Component_A: CGlobalTimestamp
\enduml

(...)*/
```

If the diagram becomes more complex or if you want to include a PlantUML diagram in a markdown page, make use of the [PlantUML include syntax](http://plantuml.com/de/preprocessing) and put the PlantUML diagram code in a separate file. This also allows you to edit the PlantUML diagram in an editor with a diagram preview, e.g. PlantUML QEditor or Visual Studio Code with the PlantUML extension.

This is the PlantUML include command, used in Doxygen:

```
\startuml
!include tic_seq_api_calls.puml
\enduml


```

 

This is the generated PlantUML output for both variants:

![2019-09-12_10h26_22.png](/assets/img/posts/2019-09-12-adding-uml-diagrams-to-doxygen-documentation/2019-09-12_10h26_22.png)

Please be aware that PlantUML does not work with compiled HTML output (\*.chm). Similar to other SVG-based features, the .chm documentation will just show an IE-style "page not found" frame instead of the actual picture. PlantUML output works with the Doxygen HTML browsable output.

## Including other UML diagram tool output

### EA Diagrams

If you want to include EA diagrams, you have to export them from the EA model first. This is how:

Export to PNG or other format:

1. Open the diagram
2. Click on Menu "Diagram → Save Image to File..." (CTRL-T)
3. Select "PNG" as file format and save

Export to SVG:

1. Download and install the SVG diagram export add-in from: [https://community.sparxsystems.com/community-resources/706-svg-diagram-export-add-in](https://community.sparxsystems.com/community-resources/706-svg-diagram-export-add-in)
2. export

The SVG export has the advantage of smaller file sizes and a scalable graphic (but again, the images will not be rendered in Doxygen compiled HTML output).

### UMLet, yED

These editors allow lightweight creation of UML diagrams, and the diagrams are saved in a text-baed format (an XML-based format), which is nice for handling them in version control systems like git. Anyhow, the diagrams need to be converted to a format that Doxygen can read.

I have not evaluated these diagram editors and their automated export capabilities yet, but wanted to mention them for completeness, as they are also used in some projects I have seen.

 

I hope this overview is helpful for you. My personal favorite is PlantUML integration for simple behavioral diagrams and EA export for complex structural or mixed-type diagrams.
