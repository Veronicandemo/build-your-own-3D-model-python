# 3d-modeller

Humans are innately creative. We continuously build novel and interesting things. We assist write software that helps in
design and creation process.
Computer-aided design (CAD) software allows creators to design buildings, bridges, video game art, film monsters, 
3D printable objects, and many other things before building a physical version of the design.

A CAD tool must at least include these three things:
  -  A data structure to represent the design
  - The ability to display it to the screen
  - A method to interact with the design

Managing the interface and the main loop
Before rendering there are a few things that need to be setup 
   - A window to display the design in
     - Communicate with graphics drivers to render to the screen - use a cross-platform abstraction layer called OpenGL, 
            and a library called GLUT (the OpenGL Utility Toolkit) to manage our window.

## The Viewer

To manage the setting up of GLUT and OpenGL, and to drive the rest of the modeller, we create a class called Viewer. We use a single Viewer instance, which manages window creation and rendering, and contains the main loop for our program. 
In the initialization process for Viewer, we create the GUI window and initialize OpenGL.

