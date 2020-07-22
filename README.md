# :computer: Chess-diagram-recognition  

Detect and identify a 2D chessboard and the configuration of its pieces through the  
application of image processing.  

## :movie_camera: Screenshot
<img src="https://github.com/IlicStefan/ChessDiagramRecognition/blob/master/screenshots/demo_video.gif" width="600" height="300" />

## :page_facing_up: Description
First, we need to load an image:  
![alt text](https://github.com/mr11261/Chess-diagram-recognition/blob/master/description/raw_image.jpg)  
Next job is to extract a 2D diagram:  
![alt text](https://github.com/mr11261/Chess-diagram-recognition/blob/master/description/chess_diagram.jpg)  
Then, we will divide the diagram into 64 squares,  
and identify each piece:  
![alt text](https://github.com/mr11261/Chess-diagram-recognition/blob/master/description/chess_piece.jpg) ==> White queen!  

## :wrench: Tools
- Python
- NumPy
- OpenCV
- Tkinter
- Tensorflow
- Keras
- And many more ...

## :pushpin: Tasks
- [X] Migrate Python2 to Python3
- [X] Refactor tools/raw_diagrams_to_diagrams.py
- [X] Refactor tools/diagrams_to_squares.py
- [X] Improve detection (Detect even rotated diagrams)
- [X] Build Application.py
- [ ] Build JavaScript Application
- [X] Data augmentation
- [X] Play with different learning models (use transfer learning)
- [X] Collect more labeled data (both diagrams and squares)

## :books: Datasets
- [Kaggle](https://www.kaggle.com/mr11261/chess-squares-from-chess-diagrams)
- *diagrams* - cropped diagrams from images  
- *squares* - divided into *black* and *white* subsets, each with 13 classes

## :bug: Known bugs
- For now, these are all features :)

## :mortar_board: Author  
Stefan Ilić  
