# Matching-and-Verifying

# Authors
John (Jack) Kellen | UFID: 85033113

# How To Run
To work with this project:
1) Clone the repository to your local machine
2) Open project in a Python IDE
3) Open the main.py file and run it

Following these instructions will run the default setup that we have
where an input of n=16 is run through the matcher which generates an
output_x.txt file in the Data\Output folder.

For custom inputs, you can add the input .txt file to the Data\Input
folder and then copy the relative path without the Matching-and-Verifying
portion and assign the input variable on main.py to it. Then run the
program. This will generate and verify the results of the process.

To Test the verifier on its own simply change the testVerifierAlone
variable to True and then change the input and output filepaths
to your desired ones. We have set up an example of an Invalid
input and an Unstable input in the file already.

# Assumptions
1) All inputs will be in the Input folder
2) For an input to work it must be formatted as specified in the assignment or it will be viewed as Invalid
3) All outputs will be in the output folder
4) For an output to work it must be formatted as specified in the assignment or it will be viewed as Invalid

# Task C: Runtime Analysis

<img src="Graphics\GSMatcherTimeGraph.png" width="600" height="450">

The above graph is the representation of the time it takes for 
the program to match hospital and student pairs over n, the number
of students/hospitals. The graph appears to follow an exponential curve
with relatively little increase in runtime for small increases in the
input size and growing rapidly after the inputs cross 100.

This holds true for the verifier as well as can be seen below:

<img src="Graphics\VerifierTimeGraph.png" width="600" height="450">

In both of these instances, it is clear that as the inputs increase
runtime increases at a faster and faster rate meaning that for much larger inputs
there would be significant problems posed.
