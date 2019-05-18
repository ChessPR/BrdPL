# BrdPL - Board Games Programming Language (ICOM4036)
Developers:

Jean Paul Rivera

Roberto D. De Jesus

Francisco M. Valentin

# Project Description and Motivation:
The BrdPL programming language provides the programmer the tools necessary to start
creating any type of board game. If you need to create a board, some pieces to make 
the game fun or just throwing a dice, this language can simplify your life by just 
writing few lines of code. 

The idea of creating a board game Programming Language came since one of our teammates 
is a great chess player and the other two love to play others (not classic much classic) 
games. We also didn't had any other topic in mind so this one got the most votes. We then 
started to think of what features we could add to this language if we develop it and there
were several that will be explain later on this file.

If you are curious and what to find out more about features, how it works or see a 
demonstration you can find it below. 

# Introduction
Programing languages allows us to do almost anything with it. We have various languages to
choose from and each of them have their pros and cons. One of the main uses for programing
languages is the development of games. Since this area is a little complex, we decided to 
develop a new programming language powerful and simple enough to provide the necessary tools
for beginners who wish to create board games called BrdPL. BrdPL is a language based on Python,
one of the friendliest languages for beginners. This mean that the programmer will be able to
acquire new knowledge and improve their projects later on. Some of the start-up board games that
can be made quickly are checkers, tic-tac-toe, rolling dice, connect 4 and others. We will now
talk about some language features, a tutorial of how to use it, and explain the code. 

# Language Features
Board( # rows, # columns, set color1, set color2) 
- specify the size of the board by the numbers of rows and columns 
- you can set the board colors for example black and red for charckers.
- For details: [Board.py](Board.py)

Piece(image, name) 
- create piece with the given image and distinct name. 
- the movement is implemented seperately to preven limitations
- For details: [Piece.py](Piece.py)

Dice(Number)
- add the dice roll to the board game and specify the number of faces
- the range is from 1 to Number inclusive
- For details: [Dice.py](Dice.py)

Player( # of players)
- specify the maximum number of players
- each player will be have a unique identity from 1 to 4
- For details: [Player.py](Player.py)

Timer(boolean)
- adds time to the game
- For details: [Timer.py](Timer.py)

Rule --- falta


#Tutorial and Demo
Requirements:
1. Python 3.X
2. A text editor of you liking
3. Install the necesary import for the program(some imports don't work well on ubuntu, so windows is recomended)
4. After you download and extract, run the main class.
In the next video there will be a short demonstration video and a breif tutorial 
of how to use the BrdPL Programming language.

[![Watch the video]()](https://youtu.be/T-D1KVIuvjA)

# Implementation Description
The rules of the grammar and syntax of the BrdPL are written in Python. We also used the
PLY library as our lexical analyzer for the project grammar and for it to be readable by
the computer. This will enable the execution of code written in the BrdPL language. Finally,
the development of the project is aided by the use of GitHub to keep track of versions
and updates as well as serving as a place where others could access this finished product.

--- Add more

# Conclusion
As seen in the demo, the BrdPL Programming Language completed its task in developing board
games quickly and easily. This language reduce the amount of time required to develop a board
game. It also provides a breif knowledge in programming and does not limit the developer in
any way making it accessible for any adjustments. In our opinion, this project overpassed our
expectations since we had no idea of how to create a programming language. Lastly, we are
really excited with how the project ended and hope you enjoy it as well.

