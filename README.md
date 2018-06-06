# :computer: Chess-diagram-recognition  

Detect and identify a 2D chessboard and the configuration of its pieces through the  
application of image processing.  

## :page_facing_up: Description
First, we need to load image:  
![alt text](https://github.com/mr11261/Chess-diagram-recognition/blob/master/description/raw_image.jpg)  
Next job is to extract 2D diagram:  
![alt text](https://github.com/mr11261/Chess-diagram-recognition/blob/master/description/chess_diagram.jpg)  
Than, we will divide the diagram into 64 squares,  
and identify each piece:  
![alt text](https://github.com/mr11261/Chess-diagram-recognition/blob/master/description/chess_piece.jpg) ==> White queen!  

## :wrench: Tools
- Python
- NumPy
- OpenCV
- Tkinter

## :pushpin: Tasks
- [X] Detect 2D chess diagram in image using OpenCV.  
- [X] Collect more labeled data (both diagrams and squares).  
- [ ] Implement various machine learning algorithms to classify chess squares, and choose which work the best.  
- [ ] Use 'diagrams' dataset for detection (via deep learning), and compare it with previous methods.  

## :books: Datasets
- *diagrams* - croped diagrams from images  
- *squares* - divided into *black* and *white* subsets, each with 13 classes

## :bug: Known bugs
- Some diagrams in the photos may be rotated or distorted.  
- Not all diagrams are wrapped with black bounding box!

## :mortar_board: Author  
Stefan Ilic  
