# Matching-and-Verifying

# Task C: Runtime Analysis

![GS Matcher Time Graph](Graphics\GSMatcherTimeGraph.png)

The above graph is the representation of the time it takes for 
the program to match hospital and student pairs over n, the number
of students/hospitals. The graph appears to follow an exponential curve
with relatively little increase in runtime for small increases in the
input size and growing rapidly after the inputs cross 100.

This holds true for the verifier as well as can be seen below:

![GS Verifier Time Graph](Graphics\VerifierTimeGraph.png)

In both of these instances, it is clear that as the inputs increase
runtime increases at a faster and faster rate meaning that for much larger inputs
there would be significant problems posed.
