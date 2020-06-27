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
- And many more :(

## :pushpin: Tasks
- [X] Migrate Python2 to Python3
- [ ] Refactor tools/raw_diagrams_to_diagrams.py
- [ ] Refactor tools/diagrams_to_squares.py
- [ ] Improve detection (Detect even rotated diagrams)
- [ ] Build Application.py
- [ ] Build JavaScript Application
- [ ] Data augmentation
- [ ] Play to different learning models (use transfer learning)
- [ ] Collect more labeled data (both diagrams and squares)

## :books: Datasets
- *diagrams* - croped diagrams from images  
- *squares* - divided into *black* and *white* subsets, each with 13 classes

## :bug: Known bugs
- For now, these are all features :)

## :mortar_board: Author  
Stefan Ilic  
