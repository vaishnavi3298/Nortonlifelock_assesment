# Nortonlifelock_assesment

This program is created to display the following information analyzed from a dataset. The dataset can be found here: https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets

1.	The number of orphan planets (no star).
2.	The name (planet identifier) of the planet orbiting the hottest star.
3.	A timeline of the number of planets discovered per year grouped by size. Use the following groups: “small” is less than 1 Jupiter radii, “medium” is less than 2 Jupiter radii, and anything bigger is considered “large”. For example, in 2004 we discovered 2 small planets, 5 medium planets, and 0 large planets.

Two programs are written to achieve the above, namely main.py and assessment.py, main.py can read the input file and display the output by calling the desired functions in assesment.py
assessment.py has three functions to find the information given in the question

test.py is written to test the program. For this, I have created two input files namely input.json and input1.json and passed through main.py. test.py is used to see if the output is correct.

Note: input.json and input1.json are subset of the main input json file.

To run program:
1. Clone the repository to your local system
2. Go the path where it is located on terminal
3. Execute python main.py and the output will be displayed on your terminal

To run tests:
1. Execute python test.py and the it shows the output in your terminal


