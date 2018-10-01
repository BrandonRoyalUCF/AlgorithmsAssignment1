# AlgorithmsAssignment1

Here is what we used to setup and run the program. 

1. Windows Instructions<br/>
  - Downloads<br/>
    - Pycharm<br/>
    - Git<br/>
    - Python 3.7 Interpreter<br/>
  - Once these were downloaded we used the version control of Pycharm in order to download the repository.<br/>
    - This only required https://github.com/BrandonRoyalUCF/AlgorithmsAssignment1.git copied into the clone from URL box.<br/>
    - NOTE: You may need to find your git.exe file and link pycharm to it in the settings.<br/>
    - The default location of git.exe is C:\Program Files\Git\bin\git.exe<br/>
  - Now the project should be open and downloaded. So next is setting up the interpreter.<br/>
    - You will need to open the project settings and select python interpreter from the left hand side<br/>
    - The default location for python 3.7 is C:\Users\<Insert username>\AppData\Local\Programs\Python\Python37-32\Python.exe<br/>
  - With the interpreter set we need to install an external library. To do this return to the project settings.<br/>
    - Under the python interpreter tab click the plus sign on the right hand side of the package manager.<br/>
    - I recommend a search at the top for matplotlib. You only need the package marked matplotlib all of the extras are not necessary.<br/>
    - Click install package at the bottom and wait the install will tell you when it is finished succesfully.<br/>
  - Finally, you will need to configure the script to run. Our script is "assignment1.py". <br/>
    - Once selected clicking run will run the program and the "performance.png" file will be created.<br/>
2. Settings<br/>
  - All our settings are listed immediately following the import calls.<br/>
  - needed<br/>
    - This is the size of the numbers that you would like added together. So entering a 4 will generate numbers of length 4.<br/>
  - plotFile<br/>
    - This is the name of the file that will be created that has the graph of time over runs.<br/>
  - numberOfIterations<br/>
    - This is how many pairs of numbers should be added together before the program will stop.<br/>
3. Final Notes<br/>
  - The program will also print each pair of numbers followed by their summation.<br/>
